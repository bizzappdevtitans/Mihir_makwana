from odoo import fields, models


# inherit sale.order object # T00378
class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    # create a field for a sale order #T000380
    invoice_description = fields.Char()
    delivery_description = fields.Char()
    # create a field for a purchase order #T000393
    purchase_description = fields.Char()
    # create a field for a manufacturing  order #T000409
    manufacturing_order_description = fields.Char(string="Manufacturing Description")
    # create a field for a project  #T000412
    project_description = fields.Char()
    task_description = fields.Char()

    def _prepare_invoice(self):
        """This Method passing value sale order to create an regular invoice #T00380"""
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals["invoice_description"] = self.invoice_description
        return invoice_vals
