from odoo import fields, models

class VisaType(models.Model):
    _inherit = 'visa.type'

    contract_template_id = fields.Many2one('contract.template', 
        string='Contract Template',
        help="Contract template to use when creating contracts for this visa type") 