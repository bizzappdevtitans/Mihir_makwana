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

    options = fields.Selection(
        [
            ("category", "Based On Category"),
            ("selected_lines", "Selected lines"),
            ("one_line_per_order", "One line per order"),
        ],
        required=True,
    )
    sale_order_line_ids = fields.Many2many(
        comodel_name="sale.order.line", string="Sale Order Lines "
    )

    def action_confirm_split_sale_order(self):
        """This method is use to split sale order for each category and
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

    def split_sale_order_on_selected_lines(self):
        """This method is use of create a sale  selected line #T00483"""
        if not self.sale_order_line_ids:
            raise ValidationError(_("Please Select The Sale order Lines "))

        for order_lines in self.sale_order_line_ids:  # get sale order line #T00483
            sale_order_lines = []

            for product in order_lines:
                sale_order_lines.append(
                    (
                        0,
                        0,
                        {
                            "product_id": product.product_id.id,
                            "product_uom_qty": product.product_uom_qty,
                        },
                    )
                )

            self.env["sale.order"].create(
                {
                    "partner_id": self.sale_order_id.partner_id.id,
                    "order_line": sale_order_lines,
                }
            )

    def split_sale_order_on_sale_order_per_line(self):
        """This method is use of create a sale order from every sale order line #T00483"""
        context = dict(self._context)

        sale_order = self.env["sale.order"].browse(context.get("active_id", False))
        order_lines = sale_order.mapped("order_line")
        if len(order_lines) <= 1:
            raise ValidationError(_("Please Add A Multiple Sale Order Line"))

        for products in order_lines:
            sale_order = self.env["sale.order"].create(
                {
                    "partner_id": self.sale_order_id.partner_id.id,
                }
            )
            self.env["sale.order.line"].create(
                {
                    "order_id": sale_order.id,
                    "product_id": products.product_id.id,
                    "product_uom_qty": products.product_uom_qty,
                }
            )

    def action_split_done(self):
        """done split order action of Wizard #T00483"""
        if self.options == "category":
            self.action_confirm_split_sale_order()
        if self.options == "selected_lines":
            self.split_sale_order_on_selected_lines()
        if self.options == "one_line_per_order":
            self.split_sale_order_on_sale_order_per_line()
