# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


# inherit res.partner object # T00458
class ResPartner(models.Model):
    _inherit = "res.partner"

    # create a field for a #T00458
    delivery_adress = fields.Boolean(
        string=" Is Delivery Address ? ", help=" is adress is a delivery adress ??"
    )

    type = fields.Selection(
        [
            ("contact", "Contact"),
            ("invoice", "Invoice Address"),
            ("delivery", "Delivery Address"),
            ("other", "Other Address"),
            ("private", "Private Address"),
            ("Drop Shiping", "drop shiping"),
        ],
        string="Address Type",
        default="contact",
        help="Invoice & Delivery addresses are used in sales orders. Private addresses are only visible by authorized users.",
    )
