from odoo import api, fields, models

class ProjectTask(models.Model):
    _inherit = 'project.task'

    visa_type_id = fields.Many2one('visa.type', string='Visa Type Template')
    visa_application_id = fields.Many2one('visa.application', string='Visa Application')
    is_template = fields.Boolean(string='Is Template Task', 
        compute='_compute_is_template', store=True)

    @api.depends('visa_type_id')
    def _compute_is_template(self):
        for task in self:
            task.is_template = bool(task.visa_type_id)

    def create_from_template(self, visa_application_id):
        """Create a new task from template"""
        new_task = self.copy({
            'visa_type_id': False,
            'is_template': False,
            'visa_application_id': visa_application_id,
        })
        return new_task