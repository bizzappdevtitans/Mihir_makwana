# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from datetime import date

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

available_priority = [
    ("0", "Normal"),
    ("1", "Good"),
    ("2", "Very Good"),
    ("3", "Excellent"),
]


# create a class for a applicant
class JobApplicant(models.Model):
    _name = "it.applicant"
    _description = "Job Applicant"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # fields for applicant
    name = fields.Char(
        string="Applicant Id",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
    )
    is_active = fields.Boolean(string="Active", default=True, required=True)
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
    availability = fields.Date(string="Availability of Applicant", required=True)

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
        string="Job Platform",
        help="Which Plateform to find job",
    )

    attachment_cv = fields.Binary(string="Attach your CV")
    image = fields.Binary(string="Applicant Image", attachment=True)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        store=True,
    )
    position_ids = fields.Many2one(
        comodel_name="job.position", string="Already Apply Jobs"
    )
    stage_id = fields.Many2one(
        comodel_name="applicant.stages",
        string="Stage",
        store=True,
        readonly=True,
        compute="_compute_stage",
    )
    active_applicant = fields.Boolean(string="Active ", default=True)
    state_kanban = fields.Selection(
        [
            ("normal", "In progress"),
            ("done", "Ready for next stage"),
            ("blocked", "Blocked"),
        ],
        string="State",
        copy=False,
        default="normal",
    )
    priority_selection = fields.Selection(
        available_priority, string="Priority", default="0"
    )

    def action_cancle(self):
        """This method is use in wizard for a cancle a application for #T00472"""
        action = self.env.ref(
            "corporate_it_service.action_applicant_wizard_form_view"
        ).read()[0]
        return action

    def action_create_position(self):
        """This method is use in wizard for a create a record #T00472"""
        action = self.env.ref(
            "corporate_it_service.action_position_wizard_form_view"
        ).read()[0]
        return action

    def action_share_in_whatsapp(self):
        """This method is use to share into whatsapp massages  #T00472"""
        if not self.mobile:
            raise ValidationError(_("Missing your phone number !!!!!!"))
        message = "HI %s ,YOUR APPLICATION ID IS : %s, THANK YOU " % (
            self.applicant_id,
            self.name,
        )
        whatsapp_api_url = "https://api.whatsapp.com/send?phone=%s&text=%s" % (
            self.mobile,
            message,
        )
        return {"type": "ir.actions.act_url", "target": "new", "url": whatsapp_api_url}

    # @api.onchange("mobile")
    # def validate_phone(self):
    #     if self.mobile:
    #         match = re.match("^[0-9]{10}$", self.mobile)
    #         if match == None:
    #             raise ValidationError(_("Invalid Mobile Number"))

    @api.model
    def create(self, vals):
        """This method is use to defult applicant id is NEW  #T00472"""
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code("it.applicant") or _(
                "New"
            )

        res = super(JobApplicant, self).create(vals)
        return res

    def action_send_email(self):
        """This method is use to a send a email  #T00472"""
        records = self.env["it.applicant"].search([])
        for record in records:
            if record.applicant_date == date.today():
                mail_template = self.env.ref(
                    "corporate_it_service.apllicant_email_template"
                )
                mail_template.send_mail(record.id, force_send=True)

    @api.depends("position_ids")
    def _compute_stage(self):
        for applicant in self:
            if applicant.position_ids:
                if not applicant.stage_id:
                    stage_ids = self.env["applicant.stages"].search([], limit=1).ids
                    applicant.stage_id = stage_ids[0] if stage_ids else False
            else:
                applicant.stage_id = False

    def action_status_potential(self):
        """This method is use to change the state #T00472"""
        self.state_kanban = "done"

    def action_status_blocked(self):
        """This method is use to change the state #T00472"""
        self.state_kanban = "blocked"

    @api.constrains("applicant_email")
    def _check_email_of_the_applicant(self):
        """This method is use to validate a email  #T00472"""
        for record in self:
            valid_applicable_email = re.match(
                "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z|a-z]{2,7}",
                record.applicant_email,
            )
            if valid_applicable_email is None:
                raise ValidationError(_("Please Enter a Valid Email"))

    @api.constrains("salary_expect")
    def _check_salary_expected_of_the_applicant(self):
        """This method is use to constrains to validate a salary #T00472"""
        for record in self:
            if record.salary_expect <= 0:
                raise ValidationError(_("Expected salary must be greater than 0"))
