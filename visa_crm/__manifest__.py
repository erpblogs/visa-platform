{
    'name': 'Visa CRM Integration',
    'version': '1.0',
    'category': 'Services/Visa',
    'summary': 'Integrate Visa Management with CRM',
    'description': """
        Link leads and opportunities with visa applications.
        Create visa applications directly from leads.
    """,
    'depends': ['visa_management', 'crm'],
    'data': [
        'views/crm_lead_views.xml',
        'views/visa_application_views.xml',
    ],
    'installable': True,
    'auto_install': False,
} 