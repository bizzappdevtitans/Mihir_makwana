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
        selection_add=[
            ("drop shiping", "Drop Shiping"),
        ],
    )
