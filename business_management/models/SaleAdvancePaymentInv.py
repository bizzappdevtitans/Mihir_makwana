from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        """This method use to pass value from sale order to invoice #T000380"""
        create_invoice = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(
            order, name, amount, so_line
        )
        create_invoice.update({"invoice_description": order.invoice_description})
        return create_invoice
