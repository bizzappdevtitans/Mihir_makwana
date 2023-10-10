from odoo import models


# inherit sale.order object # T00378
class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    def partner_invoice_adress(self):
        """This Method set delivery adress #T00458"""

    # adding a field for a set a delivery adress for #T00458
    # partner_invoice_adress_id = fields.Many2one(
    #     "res.partner",
    #     string="Invoice Address",
    #     readonly=True,
    #     required=True,
    #     compute="",
    #     domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    # )
