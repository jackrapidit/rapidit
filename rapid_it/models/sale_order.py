from odoo import api, fields, models, _
import logging
from odoo.addons.sale_ebay.models import product

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = 'Smart IT custom changes to the base Sale Oder Module'

    @api.model
    def _process_order(self, order):
        for transaction in order['TransactionArray']['Transaction']:
            so = self.env['sale.order'].search(
                [('client_order_ref', '=', transaction['OrderLineItemID'])], limit=1)
            try:
                if not so:
                    so = self._process_order_new(order, transaction)
                    so._process_order_update(order)
            except Exception as e:
                message = _("Ebay could not synchronize order:\n%s") % str(e)
                path = str(order)
                product._log_logging(self.env, message, "_process_order", path)
                _logger.exception(message)

    @api.model
    def _process_order_new(self, order, transaction):
        (partner, shipping_partner) = self._process_order_new_find_partners(order)
        fp = self.env['account.fiscal.position'].get_fiscal_position(partner.id, delivery_id=shipping_partner.id)
        if fp:
            partner.property_account_position_id = fp
        create_values = {
            'partner_id': partner.id,
            'partner_shipping_id': shipping_partner.id,
            'state': 'draft',
            'client_order_ref': transaction['OrderLineItemID'],
            'origin': 'eBay' + transaction['OrderLineItemID'],
            'fiscal_position_id': fp.id,
            'date_order': product._ebay_parse_date(order['PaidTime']),
        }
        if self.env['ir.config_parameter'].sudo().get_param('ebay_sales_team'):
            create_values['team_id'] = int(
                self.env['ir.config_parameter'].sudo().get_param('ebay_sales_team'))

        sale_order = self.env['sale.order'].create(create_values)

        sale_order._process_order_new_transaction(transaction)

        sale_order._process_order_shipping(order)

        return sale_order
