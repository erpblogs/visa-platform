{
    'name': 'Visa Service Management',
    'version': '1.0',
    'summary': 'Manage visa services and pricing',
    'description': """
        Manage visa services, requirements, and pricing.
        Integration with sales for service management.
    """,
    'category': 'Services/Visa',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': [
        'base',
        'sale_management',
        'product',
        'visa_management',
    ],
    'data': [
        'security/service_security.xml',
        'security/ir.model.access.csv',
        'views/visa_service_views.xml',
        'views/visa_service_requirement_views.xml',
        'views/visa_service_process_views.xml',
        'views/menu_views.xml',
        'data/visa_service_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
} 