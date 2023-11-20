# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # fields for #T0048
    sale_order_reference = fields.Char()
