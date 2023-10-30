from odoo import fields, models


# inherit project.task object # T00412
class ProjectTask(models.Model):
    _inherit = "project.task"

    # create a field for a project  #T000412
    _task_description = fields.Char(string="Task Description")
