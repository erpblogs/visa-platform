from odoo import fields, models, api

class Lead(models.Model):
    _inherit = 'crm.lead'

    visa_category_id = fields.Many2one('visa.category', string='Visa Category')
    visa_application_id = fields.Many2one('visa.application', string='Visa Application')

    def action_create_visa_application(self):
        self.ensure_one()
        if not self.visa_application_id:
            application = self.env['visa.application'].create_from_lead(self)
            self.visa_application_id = application.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'visa.application',
            'res_id': self.visa_application_id.id,
            'view_mode': 'form',
            'target': 'current',
        }