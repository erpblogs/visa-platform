from odoo import api, fields, models

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    is_visa_template = fields.Boolean(string="Is Visa Template", default=False,
                                    help="Check this box if this survey is a template for visa applications")
    visa_category_ids = fields.One2many('visa.category', 'checklist_survey_id', 
                                      string='Visa Categories')
    visa_category_count = fields.Integer(compute='_compute_visa_category_count', 
                                       string='Visa Category Count')

    @api.depends('visa_category_ids')
    def _compute_visa_category_count(self):
        for survey in self:
            survey.visa_category_count = len(survey.visa_category_ids)

    def action_view_visa_categories(self):
        self.ensure_one()
        return {
            'name': 'Visa Categories',
            'view_mode': 'tree,form',
            'res_model': 'visa.category',
            'type': 'ir.actions.act_window',
            'domain': [('checklist_survey_id', '=', self.id)],
        }