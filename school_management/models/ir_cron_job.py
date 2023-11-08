# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, models


# create a class for a cron job #T00443
class CronJobSchoolManagement(models.Model):
    _name = "cron.job.school.management"
    _description = "cron job for student cancle record delete "

    # method for a cron job #T00443
    @api.model
    def cronjobtest(self, context=None):
        """method for a cron job to call after every 1 weeks #T00243"""
        customer = self.env["student.name"].search([("state", "=", "cancel")]).unlink()
        return customer
