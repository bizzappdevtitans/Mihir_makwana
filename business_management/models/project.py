from odoo import fields, models


# inherit project.project object # T00412
class Project(models.Model):
    _inherit = "project.project"

    # create a field for a project  #T000412
    _project_description = fields.Char(string="Project Description")
