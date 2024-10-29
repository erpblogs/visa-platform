{
    'name': 'Visa Management',
    'version': '1.0',
    'summary': 'Manage visa applications and processes',
    'description': """
        Visa Management System for managing visa applications, 
        processing, and tracking.
    """,
    'category': 'Services/Visa',
    'author': 'Quang Trinh',
    'website': 'https://www.erpblogs.com',
    'depends': [
        'base',
        'mail',
        'survey',
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
        'views/visa_survey_views.xml',
        'views/visa_type_views.xml',
        'views/visa_menu.xml',
        'views/visa_menu_survey.xml',
        'views/visa_menu_partner.xml',
        # 'reports/visa_reports.xml',
        # 'reports/visa_report_templates.xml',
    ],
    'demo': [
        # 'demo/visa_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'visa_management/static/src/scss/visa_styles.scss',
            # 'visa_management/static/src/js/visa_widgets.js',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 1,
} 