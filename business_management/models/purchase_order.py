from odoo import fields, models


# inherit purchase.order object # T00393
class PurchaseOrder(models.Model):
    _inherit = ["purchase.order"]
    # fields for #T00393
    _purchase_description = fields.Text(string="Purchase Description")
