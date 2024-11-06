from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

class Contract(models.Model):
    _inherit = 'contract.contract'

    visa_application_id = fields.Many2one('visa.application', string='Visa Application')
    visa_type_id = fields.Many2one('visa.type', related='visa_application_id.category_id.visa_type_id', 
                                  string='Visa Type', store=True)

    @api.model
    def create_from_application(self, application):
        """Create contract from visa application"""
        contract_template = application.category_id.visa_type_id.contract_template_id
        vals = {
            'name': f'Contract for {application.name}',
            'partner_id': application.partner_id.id,
            'visa_application_id': application.id,
            'contract_template_id': contract_template.id if contract_template else False,
            'date_start': fields.Date.today(),
            'date_end': fields.Date.today() + relativedelta(days=application.category_id.visa_type_id.duration),
        }
        return self.create(vals)