from odoo import api, fields, models


# school_management/student_sport.py #T00339
class StudentSport(models.Model):
    _name = "student.sport"
    _description = "students sports"
    _rec_name = "name"

    # student sport attributes fields #T00339
    name = fields.Char(required=True)
    sports_roll = fields.Integer("Roll number")
    sport = fields.Selection(
        [
            ("kabbdi", "KABBADI"),
            ("cricket", "CRICKET"),
            ("table tannies", "TABLE TANNIES"),
            ("box cricket", "BOX CRICKET"),
        ],
        string="Sports",
    )
    phone = fields.Char("Mobile")
    sport_std = fields.Selection(
        [
            ("std1", "STD-1"),
            ("std2", "STD-2"),
            ("std3", "STD-3"),
            ("std4", "STD-4"),
            ("std5", "STD-5"),
            ("std6", "STD-6"),
            ("std7", "STD-7"),
            ("std8", "STD-8"),
            ("std9", "STD-9"),
            ("std10", "STD-10"),
        ],
        string="standard",
    )
    # image field #T00339
    achivement_photo = fields.Image(string="Attech your photo with medal ")
    email = fields.Char()
    some_url = fields.Char(string="url")
    # many2many field
    student_ids = fields.Many2many(comodel_name="student.name", string="students")
    progress = fields.Integer(default=69)

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("cancel", "Cancelled"),
            ("done", "Done"),
        ],
        string="Status",
        required=True,
        readonly=True,
        copy=False,
        default="draft",
    )

    # name_get orm method #T00339
    def name_get(self):
        """This method is name get to student #T00339"""
        namegate = []
        for name in self:
            name = f"{name.name} - {name.sports_roll}"
            namegate.append((name, name))
        return namegate

    # name_search orm method #T00339
    @api.model
    def _name_search(
        self, name="", args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        args = args or []
        # we create a empty list
        domain = []
        if name:
            domain = [
                "|",
                "|",
                ("name", operator, name),
                ("phone", operator, name),
                ("email", operator, name),
            ]
        # we search with help of _search orm method #T00339
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
