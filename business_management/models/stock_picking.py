from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # fields for #T00394
    _delivery_description = fields.Text(string="Delivery Description")
