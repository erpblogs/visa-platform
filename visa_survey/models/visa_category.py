from odoo import fields, models, api

class VisaCategory(models.Model):
    _inherit = 'visa.category'

    checklist_survey_id = fields.Many2one('survey.survey', 
        string='Checklist Survey',
        domain=[('is_visa_template', '=', True)],
        help="Survey template to use as checklist for this visa category")
    checklist_required = fields.Boolean(string='Checklist Required',
        help="Make checklist mandatory before submission")
    min_score_required = fields.Float(string='Minimum Score Required (%)',
        help="Minimum score required to pass the checklist")

    @api.onchange('checklist_survey_id')
    def _onchange_checklist_survey(self):
        if self.checklist_survey_id:
            self.checklist_required = True 