from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class VisaApplication(models.Model):
    _name = 'visa.application'
    _description = 'Visa Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Application Number', required=True, copy=False, readonly=True, default='New')
    partner_id = fields.Many2one('res.partner', string='Applicant', required=True, tracking=True)
    category_id = fields.Many2one('visa.category', string='Visa Category', required=True, tracking=True)
    stage_id = fields.Many2one('visa.stage', string='Stage', default=lambda self: self.env['visa.stage'].search([], limit=1), tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', tracking=True)
    date_submitted = fields.Date(string='Submission Date')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string='Priority', default='1')
    checklist_survey_id = fields.Many2one('survey.survey', string='Checklist Survey')
    checklist_user_input_id = fields.Many2one('survey.user_input', string='Checklist Responses')
    invoice_id = fields.Many2one('account.move', string='Invoice')

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['visa.stage'].search([])
        return stage_ids

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('visa.application') or 'New'
        return super(VisaApplication, self).create(vals)

    def action_start_checklist(self):
        self.ensure_one()
        if not self.checklist_survey_id:
            raise UserError(_("No checklist survey defined for this visa category."))
        if self.checklist_user_input_id:
            return self.checklist_survey_id.action_start_survey(answer=self.checklist_user_input_id)
        else:
            user_input = self.checklist_survey_id._create_answer(partner=self.partner_id)
            self.checklist_user_input_id = user_input.id
            return self.checklist_survey_id.action_start_survey(answer=user_input)

    def action_view_checklist_results(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'name': "Checklist Results",
            'target': 'new',
            'url': '/survey/results/%s' % self.checklist_user_input_id.access_token
        }

    def action_submit(self):
        self.write({
            'state': 'submitted',
            'date_submitted': date.today(),
        })

    def action_review(self):
        self.write({'state': 'under_review'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_reject(self):
        self.write({'state': 'rejected'})
        
    def action_create_invoice(self):
        for application in self:
            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': application.partner_id.id,
                'invoice_line_ids': [(0, 0, {
                    'name': f'Visa Application Fee - {application.category_id.name}',
                    'quantity': 1,
                    'price_unit': application.category_id.fee,
                })],
            })
            application.invoice_id = invoice.id

    def action_print_affidavit(self):
        return self.env.ref('visa_management.action_report_visa_affidavit').report_action(self)

    def action_print_receipt(self):
        return self.env.ref('visa_management.action_report_visa_receipt').report_action(self)