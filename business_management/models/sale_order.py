from odoo import fields, models


# inherit sale.order object # T00378
class SaleOrder(models.Model):
    _inherit = ["sale.order"]

    # create a field for a sale order #T000380
    _customer_number = fields.Char(string="Customer number")
    _invoice_description = fields.Text(string="Invoice Description")
    _delivery_description = fields.Text(string="Delivery Description")
    # create a field for a purchase order #T000393
    purchase_description = fields.Text(string="purchase description")
    # create a field for a manufacturing  order #T000409
    manufacturing_order_description = fields.Text(string="Manufacturing Description")
    # create a field for a project  #T000412
    _project_description = fields.Char(string="Project Description")
    _task_description = fields.Char(string="Task Description")

    def _prepare_invoice(self):
        """This Method passing value sale order to create an invoice #T00380"""
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals["invoice_description"] = self.invoice_description
        return invoice_vals
