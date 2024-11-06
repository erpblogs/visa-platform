from odoo import fields, models, api, _
from odoo.exceptions import UserError

class VisaApplication(models.Model):
    _inherit = 'visa.application'

    checklist_survey_id = fields.Many2one('survey.survey', 
        related='category_id.checklist_survey_id', string='Checklist Survey',
        help="Survey template used as checklist for this application")
    checklist_user_input_id = fields.Many2one('survey.user_input', 
        string='Checklist Responses',
        help="User's responses to the checklist")
    checklist_state = fields.Selection(related='checklist_user_input_id.state', 
        string='Checklist Status')
    checklist_score = fields.Float(related='checklist_user_input_id.scoring_percentage', 
        string='Checklist Score (%)')
    checklist_deadline = fields.Date(string='Checklist Deadline')

    def action_start_checklist(self):
        """Start or continue filling the checklist"""
        self.ensure_one()
        if not self.checklist_survey_id:
            raise UserError(_("No checklist template defined for this visa category."))

        if not self.checklist_user_input_id:
            # Create new response
            user_input = self.checklist_survey_id._create_answer(
                partner=self.partner_id,
                deadline=self.checklist_deadline)
            self.checklist_user_input_id = user_input.id

        action = self.checklist_survey_id.action_start_survey()
        action.update({
            'target': 'new',
            'answer_token': self.checklist_user_input_id.access_token,
        })
        return action

    def action_view_checklist_results(self):
        """View checklist results"""
        self.ensure_one()
        if not self.checklist_user_input_id:
            raise UserError(_("No checklist has been filled out yet."))

        return {
            'type': 'ir.actions.act_url',
            'name': "Checklist Results",
            'target': 'new',
            'url': '/survey/results/%s' % self.checklist_user_input_id.access_token
        }

    def action_reset_checklist(self):
        """Reset checklist to start over"""
        self.ensure_one()
        if self.checklist_user_input_id:
            self.checklist_user_input_id.unlink()