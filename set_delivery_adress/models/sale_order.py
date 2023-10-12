from odoo import api, models


# inherit sale.order object # T00458
class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        """Update the delivery_adress fields when the partner is select # T00458"""
        if self.partner_id and self.partner_id.company_type == "company":
            # if we select a company  while filter that record who has
            # company_type is individule # T00458
            individual_with_delivery_adress = self.partner_id.child_ids.filtered(
                lambda a: a.delivery_adress and a.company_type == "individual"
            )
            if individual_with_delivery_adress:
                # when  company has individule that time delivery address
                # will be individules adress # T00458
                self.partner_shipping_id = individual_with_delivery_adress[0]

            else:
                # otherwise delivery adress is a partners delivery  address # T00458
                self.partner_shipping_id = self.partner_id

        else:
            self.partner_shipping_id = self.partner_id
