from odoo import fields, models

# This model create a purpose of save a configuration settings of the module


class SchoolStudentConfigSetings(models.TransientModel):
    """inherit res.config.setting #T00368"""

    _inherit = "res.config.settings"

    minimum_student_age = fields.Integer(
        default=5,
        config_parameter="school_management.minimum_student_age",
    )
    maximum_teacher_age = fields.Integer(
        default=60,
        config_parameter="school_management.maximum_teacher_age",
    )
    admission_confirm_time = fields.Integer(
        string="Number of days to admission confirm",
        config_parameter="school_management.admission_confirm_time",
    )
