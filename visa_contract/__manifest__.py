{
    'name': 'Visa Contract Integration',
    'version': '1.0',
    'category': 'Services/Visa',
    'summary': 'Integrate Visa Management with Contracts',
    'description': """
        Link visa applications with contracts.
        Create contracts automatically from visa applications.
    """,
    'depends': [
        'visa_management',
        'contract',
    ],
    'data': [
        'views/contract_views.xml',
        'views/visa_type_views.xml',
    ],
    'installable': True,
    'auto_install': False,
} 