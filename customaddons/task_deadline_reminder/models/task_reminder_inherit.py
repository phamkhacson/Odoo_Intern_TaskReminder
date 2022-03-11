from odoo import api, fields, models
from odoo.fields import Datetime


class TaskReminder(models.Model):
    _inherit = 'project.task'

    task_reminder = fields.Boolean(string="Task Reminder", default=False)

    def send_cron_mail(self):
        for task in self.env['project.task'].search(
                [('date_deadline', '!=', None), ('task_reminder', '=', True), ('user_ids', '!=', None)]):
            reminder_date = task.date_deadline
            today = Datetime.now().date()
            if today == reminder_date and task:
                template_id = self.env.ref('task_deadline_reminder.mail_template_task_reminder').id
                if template_id:
                    email_template_obj = self.env['mail.template'].browse(template_id)
                    values = email_template_obj.generate_email(task.id,
                                                               ['subject', 'body_html', 'email_from', 'email_to',
                                                                'partner_to', 'email_cc', 'reply_to', 'scheduled_date'])
                    msg_id = self.env['mail.mail'].create(values)
                if msg_id:
                    msg_id.send()
        return True

    def get_user_email(self):
        self.ensure_one()
        return ",".join([e for e in self.user_ids.mapped("email") if e])

    def get_user_name(self):
        self.ensure_one()
        return ",".join([e for e in self.user_ids.mapped("name") if e])
