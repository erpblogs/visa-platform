from odoo import fields, models

class VisaServiceRequirement(models.Model):
    _name = 'visa.service.requirement'
    _description = 'Visa Service Requirement'
    _order = 'sequence, id'

    name = fields.Char('Requirement Name', required=True)
    product_tmpl_id = fields.Many2one(
        'product.template', 
        string='Visa Service',
        required=True,
        domain=[('is_visa_service', '=', True)]
    )
    sequence = fields.Integer('Sequence', default=10)
    requirement_type = fields.Selection([
        ('document', 'Document'),
        ('information', 'Information'),
        ('payment', 'Payment'),
        ('other', 'Other')
    ], string='Requirement Type', required=True)
    is_mandatory = fields.Boolean('Mandatory', default=True)
    description = fields.Text('Description')
    note = fields.Text('Internal Note') 