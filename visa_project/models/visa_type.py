from odoo import fields, models

class VisaType(models.Model):
    _inherit = 'visa.type'

    project_id = fields.Many2one('project.project', string='Project Template', 
        help="Project template containing standard tasks for this visa type")
    task_template_ids = fields.One2many('project.task', 'visa_type_id', 
        string='Task Templates', domain=[('is_template', '=', True)]) 