# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests.common import TransactionCase


# create a class for a testcases #T00472
class TestApplicantPosition(TransactionCase):
    def setup(self):
        return super(TestApplicantPosition, self).setup()

        # def test_01_create_job_position(self):
        #     position = self.env["job.position"].create(
        #         {
        #             "name": "Sales Manager",
        #             "description": "This position for a Sales Manager",
        #             "company_id": False,
        #             "department_id": False,
        #             "recruiter_id": False,
        #             "recruitment": 12,
        #             "date_of_open": date.today(),
        #             "date_of_closing": date.today(),
        #             "salary_proposed": "12000000",
        #         }
        #     )
        #     self.assertEqual(
        #         position.name,
        #         "Sales Manager",
        #         "position name should be 'Sales Manager'",
        #     )
