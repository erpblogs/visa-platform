# models/visa_category.py
from odoo import fields, models

class VisaCategoryInherit(models.Model):
    _inherit = 'visa.category'

    checklist_survey_id = fields.Many2one('survey.survey', string='Checklist Survey', 
                                          help="Survey to use as a checklist for this visa category")