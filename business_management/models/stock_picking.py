from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # fields for #T00394
    delivery_description = fields.Text()
