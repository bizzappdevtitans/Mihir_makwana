# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests.common import TransactionCase


# create a class for a testcases #T00472
class TestCategory(TransactionCase):
    def setup(self):
        return super(TestCategory, self).setup()
        #  self.ApplicantCategory = self.env["applicant.category"]

    def test_01_create_applicant_category(self):
        """This method is a check a category #T00472"""
        category = self.env["applicant.category"].create({"name": "engineering"})
        self.assertEqual(
            category.name, "engineering", "Category name should be 'engineering'"
        )

    def test_02_check_default_color(self):
        """This method is a check a tag name is generate a number between 1 to 20 #T00472"""

        category = self.env["applicant.category"].create({"name": "sales"})

        self.assertTrue(1 <= int(category.color_of_tag) <= 20)
