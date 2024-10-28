from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class SurveyPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id
        SurveyUser = request.env['survey.user_input']
        
        if 'survey_count' in counters:
            survey_count = SurveyUser.search_count([
                ('partner_id', '=', partner.id),
                # ('state', 'in', ['new', 'in_progress'])
            ])
            values['survey_count'] = survey_count
        return values
    

    @http.route(['/my/surveys'], type='http', auth="user", website=True)
    def portal_my_surveys(self, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        SurveyUser = request.env['survey.user_input']
        
        surveys = SurveyUser.search([
            ('partner_id', '=', partner.id),
            # ('state', 'in', ['new', 'in_progress'])
        ])
        
        values.update({
            'surveys': surveys,
            'page_name': 'surveys',
        })
        return request.render("survey_user_portal.portal_my_surveys", values)
