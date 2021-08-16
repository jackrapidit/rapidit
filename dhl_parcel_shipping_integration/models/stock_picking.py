from odoo import models, fields


class AfterShipTrackingNumber(models.Model):
    _inherit = 'stock.picking'

    collection_Job_Number = fields.Char(string="Dhl Parcel Collection Job Number",
                                        help="for collection job number plz enter authentication Token number")
