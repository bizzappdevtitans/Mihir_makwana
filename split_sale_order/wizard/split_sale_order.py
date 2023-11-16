# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SplitSaleOrderWizard(models.Model):
    _name = "split.sale.order.wizard"
    _description = "Split Sale Order"

    sale_order_id = fields.Many2one(
        comodel_name="sale.order", string="Sale Order Number"
    )

    is_split_sale_order_based_on_category = fields.Boolean(
        string="Based On Category ?", default=True
    )

    def action_confirm_split_sale_order(self):
        if not self.sale_order_id.sale_order_reference:
            if self.is_split_sale_order_based_on_category:
                product_category_list = []

                for products in self.sale_order_id.order_line:
                    if products.product_id.categ_id.name not in product_category_list:
                        product_category_list.append(products.product_id.categ_id.name)

                    self.env["sale.order"].create(
                        {
                            "partner_id": self.sale_order_id.partner_id.id,
                            "sale_order_reference": self.sale_order_id,
                            "order_line": product_category_list,
                        }
                    )

            else:
                raise ValidationError(_("INVALID !!!!!!!!!!!!!"))
        else:
            raise ValidationError(_(" ALREADY SPLITED"))
