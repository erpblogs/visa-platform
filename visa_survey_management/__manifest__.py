{
    'name': 'Visa Survey Management',
    'version': '1.0',
    'summary': 'Manage visa application checklists using surveys',
    'description': """
        This module extends the survey functionality to manage visa application checklists.
        It provides templates and tools for creating and managing visa application requirements.
    """,
    'category': 'Services/Visa',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': [
        'survey',
        'visa_management',
    ],
    'data': [
        'security/survey_security.xml',
        'security/ir.model.access.csv',
        'views/survey_views.xml',
        'views/visa_checklist_views.xml',
        'views/menu_views.xml',
        'data/survey_template_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
} 