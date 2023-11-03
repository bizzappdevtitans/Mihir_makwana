# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class ApplicantWizard(models.TransientModel):
    _name = "applicant.wizard"
    _description = "cancle application"

    # fields for a wizard #T00472
    name = fields.Char(
        string="Applicant Id",
        copy=False,
        readonly=True,
    )
    is_active = fields.Boolean(string="Active", default=True, required=True)
    applicant_id = fields.Char(
        string="Applicant Name",
    )
    applicant_email = fields.Char(
        string="Email", help="Applicant Email", required=True, store="True"
    )

    def action_cancle_record(self):
        """This method is delete a record #T00472"""
        for record in self:
            applicant = self.env["it.applicant"]

            delete_record = applicant.search(
                [("applicant_email", "=", record.applicant_email)]
            )
            delete_record.unlink()


class PositionCreateWizard(models.TransientModel):
    _name = "position.wizard"
    _description = "position wizard"

    name = fields.Char(string="Position Name", required=True, default="Sales Manager")
    description_of_position = fields.Text("Description")

    def action_confirm(self):
        """This method is a create a new record #T00472"""
        self.env["job.position"].create(
            {
                "name": self.name,
                "description": self.description_of_position,
            }
        )
