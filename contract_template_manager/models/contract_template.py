from odoo import models, fields, api
from odoo.exceptions import UserError


class ContractContractInherit(models.Model):
    _inherit = 'contract.contract'

    report_id = fields.Many2one(
        'ir.actions.report', 
        string='Contract Report Template',
        domain=[('model', '=', 'contract.contract')],
        help="Select the report template to use for contracts created from this template"
    )

class ContractTemplateInherit(models.Model):
    _inherit = 'contract.template'

    report_id = fields.Many2one(
        'ir.actions.report', 
        string='Contract Report Template',
        domain=[('model', '=', 'contract.contract')],
        help="Select the report template to use for contracts created from this template"
    )

    def action_preview_template(self):
        self.ensure_one()
        contract_id = self.env['contract.contract'].search([], limit=1)

        if not self.report_id:
            raise UserError("Please select a report template first.")
        if not contract_id:
            raise UserError("No contract found for this template!")
        
        return {
            'type': 'ir.actions.report',
            'model': 'contract.contract',
            'binding_model_id': 'contract.model_contract_contract',
            'report_type': 'qweb-pdf',
            'report_name': self.report_id.report_name,
            'report_file': self.report_id.report_file,
            'res_id': contract_id.id,
            'context': {'active_ids': contract_id.ids},
        }