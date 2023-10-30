from odoo import fields, models


class AccountMove(models.Model):
    _inherit = ["account.move"]

    # fields for #T000380
    customer_number = fields.Char()
    delivery_description = fields.Text()
    invoice_description = fields.Text()
