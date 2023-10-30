from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _prepare_purchase_order(self, company_id, origins, values):
        """This function is passing  value sale order to purchase order  #T00393"""
        value = super()._prepare_purchase_order(
            company_id=company_id, origins=origins, values=values
        )
        value["purchase_description"] = values[0].get("sale").about_purchase
        return value

    def _prepare_mo_vals(
        self,
        product_id,
        product_qty,
        product_uom,
        location_id,
        name,
        origin,
        company_id,
        values,
        bom,
    ):
        """This function is passing  value sale order to purchase order  #T00409"""
        result = super(StockRule, self)._prepare_mo_vals(
            product_id,
            product_qty,
            product_uom,
            location_id,
            name,
            origin,
            company_id,
            values,
            bom,
        )
        result["manufacturing_order_description"] = values.get(
            "manufacturing_order_description"
        )
        return result
