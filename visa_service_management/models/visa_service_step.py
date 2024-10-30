from odoo import fields, models, api

class VisaServiceStep(models.Model):
    _name = 'visa.service.step'
    _description = 'Visa Service Process Step'
    _order = 'sequence, id'

    name = fields.Char('Step Name', required=True)
    sequence = fields.Integer('Sequence', default=10)
    product_tmpl_id = fields.Many2one(
        'product.template', 
        string='Visa Service',
        required=True,
        domain=[('type', '=', 'service')]
    )
    duration = fields.Integer(
        'Duration (days)', 
        default=1,
        help='Expected duration for this step'
    )
    responsible_type = fields.Selection([
        ('vendor', 'Immigration Agency'),
        ('applicant', 'Applicant'),
        ('both', 'Both')
    ], string='Responsible', required=True)
    description = fields.Text('Description')
    required_documents = fields.Many2many(
        'visa.service.requirement',
        string='Required Documents'
    )
    is_milestone = fields.Boolean(
        'Is Milestone', 
        help='Mark if this step is a major milestone in the process'
    ) 