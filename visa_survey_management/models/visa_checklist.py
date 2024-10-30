from odoo import api, fields, models

class VisaChecklistDocument(models.Model):
    _name = 'visa.checklist.document'
    _description = 'Visa Checklist Document'
    _order = 'sequence, id'

    name = fields.Char(string='Document Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    survey_id = fields.Many2one('survey.survey', string='Checklist', required=True)
    is_mandatory = fields.Boolean(string='Mandatory', default=True)
    document_type = fields.Selection([
        ('identity', 'Identity Document'),
        ('financial', 'Financial Document'),
        ('educational', 'Educational Document'),
        ('professional', 'Professional Document'),
        ('other', 'Other')
    ], string='Document Type', required=True)
    notes = fields.Text(string='Notes') 