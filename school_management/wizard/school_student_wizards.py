from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


# school_management/school_student_wizards.py #T00360
class StudentWizard(models.TransientModel):
    _name = "student.wizard"
    _description = "student Wizard"
    _rec_name = "name"

    name = fields.Char(required=True)

    roll = fields.Integer(string="Roll Number", required=True)

    dob = fields.Date(string="Date Of Birth ")

    age = fields.Integer(compute="_compute_age")

    @api.depends("dob")
    def _compute_age(self):
        """this is a compute method for a compute a age #T00360"""
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(), rec.dob).years

    def action_done(self):
        """this is method for create a new record in student.name object #T00360"""
        self.env["student.name"].create(
            {"name": self.name, "roll": self.roll, "dob": self.dob, "age": self.age}
        )


class SportWizard(models.TransientModel):
    _name = "sport.wizard"
    _description = "sport wizard for student"

    name = fields.Many2one(comodel_name="student.sport")

    phone = fields.Char(string="phone")

    Email = fields.Char()

    sports_roll = fields.Integer(string="roll number")

    def action_done_sport(self):
        """this is method for create a new record in student.name object #T00360"""
        self.env["student.sport"].create(
            {"name": self.name, "phone": self.phone, "email": self.Email}
        )
