from odoo import fields, models


class AccountMove(models.Model):
    _inherit = ["account.move"]

    # fields for #T000380
    delivery_description = fields.Char()
    invoice_description = fields.Char()
