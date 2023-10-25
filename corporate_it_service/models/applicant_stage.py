from odoo import _, fields, models


class ApplicantStages(models.Model):
    _name = "applicant.stages"
    _description = "Stages Of Applicant"

    name = fields.Char(string="Stage Name")
    sequence = fields.Integer(string="Secuence", default="10")
    requirement = fields.Text(string="Recruitment")
    template_id = fields.Many2one(comodel_name="mail.template", string="Email Template")
    legend_blocked = fields.Char(
        "Red Kanban Label",
        default=lambda self: _("Blocked"),
        translate=True,
        required=True,
    )
    legend_done = fields.Char(
        "Green Kanban Label",
        default=lambda self: _("Ready for Next Stage"),
        translate=True,
        required=True,
    )
    legend_normal = fields.Char(
        "Grey Kanban Label",
        default=lambda self: _("In Progress"),
        translate=True,
        required=True,
    )
