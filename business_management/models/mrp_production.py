from odoo import fields, models

# inherit mrp.production object # T00409


class MrpProduction(models.Model):
    _inherit = ["mrp.production"]
    # fields for #T00409
    manufacturing_order_description = fields.Text(string="Manufacturing Description")
