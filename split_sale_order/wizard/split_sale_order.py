from odoo import fields, models


class SplitSaleOrderWizard(models.Model):
    _name = "spli.sale.order.wizard"
    _description = "Split Sale Order"

    is_split_sale_order_based_on_category = fields.Boolean(
        string="Split SO Based On Category ?"
    )

    def action_confirm_so_order(self):
        pass
