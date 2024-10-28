# models/res_partner.py
from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    passport_number = fields.Char(string="Passport Number")
    passport_expiry_date = fields.Date(string="Passport Expiry Date")
    nationality = fields.Many2one('res.country', string="Nationality")
    visa_ids = fields.One2many('visa.visa', 'partner_id', string="Visas")
    visa_application_ids = fields.One2many('visa.application', 'partner_id', string="Visa Applications")