from odoo import fields, models

class VisaServiceProcess(models.Model):
    _name = 'visa.service.process'
    _description = 'Visa Service Process'
    _order = 'sequence, id'

    name = fields.Char('Step Name', required=True)
    product_tmpl_id = fields.Many2one(
        'product.template', 
        string='Visa Service',
        required=True,
        domain=[('is_visa_service', '=', True)]
    )
    sequence = fields.Integer('Sequence', default=10)
    duration = fields.Integer('Duration (days)', default=1)
    responsible_type = fields.Selection([
        ('vendor', 'Vendor'),
        ('applicant', 'Applicant'),
        ('both', 'Both')
    ], string='Responsible', required=True)
    description = fields.Text('Description')
    required_documents = fields.Many2many(
        'visa.service.requirement',
        string='Required Documents'
    ) 