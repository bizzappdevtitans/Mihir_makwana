# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models


# create a class for a cron job #T00443
class CronJobSentEmail(models.Model):
    _name = "cron.job.sent.email"
    _description = "Cron Job to Sent Email"

    # @api.model
    # def sent_email(self, context=None):
    #     self.env["it.applicant"]
    #     return action_send_email
