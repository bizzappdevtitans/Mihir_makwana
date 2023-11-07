from datetime import date, timedelta

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SchoolManagement(models.Model):
    _name = "student.name"
    _description = "school students"
    _rec_name = "name"

    # student attributes fields #T00339
    name = fields.Char(required=True)
    # selection field #T00339
    std = fields.Selection(
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
    roll = fields.Integer(string="Roll number")
    course = fields.Selection(
        [("gseb", "GSEB"), ("ncert", "NCERT")],
    )
    gender = fields.Selection(
        [("male", "MALE"), ("female", "FEMALE"), ("other", "OTHER")],
    )
    # charactor field #T00339
    reference_no = fields.Char(
        string=" Reference number",
        required=True,
        readonly=True,
        default=lambda self: _("New"),
    )
    teachers_name = fields.Many2one(
        comodel_name="school.teacher",
    )
    email = fields.Char(help="enter your email")
    # date field
    date_of_birth = fields.Date(help="enter your birth date")
    age = fields.Integer(
        compute="_compute_age",
        inverse="_inverse_compute_age",
        search="_search_age",
        readonly=False,
    )
    phone = fields.Char(string="Mobile", help="enter your mobile number")
    permenent_adress = fields.Text(string="Permennt adress", help="perment adress")
    # many2may field for student sport model
    student_sport = fields.Many2one(comodel_name="student.sport", string="Sport")
    student_image = fields.Image(help="student image")
    count_teacher = fields.Integer(compute="_compute_class_teacher", readonly=True)
    # text field
    progress = fields.Integer(default="54")
    school_name = fields.Char(
        string="School", default="SUNSHINE INTERNATIONAL SCHOOL", readonly=True
    )
    school_contact = fields.Char(
        string="Contact", default="(+91) 9510431554", readonly=True
    )
    visit_web = fields.Char(
        string="website",
        default="https://www.icbse.com/schools/sunshine-international-school-gy4k83",
        readonly=True,
    )

    priority = fields.Selection(
        [
            ("poor", "poor"),
            ("good", "good"),
            ("nice", "nice"),
            ("verygood", "verygood"),
            ("exelence", "exelence"),
        ]
    )

    percentage = fields.Float(string="Last year percentage")
    record = fields.Reference([("student.sport", "sports")], string="Reference sport")
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        default=lambda self: self.env.user.company_id.currency_id.id,
    )
    # monetary fields
    student_fees = fields.Monetary(string="Student fees", readonly=True)
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("cancel", "Cancelled"),
            ("done", "Done"),
        ],
        string="Status",
        required=True,
        default="draft",
    )
    student_result = fields.Integer(string="Result", compute="_compute_result")
    admission_date = fields.Date(default=date.today())
    admission_confirm_date = fields.Date(
        compute="_compute_confirm_admission_date",
    )
    student_all_records = fields.One2many(
        comodel_name="students.mark",
        inverse_name="student_enroll",
    )

    @api.depends("date_of_birth")
    def _compute_age(self):
        # """This method is compute a student age #T00368"""
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - (rec.date_of_birth).year
            else:
                rec.age = 1

    @api.depends("age")
    def _inverse_compute_age(self):
        # """This method is compute a student date of birth from age #T00445"""
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

    def _search_age(self, operator, value):
        return [("id", "=", 2)]

    @api.depends("admission_date")
    def _compute_confirm_admission_date(self):
        """compute method for admission confirm date #T00368"""
        cnfm_date = int(
            self.env["ir.config_parameter"].get_param(
                "school_management.admission_confirm_time"
            )
        )
        for rec in self:
            rec.admission_confirm_date = self.admission_date + timedelta(days=cnfm_date)

    events = fields.Text(
        string="events", help="adding your events you have conduct priviously"
    )

    @api.constrains("phone")
    def _validate_phone_number(self):
        """This method is validate a phone number #T00368"""
        if self.phone:
            test_count = 0
            for element in self.phone:
                test_count += 1
                if not element.isdigit():
                    raise ValidationError(
                        _("Only digits are allowed in phone number field")
                    )
            if test_count > 10:
                raise ValidationError(
                    _("More than 10 digits are not allowed in phone number field")
                )
            elif test_count < 10:
                raise ValidationError(
                    _("Enter atleast 10 digits in phone number field")
                )

    # check age is valid
    @api.constrains("age")
    def validate_student_age(self):
        """this method for validate a student if student is below 5
        year so it not register #T00368"""
        minimum_age = int(
            self.env["ir.config_parameter"].get_param(
                "school_management.minimum_student_age"
            )
        )
        if self.date_of_birth:
            if self.age < minimum_age:
                raise ValidationError(
                    _(
                        "Below 5 years student cannot take admission in school "
                        "According Goverment Policy "
                    )
                )

    # model decorators #T00339
    @api.model
    def default_get(self, fields):
        """This is a default_get  orm method for #T00339"""
        default = super(SchoolManagement, self).default_get(fields)
        default["email"] = "abc@gmail.com"
        return default

    # overide @api.model decorators #T00339
    @api.model
    def create(self, vals):
        """This method is create a sequence generator #T00368"""
        if vals.get("reference_no", _("New")) == _("New"):
            vals["reference_no"] = self.env["ir.sequence"].next_by_code(
                "student.name"
            ) or _("New")
            newsequence = super(SchoolManagement, self).create(vals)
            return newsequence

    @api.onchange("std")
    def _onchange_std_(self):
        """this is method for if student select thier
        standard so that time changes on student fees fields #T00368"""
        if self.std == "std1":
            self.student_fees = 5000
        elif self.std == "std2":
            self.student_fees = 10000
        elif self.std == "std3":
            self.student_fees = 30000
        elif self.std == "std4":
            self.student_fees = 40000
        elif self.std == "std5":
            self.student_fees = 50000
        elif self.std == "std6":
            self.student_fees = 60000
        elif self.std == "std7":
            self.student_fees = 70000
        elif self.std == "std8":
            self.student_fees = 80000
        elif self.std == "std9":
            self.student_fees = 90000
        elif self.std == "std10":
            self.student_fees = 95000

    def get_class_teacher(self):
        return {
            "type": "ir.actions.act_window",
            "name": "class teacher",
            "view_mode": "tree",
            "res_model": "school.teacher",
            "domain": [("class_teacher", "=", self.count_teacher)],
            "context": "{'create': False}",
        }

    def _compute_class_teacher(self):
        """This method is compute the class teacher #T00368"""
        for record in self:
            record.count_teacher = self.env["school.teacher"].search_count(
                [("class_teacher", "=", self.count_teacher)]
            )

    # unlink orm method
    def unlink_orm(self):
        """This is a unlink orm method for #T00339"""
        if self.state == "done":
            raise ValidationError(_("you cannot delete record on done state "))
        return super(SchoolManagement, self).unlink()

    # name_get orm method #T00339
    def name_get(self):
        # This method  is use to name get for student #T00368
        student_list = []
        for student in self:
            name = f"{student.name} - [{student.roll}]"
            student_list.append((student.id, name))
        return student_list

    def _compute_teacher_count(self):
        for teacher in self:
            teacher.teacher_count = self.env["school.teacher"].search_count(
                [("student_id", "=", self.name)]
            )

    def compute_student_result_button(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Result",
            "view_mode": "form",
            "res_model": "students.mark",
            "domain": [("average", "=", self.name)],
            "context": "{'create': False}",
        }

    def _compute_result(self):
        """This is a compute method for a #T00339"""
        for record in self:
            record.student_result = self.env["students.mark"].search_count(
                [("student_enroll", "=", self.name)]
            )
