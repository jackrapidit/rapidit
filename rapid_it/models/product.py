from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _prepare_item_dict(self):
        res = super(ProductTemplate, self)._prepare_item_dict()
        res['Item']['SKU'] = self._ebay_encode(self.default_code)
        return res