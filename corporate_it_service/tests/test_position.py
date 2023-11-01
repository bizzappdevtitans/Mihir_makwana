# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


# create a class for a testcases #T00472
class TestApplicantPosition(TransactionCase):
    def setup(self):
        return super(TestApplicantPosition, self).setup()
        # self.TestApplicantPosition = self.env["job.position"]

    def test_01_create_job_position(self):
        position = self.env["job.position"].create(
            {
                "name": "Sales Manager",
                "description": "This position for a Sales Manager",
                "company_id": False,
                "department_id": False,
                "recruiter_id": False,
                "recruitment": 12,
                "date_of_open": "2023-12-01",
                "date_of_closing": "2023-12-01",
                "salary_proposed": 12000000,
            }
        )
        self.assertEqual(
            position.name,
            "Sales Manager",
            "position name should be 'Sales Manager'",
        )

    # def test_02_check_invalid_salary_proposed(self):
    #     with self.assertRaises(ValidationError):
    #         salary = self.env["job.position"].create(
    #             {
    #                 "name": "Sales Manager",
    #                 "description": "This position for a Sales Manager",
    #                 "company_id": False,
    #                 "department_id": False,
    #                 "recruiter_id": False,
    #                 "recruitment": 12,
    #                 "date_of_open": "2023-12-01",
    #                 "date_of_closing": "2023-12-01",
    #                 "salary_proposed": -12000000,
    #             }
    #         )

    def test_03_check_invalid_recruitment_proposed(self):
        with self.assertRaises(ValidationError):
            salary = self.env["job.position"].create(
                {
                    "name": "Sales Manager",
                    "description": "This position for a Sales Manager",
                    "company_id": False,
                    "department_id": False,
                    "recruiter_id": False,
                    "recruitment": 0,
                    "date_of_open": "2023-12-01",
                    "date_of_closing": "2023-12-01",
                    "salary_proposed": -12000000,
                }
            )
            self.assertEqual(
                salary.recruitment, "0", "salary recruitment should not --0--"
            )

    # def test_04_check_dates_validation(self):
    #     with self.assertRaises(ValidationError):
    #         dates = self.env["job.position"].create(
    #             {
    #                 "name": "Sales Manager",
    #                 "description": "This position for a Sales Manager",
    #                 "company_id": False,
    #                 "department_id": False,
    #                 "recruiter_id": False,
    #                 "recruitment": 21,
    #                 "date_of_open": "2023-12-01",
    #                 "date_of_closing": "2023-11-01",
    #                 "salary_proposed": 12000000,
    #             }
    #         )

    def test_05_check_default_values(self):
        position = self.env["job.position"].create(
            {
                "name": "Sales Manager",
                "recruitment": 1,
                "date_of_open": "2023-12-01",
                "date_of_closing": "2023-12-01",
            }
        )
        self.assertFalse(position.company_id, "compony id should be a False")
        self.assertFalse(position.department_id, "department id should be a False")
        self.assertFalse(position.recruiter_id, "recruiter should be a False")
