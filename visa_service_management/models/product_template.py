from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    service_requirement_ids = fields.One2many(
        'visa.service.requirement', 
        'product_tmpl_id', 
        string='Service Requirements'
    )
    service_process_ids = fields.One2many(
        'visa.service.process', 
        'product_tmpl_id', 
        string='Service Process Steps'
    )
    estimated_duration = fields.Integer(
        'Estimated Duration (days)',
        help='Estimated processing time in days'
    )
    validity_period = fields.Integer(
        'Validity Period (months)',
        help='Validity period of the visa in months'
    )
    entry_type = fields.Selection([
        ('single', 'Single Entry'),
        ('multiple', 'Multiple Entry')
    ], string='Entry Type')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('is_visa_service'):
                vals['type'] = 'service'
        return super().create(vals_list) 