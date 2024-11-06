# models/visa_category.py
from odoo import fields, models

class VisaCategory(models.Model):
    _name = 'visa.category'
    _description = 'Visa Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    country_id = fields.Many2one('res.country', string="Issuing Country")
    fee = fields.Float(string='Application Fee')
    visa_type_id = fields.Many2one('visa.type', string='Visa Type')