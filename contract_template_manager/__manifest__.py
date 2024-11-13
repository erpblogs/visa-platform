{
    'name': 'Contract Template Manager',
    'version': '17.0.1.0.0',
    'category': 'Sales/Contracts',
    'summary': 'Enhanced Contract Templates with Report Management',
    'description': """
        Extends contract templates with:
        * Report template selection
        * Report template management
        * Template preview functionality
    """,
    'depends': ['contract'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/contract_template_views.xml',
        'views/report_contract_template.xml',
        'report/custom_report.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
} 