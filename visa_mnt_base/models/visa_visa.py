# models/visa.py
from odoo import api, fields, models

class Visa(models.Model):
    _name = 'visa.visa'
    _description = 'Visa'
    _order = 'expiry_date desc'

    name = fields.Char(string="Visa Number", required=True)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    visa_type_id = fields.Many2one('visa.type', string="Visa Type", required=True)
    issue_date = fields.Date(string="Issue Date")
    expiry_date = fields.Date(string="Expiry Date")
    country_id = fields.Many2one('res.country', string="Issuing Country")
    status = fields.Selection([
        ('valid', 'Valid'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ], string="Status", compute='_compute_status', store=True)

    @api.depends('expiry_date')
    def _compute_status(self):
        today = fields.Date.today()
        for visa in self:
            if not visa.expiry_date:
                visa.status = 'valid'
            elif visa.expiry_date < today:
                visa.status = 'expired'
            else:
                visa.status = 'valid'

    # You might want to add more fields and methods as needed