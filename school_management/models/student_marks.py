from odoo import api, fields, models


# school_management/student_marks.py #T00339
class StduentMark(models.Model):
    _name = "students.mark"
    _description = "students marks"
    _rec_name = "student_enroll"

    # student marks attributes fields #T00339
    student_enroll = fields.Many2one(
        comodel_name="student.name", string="Enrollment Number", required=True
    )
    std = fields.Selection(
        [
            ("std-1", "STD-1"),
            ("std-2", "STD-2"),
            ("std-3", "STD-3"),
            ("std-4", "STD-4"),
            ("std-5", "STD-5"),
            ("std-6", "STD-6"),
            ("std-7", "STD-7"),
            ("std-8", "STD-8"),
            ("std-9", "STD-9"),
            ("std-10", "STD-10"),
        ],
        string="Standard",
        required=True,
    )
    exam_1 = fields.Float(string="Exam mark 1", required=True)
    exam_2 = fields.Float(string="Exam mark 2", required=True)
    extra = fields.Float(string="Discipline & Presence", required=True)
    average = fields.Float(
        string="Average Mark", compute="_compute_get_avg_mark", store=True
    )

    @api.depends("exam_1", "exam_2", "extra")
    def _compute_get_avg_mark(self):
        """This is a method for find the average marks of the student #T00339"""
        if self.exam_1 and self.exam_2 and self.extra:
            self.average = (self.exam_1 + self.exam_2 + self.extra) / 3
