from odoo import fields, models


class ExamRelated(models.Model):
    _name = "exam.related"
    _description = "exam.related"

    first_exam = fields.Char(string=" First Exam name")
    second_exam = fields.Char(string=" Second Exam name")
    first_exam_date = fields.Date(string=" First Exam Date")
    second_exam_date = fields.Date(string=" Second Exam Date")
