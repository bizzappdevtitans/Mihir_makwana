from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


# school_management/school_teacher.py #T00339
class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "school teachers"
    _rec_name = "teacher_name"

    # teacher attributes fields #T00339
    image = fields.Image()
    teacher_name = fields.Char(
        string="Name",
        required=True,
    )
    gender = fields.Selection([("male", "MALE"), ("female", "FEMALE")])
    teacher_dob = fields.Date(string="age")
    age = fields.Integer(readonly=True, compute="_compute_age")
    teacher_number = fields.Char(string="Conatact Number")
    teacher_email = fields.Char(string="Email")
    count = fields.Integer(compute="_compute_count")

    # selection field
    class_teacher = fields.Selection(
        [
            ("std1", "STD-1"),
            ("std2", "STD-2"),
            ("std3", "STD-3"),
            ("std4", "STD-4"),
            ("std5", "STD-5"),
            ("std6", "STD-6"),
            ("std7", "STD-7"),
            ("std8", "STD-8"),
            ("std9", "STD-9"),
            ("std10", "STD-10"),
        ],
        string="Standard",
    )
    degree = fields.Selection(
        [
            ("phd", "PHD"),
            ("m.tech", "M.TECH"),
            ("b.tech", "B.TECH"),
            ("b.ed", "B.ED"),
            ("m.ed", "M.ED"),
        ],
        string="Qualifiaction",
    )
    teacher_subject = fields.Selection(
        [
            ("english", "ENGLISH"),
            ("hindi", "HINDI"),
            ("gujrati", "GUJRATI"),
            ("social scince", "SOCIAL SCINCE"),
            ("computer", "COMPUTER"),
        ]
    )

    teacher_experience = fields.Char(string="Experience", default=" years")
    teacher_feedback = fields.Text(
        string="your feedback",
        default="your feedback is important for us THANK YOU !!!",
    )
    document_upload = fields.Image(string="upload document")
    skills = fields.Text(string="skills", help="add your skill")

    @api.ondelete(at_uninstall=False)
    def _ondelete_restrict(self):
        """This is a _ondelete orm method for #T00339"""
        for record in self:
            if record.teacher_name:
                raise ValidationError(_("You have NO access to delete an record"))

    @api.depends("teacher_dob")
    def _compute_age(self):
        """this method is calculate the teacher age #T00368"""
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(), rec.teacher_dob).years

    # check age is valid
    @api.constrains("age")
    def validate_teacher_age(self):
        """This method is validate a teacher age #T00368"""
        minimum_age = int(
            self.env["ir.config_parameter"].get_param(
                "school_management.minimum_teacher_age"
            )
        )
        if self.age < minimum_age:
            raise ValidationError(
                _("Below 20 years teacher cannot register in school ")
            )

    @api.constrains("teacher_number")
    def check_mobile_no(self):
        """This method for a validate a user mobile number #T00339"""
        if self.teacher_number:
            record_count = self.search_count(
                [("teacher_number", "=", self.teacher_number)]
            )
            if record_count > 1:
                raise ValidationError(_("Mobile no. already exist."))

    @api.constrains("age")
    def validate_age(self):
        """This method is use the system parameter in module T00368"""
        maximum_age = int(
            self.env["ir.config_parameter"].get_param(
                "school_management.maximum_teacher_age"
            )
        )
        if self.age:
            if self.age > maximum_age:
                raise ValidationError(
                    _("Above 60 years teacher not allow to teach in our school")
                )
