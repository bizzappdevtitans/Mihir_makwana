# Part of Odoo. See LICENSE file for full copyright and licensing details.


from random import randint

from odoo import api, fields, models


# create a class for a applicant category #T00472
class ApplicantCategory(models.Model):
    _name = "applicant.category"
    _description = " Category of Applicant"

    def _get_default_color(self):
        """This method is use to choose a random color  #T00472"""
        return randint(1, 20)

    @api.depends("name")
    def validate_name(self, name):
        for char in name:
            if not (
                ("A" <= char and char <= "Z")
                or ("a" <= char and char <= "z")
                or (char == " ")
            ):
                return False

        return True

    # field for a applicant category #T00472
    name = fields.Char(string="Tag Name", required=True)
    color_of_tag = fields.Char(string="Color Number", default=_get_default_color)
