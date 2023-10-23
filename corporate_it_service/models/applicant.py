import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class JobApplicant(models.Model):
    _name = "it.applicant"
    _description = "Job Applicant"
    # _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Applicant Id",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
    )
    active_boolean = fields.Boolean(string="Active", default=True, required=True)
    applicant_id = fields.Char(string="Applicant Name", required=True)
    mobile = fields.Char(string="Applicant Mobile", store=True)
    applicant_email = fields.Char(
        string="Email", help="Applicant Email", required=True, store="True"
    )
    applicant_degree = fields.Selection(
        [
            ("bba", "BBA"),
            ("mba", "MBA"),
            ("bca", "BCA"),
            ("bsc", "BSC"),
            ("msc", "MSC"),
            ("b.tech", "B.TECH"),
            ("m.tech", "M.TECH"),
            ("phd", "PHD"),
        ],
        string="Highest Degree",
    )
    applicant_date = fields.Date(
        string="Application Date", readonly=True, default=fields.datetime.now()
    )
    salary_expect = fields.Float(
        string="Salary Expectation",
        store=True,
        required=True,
    )
    platform_via = fields.Selection(
        [
            ("facebook", "FACEBOOK"),
            ("linkedin", "LINKEDIN"),
            ("website", "OUR WEBSIDE"),
            ("google", "GOOGLE"),
        ],
        string="Which Plateform to find job",
    )
    attachment_cv = fields.Binary(string="Attach your CV")
    image = fields.Binary(string="Applicant Image", attachment=True)
    # department_id = Many2one(
    #     comodel_name="hr.department",
    #     string="Department",
    #     compute="_compute_department",
    #     store=True,
    # )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        store=True,
    )
    position_ids = fields.Many2one(
        comodel_name="job.position", string="Alrrady Apply Jobs"
    )

    """@api.depends("job_id", "department_id")
                def _compute_company(self):
                    for applicant in self:
                        company_id = False
                        if applicant.department_id:
                            company_id = applicant.department_id.company_id.id
                        if not company_id and applicant.job_id:
                            company_id = applicant.job_id.company_id.id
                        applicant.company_id = company_id or self.env.company.id
            """

    @api.constrains("applicant_email")
    def _check_email_of_the_applicant(self):
        for record in self:
            valid_applicable_email = re.match(
                "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,7}",
                record.applicant_email,
            )
            if valid_applicable_email is None:
                raise ValidationError(_("Please Enter a Valid Email"))

    @api.constrains("salary_expect")
    def _check_salary_expected_of_the_applicant(self):
        for record in self:
            if record.salary_expect <= 0:
                raise ValidationError(_("Expected salary must be greater than 0"))

    @api.onchange("mobile")
    def validate_applicant_phone(self):
        """this method is validate applicant mobile number"""
        if self.mobile:
            match = self.mobile.match("^[0-9]{10}$", self.mobile)
            if match is None:
                raise ValidationError(_("Invalid Mobile Number"))

    # @api.depends("department_id")
    # def _compute_department(self):
    #     for applicant in self:
    #         applicant.department_id=
