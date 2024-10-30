from odoo import api, fields, models

class Survey(models.Model):
    _inherit = 'survey.survey'

    is_visa_checklist = fields.Boolean(
        string='Is Visa Checklist',
        help='Use this survey as a visa application checklist'
    )
    service_id = fields.Many2one(
        'product.template',
        string='Visa Service',
        domain=[('type', '=', 'service')],
        help='Link this checklist to a specific visa service'
    )
    checklist_type = fields.Selection([
        ('document', 'Document Checklist'),
        ('requirement', 'Requirement Checklist'),
        ('interview', 'Interview Checklist'),
    ], string='Checklist Type')
    is_mandatory = fields.Boolean(
        string='Mandatory',
        help='Is this checklist mandatory for visa application?'
    )
    application_stage_ids = fields.Many2many(
        'visa.application.stage',
        string='Applicable Stages',
        help='Stages where this checklist should be completed'
    )
    instruction = fields.Html(
        string='Instructions',
        help='Instructions for completing this checklist'
    )

    def action_start_checklist(self, application_id):
        self.ensure_one()
        # Create user input (survey response) for this checklist
        user_input = self.env['survey.user_input'].create({
            'survey_id': self.id,
            'partner_id': self.env.user.partner_id.id,
            'application_id': application_id,
        })
        return self.action_start_survey(user_input)