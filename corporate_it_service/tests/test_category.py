# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests.common import TransactionCase


# create a class for a testcases #T00472
class TestCategory(TransactionCase):
    def setup(self):
        return super(TestCategory, self).setup()

    def test_01_create_applicant_category(self):
        category = self.env["applicant.category"].create({"name": "engineering"})
        self.assertEqual(
            category.name, "engineering", "Category name should be 'engineering'"
        )

    # def test_02_check_duplicate_name(self):
    #     category1 = self.env["applicant.category"].create({"name": "engineering"})
    #     with self.assertRaises(Exception):
    #         category2 = self.env["applicant.category"].create({"name": "engineering"})

    def test_03_check_default_color(self):
        category = self.env["applicant.category"].create({"name": "sales"})

        self.assertTrue(1 <= int(category.color_of_tag) <= 20)
