# Part of Odoo. See LICENSE file for full copyright and licensing details.
# from odoo.exceptions import ValidationError
# from odoo.tests.common import TransactionCase


# # create a class for a testcases #T00472
# class TestApplicant(TransactionCase):
#     def setup(self):
#         return super(TestApplicant, self).setup()

#     def test_01_applicant_name_uniqueness(self):
#         """This method is use to check a uniqueness of a name  #T00472"""
#         applicant1 = self.env["it.applicant"].create(
#             {
#                 "applicant_id": "MIHIR PANCHAL",
#                 "name": "APL0001",
#                 "boolean": "True",
#                 "applicant_email": "makwanamihir922@gmail.com",
#                 "applicant_degree": "bba",
#                 "salary_expect": "50000",
#             }
#         )
#         with self.assertRaises(ValidationError):
#             applicant2 = self.env["it.applicant"].create(
#                 {
#                     "applicant_id": "MIHIR PANCHAL",
#                     "name": "APL0001",
#                     "boolean": "True",
#                     "applicant_email": "makwanamihir922@gmail.com",
#                     "applicant_degree": "bba",
#                     "salary_expect": "50000",
#                 }
#             )
