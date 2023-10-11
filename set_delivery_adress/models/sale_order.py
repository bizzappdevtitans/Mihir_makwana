from odoo import api, models


# inherit sale.order object # T00458
class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        if self.partner_id and self.partner_id.company_type == "company":
            individual_with_delivery_adress = self.partner_id.child_ids.filtered(
                lambda a: a.delivery_adress and a.company_type == "individual"
            )
            if individual_with_delivery_adress:
                self.partner_shipping_id = individual_with_delivery_adress[0]

            else:
                self.partner_shipping_id = self.partner_id

        else:
            self.partner_shipping_id = self.partner_id
