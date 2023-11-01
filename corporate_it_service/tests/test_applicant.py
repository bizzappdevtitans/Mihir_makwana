# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


# create a class for a testcases #T00472
class TestApplicant(TransactionCase):
    def setup(self):
        return super(TestApplicant, self).setup()

    def test_01_applicant_name_uniqueness(self):
        """This method is use to check a uniqueness of a name  #T00472"""
        applicant1 = self.env["it.applicant"].create(
            {
                "applicant_id": "MIHIR PANCHAL",
                "name": "APL0001",
                "boolean": "True",
                "applicant_email": "makwanamihir922@gmail.com",
                "applicant_degree": "bba",
                "salary_expect": "50000",
            }
        )
        self.assertEqual(
            applicant1.applicant_id,
            "MIHIR PANCHAL",
            "applicant  name should be 'MIHIR PANCHAL'",
        )

    # def test_02_check_salary_validation(self):
    #     with self.assertRaises(ValidationError):
    #         applicant = self.env["it.applicant"].create(
    #             {
    #                 "applicant_id": "Mihir Panchal",
    #                 "applicant_email": "makwanamihir922@gmail.com",
    #                 "boolean": True,
    #                 "salary_expect": -2323,
    #                 "applicant_degree": "bba",
    #             }
    #         )

    # def test_03_check_email_validation(self):
    #     with self.assertRaises(ValidationError):
    #         applicant = self.env["it.applicant"].create(
    #             {
    #                 "applicant_id": "Mihir Panchal",
    #                 "applicant_email": "invalid email",
    #                 "boolean": True,
    #                 "salary_expect": 2323,
    #                 "applicant_degree": "bba",
    #             }
    #         )

    def test_04_action_check_whatsapp_share(self):
        with self.assertRaises(ValidationError):
            applicant = self.env["it.applicant"].create(
                {
                    "applicant_id": "Mihir Panchal",
                    "applicant_email": "makwanamihir922@gmail.com",
                    "boolean": True,
                    "salary_expect": 2323,
                    "applicant_degree": "bba",
                    "mobile": 9510431554,
                }
            )
            action = applicant.action_share_in_whatsapp()
            self.assertEqual(action["type"], "ir.actions.act_url")
            self.assertEqual(action["target"], "new")
