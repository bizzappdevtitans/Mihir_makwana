from random import randint

from odoo import fields, models


class ApplicantCategory(models.Model):
    _name = "applicant.category"
    _description = " Category of Applicant"

    def _get_default_color(self):
        return randint(1, 20)

    name = fields.Char(string="Tag Name", required=True)
    color_of_tag = fields.Char(string="Color Number", default=_get_default_color)
