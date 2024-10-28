{
    'name': 'Survey User Portal Access',
    'version': '1.0',
    'category': 'Survey',
    'summary': 'Allow portal users to access their own surveys',
    'description': """
        This module extends the functionality of the survey module to allow portal users to access their own surveys.
    """,
    'depends': ['survey', 'portal'],
    'data': [
        'views/survey_portal_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
