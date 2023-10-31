# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests.common import TransactionCase


# create a class for a testcases #T00472
class TestApplicantStages(TransactionCase):
    def setup(self):
        return super(TestApplicantStages, self).setup()

    def test_01_check_create_applicant_stages(self):
        stage = self.env["applicant.stages"].create(
            {
                "name": "Recived",
                # "sequence": self.sequence,
                "requirement": " Review application",
                "template_id": False,
                "blocked": "In Progress",
                "done": "Blocked",
                "normal": "Ready for Next Stage",
            }
        )
        self.assertEqual(stage.name, "Recived", "stage name should be a  --Recived--")
        # self.assertEqual(
        #     stage.sequence, self.sequence, "stage sequence should be a  --10--"
        # )
        # self.assertEqual(
        #     stage.requirement,
        #     "Review application",
        #     "stage requirement should be a  --Review application--",
        # )
        self.assertEqual(
            stage.blocked, "In Progress", "stage blocked should be a  --In Progress--"
        )
        self.assertEqual(stage.done, "Blocked", "stage done should be a  --Blocked--")
        self.assertEqual(
            stage.normal,
            "Ready for Next Stage",
            "stage normal should be a  --Ready for Next Stage--",
        )
