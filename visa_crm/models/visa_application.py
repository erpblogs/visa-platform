from odoo import fields, models, api

class VisaApplication(models.Model):
    _inherit = 'visa.application'

    lead_id = fields.Many2one('crm.lead', string='Lead')
    opportunity_id = fields.Many2one('crm.lead', string='Opportunity', 
        domain=[('type', '=', 'opportunity')])

    @api.model
    def create_from_lead(self, lead):
        return self.create({
            'partner_id': lead.partner_id.id,
            'lead_id': lead.id,
            'category_id': lead.visa_category_id.id,
            'notes': lead.description,
        }) 