from odoo import fields, models


class QuestionRelated(models.Model):
    _name = "question.related"
    _description = "question.related"

    question_type = fields.Selection(
        [("theory", "THEORY"), ("practical", "PRACTICAL")], string=" Type Of Question"
    )
    no_of_question_in_paper = fields.Integer(string="Question")
