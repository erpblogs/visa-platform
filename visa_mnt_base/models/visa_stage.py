from odoo import fields, models

class VisaStage(models.Model):
    _name = 'visa.stage'
    _description = 'Visa Application Stage'
    _order = 'sequence, id'

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    fold = fields.Boolean(string='Folded in Kanban')
    is_closed = fields.Boolean(string='Closed Stage')
    description = fields.Text(string='Description')
    # application_ids = fields.One2many('visa.application', 'stage_id', string='Applications')