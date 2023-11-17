# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SplitSaleOrderWizard(models.Model):
    _name = "split.sale.order.wizard"
    _description = "Split Sale Order"

    # fields #T00483
    sale_order_id = fields.Many2one(
        comodel_name="sale.order", string="Sale Order Number"
    )

    is_split_sale_order_based_on_category = fields.Boolean(
        string="Based On Category ?", default=True
    )

    def action_confirm_split_sale_order(self):
        """This method is use to split sale order and
        already sale order is splited so that time Raise Validation  #T00483"""
        if not self.sale_order_id.sale_order_reference:
            if self.is_split_sale_order_based_on_category:
                product_category_dict = {}

                for order_line in self.sale_order_id.order_line:
                    product_category = order_line.product_id.categ_id

                    if product_category not in product_category_dict:
                        new_sale_order = self.env["sale.order"].create(
                            {
                                "partner_id": self.sale_order_id.partner_id.id,
                                "sale_order_reference": self.sale_order_id.name,
                            }
                        )
                        product_category_dict[product_category] = new_sale_order

                    self.env["sale.order.line"].create(
                        {
                            "product_id": order_line.product_id.id,
                            "order_id": new_sale_order.id,
                        }
                    )

            else:
                raise ValidationError(_(" PLEASE CHECK FIELDS "))

        else:
            raise ValidationError(_(" ALREADY SPLITED"))
