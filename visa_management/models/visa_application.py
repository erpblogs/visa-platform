from datetime import date
from odoo import api, fields, models, _

class VisaApplication(models.Model):
    _name = 'visa.application'
    _description = 'Visa Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Application Number', required=True, copy=False, readonly=True, default='New')
    partner_id = fields.Many2one('res.partner', string='Applicant', required=True, tracking=True)
    category_id = fields.Many2one('visa.category', string='Visa Category', required=True, tracking=True)
    stage_id = fields.Many2one('visa.stage', string='Stage', 
                              default=lambda self: self.env['visa.stage'].search([], limit=1), 
                              tracking=True)
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
    notes = fields.Text(string='Notes')
    active = fields.Boolean(default=True)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['visa.stage'].search([])
        return stage_ids

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('visa.application') or 'New'
        return super(VisaApplication, self).create(vals)

    def action_submit(self):
        self.write({
            'state': 'submitted',
            'date_submitted': fields.Date.today(),
        })

    def action_review(self):
        self.write({'state': 'under_review'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_reject(self):
        self.write({'state': 'rejected'})