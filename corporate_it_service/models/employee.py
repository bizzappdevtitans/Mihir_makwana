# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models


# create a class for a employee #T00472
class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee information"
