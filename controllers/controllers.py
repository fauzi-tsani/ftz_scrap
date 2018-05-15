# -*- coding: utf-8 -*-
from odoo import http

# class FtzAddons/(http.Controller):
#     @http.route('/ftz_addons//ftz_addons//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ftz_addons//ftz_addons//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ftz_addons/.listing', {
#             'root': '/ftz_addons//ftz_addons/',
#             'objects': http.request.env['ftz_addons/.ftz_addons/'].search([]),
#         })

#     @http.route('/ftz_addons//ftz_addons//objects/<model("ftz_addons/.ftz_addons/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ftz_addons/.object', {
#             'object': obj
#         })