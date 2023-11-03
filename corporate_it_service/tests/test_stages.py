# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests.common import TransactionCase


# create a class for a testcases #T00472
class TestApplicantStages(TransactionCase):
    def setup(self):
        return super(TestApplicantStages, self).setup()
        # self.ApplicantStages = self.env["applicant.stages"]

    def test_01_check_create_applicant_stages(self):
        """This method is check a applicant stages#T00472"""

        stage = self.env["applicant.stages"].create(
            {
                "name": "Recived",
                "sequence": 10,
                "requirement": "Review application",
                "template_id": False,
                "blocked": "In Progress",
                "done": "Blocked",
                "normal": "Ready for Next Stage",
            }
        )
        self.assertEqual(stage.name, "Recived", "stage name should be a  --Recived--")
        self.assertEqual(stage.sequence, 10, "stage sequence should be a  --10--")
        self.assertEqual(
            stage.requirement,
            "Review application",
            "stage requirement should be a  --Review application--",
        )
        self.assertEqual(
            stage.blocked, "In Progress", "stage blocked should be a  --In Progress--"
        )
        self.assertEqual(stage.done, "Blocked", "stage done should be a  --Blocked--")
        self.assertEqual(
            stage.normal,
            "Ready for Next Stage",
            "stage normal should be a  --Ready for Next Stage--",
        )

    def test_02_check_sequence_for_stages(self):
        """This method is check sequence for stages #T00472"""

        stage1 = self.env["applicant.stages"].create(
            {"name": "Application Recived", "sequence": 10}
        )
        stage2 = self.env["applicant.stages"].create(
            {"name": "Interview Scheduled", "sequence": 20}
        )
        self.assertTrue(
            stage1.sequence < stage2.sequence,
            "stage1 should have lower sequence number  than stage2",
        )
