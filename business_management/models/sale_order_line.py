from odoo import models


# inherit sale.order.line object # T00412
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _timesheet_create_project_prepare_values(self):
        """Inherit method for passing value from sale order to project. #T00412"""
        valuepassing = super(
            SaleOrderLine, self
        )._timesheet_create_project_prepare_values()
        valuepassing["project_description"] = self.order_id.project_description
        return valuepassing

    def _timesheet_create_task_prepare_values(self, project):
        """Inherit method for passing value from sale order to task. #T00412"""
        valuepassing = super(SaleOrderLine, self)._timesheet_create_task_prepare_values(
            project
        )
        valuepassing.update({"task_description": self.order_id.task_description})
        return valuepassing
