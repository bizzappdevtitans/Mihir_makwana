from odoo import models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        """This method use to pass value from sale order to downpayment invoice #T000380"""
        invoice_value = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(
            order, name, amount, so_line
        )
        invoice_value.update({"invoice_description": order.invoice_description})
        return invoice_value
