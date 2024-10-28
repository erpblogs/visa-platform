# __manifest__.py
{
    'name': 'Visa Management Base',
    'version': '1.0',
    'summary': 'Manage visa applications and related processes',
    'description': """
    This module extends Odoo's functionality to manage visa applications,
    including visa categories, application stages, checklists using surveys, and invoicing.
    """,
    'category': 'Services',
    'author': 'NextG ERP',
    'website': 'https://www.nextgerp.com',
    'depends': ['base', 'crm', 'contacts', 'survey', 'account'],
    'data': [
        'security/visa_security.xml',
        'security/ir.model.access.csv',
        'data/visa_sequence.xml',
        'data/visa_checklist_survey_demo.xml',
        'data/visa_management_demo.xml',
        'views/visa_application_views.xml',
        'views/visa_category_views.xml',
        'views/visa_stage_views.xml',
        # 'views/res_partner_views.xml',
        'views/survey_survey_views.xml',
        'views/res_partner_views.xml',
        # 'reports/visa_affidavit_report.xml',
        # 'reports/visa_receipt_report.xml',
        'views/menu.xml',  # Add this line
        'views/menu_visa_survey.xml',
        'views/menu_visa_partner.xml',
    ],
    'demo': [
        # 'demo/visa_checklist_survey_demo.xml',
        # 'demo/visa_management_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}