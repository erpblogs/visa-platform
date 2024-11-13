from odoo import models, fields, api

class ContractTemplatePreviewWizard(models.TransientModel):
    _name = 'contract.template.preview.wizard'
    _description = 'Contract Template Preview'

    template_id = fields.Many2one('contract.template', string='Template', required=True)
    preview_content = fields.Html(string='Preview', readonly=True)

    @api.onchange('template_id')
    def _onchange_template_id(self):
        if self.template_id:
            template = self.env['ir.qweb']._render(
                'contract_template_manager.contract_template_content',
                self.template_id.get_preview_data()
            )
            self.preview_content = template 