from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    _delivery_description = fields.Text(string="Delivery Description")
    _purchase_description = fields.Text(string="Purchase Description")

    def _get_new_picking_values(self):
        """This method use to pass value from sale order to delivery #T000394"""
        results = super(StockMove, self)._get_new_picking_values()
        delivery_description = self.group_id.sale_id.delivery_description
        results["delivery_description"] = delivery_description
        return results

    def _prepare_procurement_values(self):
        """This function will work access  value from the sale #T00409"""
        value = super(StockMove, self)._prepare_procurement_values()
        value[
            "manufacturing_order_description"
        ] = self.group_id.sale_id.manufacturing_order_description
        return value
