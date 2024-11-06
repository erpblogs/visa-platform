from odoo import fields, models

class VisaApplication(models.Model):
    _inherit = 'visa.application'

    contract_id = fields.Many2one('contract.contract', string='Contract')
    contract_state = fields.Selection(related='contract_id.state', string='Contract Status')

    def action_create_contract(self):
        """Create contract for visa application"""
        self.ensure_one()
        if not self.contract_id:
            contract = self.env['contract.contract'].create_from_application(self)
            self.contract_id = contract.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'contract.contract',
            'res_id': self.contract_id.id,
            'view_mode': 'form',
            'target': 'current',
        } 