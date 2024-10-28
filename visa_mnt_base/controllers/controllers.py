# -*- coding: utf-8 -*-
# from odoo import http


# class VisaMntBase(http.Controller):
#     @http.route('/visa_mnt_base/visa_mnt_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/visa_mnt_base/visa_mnt_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('visa_mnt_base.listing', {
#             'root': '/visa_mnt_base/visa_mnt_base',
#             'objects': http.request.env['visa_mnt_base.visa_mnt_base'].search([]),
#         })

#     @http.route('/visa_mnt_base/visa_mnt_base/objects/<model("visa_mnt_base.visa_mnt_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('visa_mnt_base.object', {
#             'object': obj
#         })

