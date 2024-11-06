{
    'name': 'Visa Management',
    'version': '1.0',
    'summary': 'Manage visa applications and processes',
    'description': """
        Core Visa Management System for managing visa applications, 
        processing, and tracking.
    """,
    'category': 'Services/Visa',
    'author': 'Quang Trinh',
    'website': 'https://www.erpblogs.com',
    'depends': [
        'base',
        'mail',
        'account',
    ],
    'data': [
        'security/visa_security.xml',
        'security/ir.model.access.csv',
        'data/visa_sequence.xml',
        'views/visa_application_views.xml',
        'views/visa_category_views.xml',
        'views/visa_stage_views.xml',
        'views/visa_partner_views.xml',
        'views/visa_type_views.xml',
        'views/visa_menu.xml',
    ],
    'demo': [
        'demo/visa_demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 1,
} 