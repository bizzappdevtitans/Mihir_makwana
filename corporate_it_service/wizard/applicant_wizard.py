# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class ApplicantWizard(models.TransientModel):
    _name = "applicant.wizard"
    _description = "cancle application"

    name = fields.Char(
        string="Applicant Id",
        copy=False,
        readonly=True,
    )
    boolean = fields.Boolean(string="Active", default=True, required=True)
    applicant_id = fields.Char(
        string="Applicant Name",
    )
    applicant_email = fields.Char(
        string="Email", help="Applicant Email", required=True, store="True"
    )

    def action_done(self):
        pass


class PositionCreateWizard(models.TransientModel):
    _name = "position.wizard"
    _description = "position wizard"

    name = fields.Char(string="Position Name")
    description_of_position = fields.Text("Description")

    def action_confirm(self):
        self.env["job.position"].create(
            {
                "name": self.name,
                "description": self.description_of_position,
            }
        )
