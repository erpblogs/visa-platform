{
    'name': 'Visa Survey Integration',
    'version': '1.0',
    'category': 'Services/Visa',
    'summary': 'Integrate Visa Management with Surveys',
    'description': """
        Use surveys as checklists for visa applications.
        Track checklist completion status.
    """,
    'depends': ['visa_management', 'survey'],
    'data': [
        'views/survey_views.xml',
        'views/visa_application_views.xml',
        'views/visa_category_views.xml',
    ],
    'installable': True,
    'auto_install': False,
} 