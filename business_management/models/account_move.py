from odoo import fields, models


class AccountMove(models.Model):
    _inherit = ["account.move"]

    # fields for #T000380
    _customer_number = fields.Char(string="Customer Number")
    _delivery_description = fields.Text(string="Delivery Description")
    _invoice_description = fields.Text(string="Invoice Description")
