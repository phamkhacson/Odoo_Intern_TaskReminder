{
    'name': "Task Deadline Reminder",
    'version': "14.0.1.0.0",
    'author': 'Son@manifest',
    'company': 'Manifest JSC',
    'website': '',
    'summary': '''Automatically Send Mail To Responsible User if Deadline Of Task is Today''',
    'description': '''Automatically Send Mail To Responsible User if Deadline Of Task is Today''',
    'category': "Project",
    'depends': ['project'],
    'license': 'AGPL-3',
    'data': [
        'data/mail_reminder_template.xml',
        'views/task_reminder_cron.xml',
        'views/task_view_inherit.xml'
             ],
    'images': [],
    'installable': True,
    'auto_install': False
}