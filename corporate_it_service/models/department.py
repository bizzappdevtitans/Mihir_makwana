# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


# create a class for a HR Department #T00472
class HrDepartment(models.Model):
    _name = "hr.department"
    _inherit = "hr.department"
    # fields for a hr.department #T00472
    department_head_id = fields.Many2one(
        comodel_name="res.users", string="Department Head"
    )
    location_of_department = fields.Char(string="Location")
    budget_of_department = fields.Float(string="Budget")
    budget_currency_id = fields.Many2one(
        comodel_name="res.currency", string="Currency of Budget"
    )
    contact = fields.Many2many(comodel_name="res.partner", string="Additional Contact")
    department_code = fields.Char(string="Code")
    parent_department = fields.Many2one(
        comodel_name="hr.department", string="Parent of the Department"
    )
