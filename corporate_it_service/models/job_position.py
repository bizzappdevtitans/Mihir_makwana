# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


# create a class for a job position #T00472
class JobPositions(models.Model):
    _name = "job.position"
    _description = "Employee position"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    # fields for a #T00472
    name = fields.Char(string="Position Name", required=True)
    description = fields.Text(string="Descriptions")
    company_id = fields.Many2one(comodel_name="res.partner", string="Company")
    department_id = fields.Many2one(comodel_name="hr.department", string="Department")
    recruiter_id = fields.Many2one(comodel_name="res.users", string="Recruiter")
    recruitment = fields.Integer(string="recruitments")
    date_of_open = fields.Date(string="Job Opening Date")
    date_of_closing = fields.Date(string="Job Closing Date")
    applicants_ids = fields.One2many(
        comodel_name="it.applicant", inverse_name="position_ids", string="Applicants"
    )
    salary_proposed = fields.Float(string="salary")

    @api.constrains("salary_proposed")
    def _check_salary_proposed_of_the_applicant(self):
        """This method is use to validate a salary #T00472"""
        for record in self:
            if record.salary_proposed <= 0:
                raise ValidationError(_("Proposed Salary Must Be Greater Than 0"))

    @api.constrains("recruitment")
    def _check_recruitment_of_the_applicant(self):
        """This method is use to validate a salary #T00472"""
        for record in self:
            if record.recruitment <= 0:
                raise ValidationError(_("Recruitment Must Be Greater Than 0"))

    @api.constrains("date_of_open", "date_of_closing")
    def _check_date_validation_on_recruitment(self):
        """This method is use to validate a date  #T00472"""
        for record in self:
            if record.date_of_open > record.date_of_closing:
                raise ValidationError(_("Opening Date Must be Lessthen Closing Date"))
