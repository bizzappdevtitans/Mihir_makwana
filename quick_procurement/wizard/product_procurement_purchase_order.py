# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date

from odoo import _, fields, models
from odoo.exceptions import ValidationError


class ProductProcurementPurchaseOrder(models.TransientModel):
    _name = "product.procurement.purchase.order"
    _description = "Product Procurement Purchase Order"

    scheduled_date = fields.Date(default=date.today())
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Vendor",
        required=True,
    )

    def product_to_purchase_order_wizard(self):
        model = self.env.context.get("active_model")
        product_id = self.env.context.get("active_id")

        if model == "product.product":
            sale_order_values = self.env["sale.order"].search(
                [
                    ("order_line.product_id", "=", product_id),
                    ("date_order", ">", self.scheduled_date),
                    ("state", "=", "sale"),
                ]
            )

            purchase_order_values = self.env["purchase.order"].search(
                [
                    ("order_line.product_id", "=", product_id),
                    ("date_planned", ">", self.scheduled_date),
                    ("state", "=", "purchase"),
                ]
            )

            total_sale_order_quantity = sum(
                sale_order_values.order_line.mapped("product_uom_qty")
            )
            total_purchase_order_quantity = sum(
                purchase_order_values.order_line.mapped("product_qty")
            )
            total_quantity = total_sale_order_quantity - total_purchase_order_quantity

            if total_quantity <= 0:
                raise ValidationError(_(f"YOU CAN NOT PURCHASE {total_quantity} "))
            values = {
                "partner_id": self.partner_id.id,
                "order_line": [
                    (0, 0, {"product_id": product_id, "product_qty": total_quantity})
                ],
            }
            self.env["purchase.order"].create(values)
        else:
            return sale_order_values
