# models/visa_type.py
from odoo import api, fields, models

class VisaType(models.Model):
    _name = 'visa.type'
    _description = 'Visa Type'

    name = fields.Char(string="Visa Type Name", required=True)
    code = fields.Char(string="Code", required=True)
    description = fields.Text(string="Description")
    duration = fields.Integer(string="Default Duration (days)")
    is_active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'The code must be unique for each visa type.')
    ]