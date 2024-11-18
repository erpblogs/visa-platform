from odoo import models, fields

class ContractTemplateVariable(models.Model):
    _name = 'contract.template.variable'
    _description = 'Contract Template Variable'

    name = fields.Char(string='Variable Name', required=True)
    key = fields.Char(string='Variable Key', required=True)
    description = fields.Text(string='Description')
    template_id = fields.Many2one('contract.template', string='Template') 