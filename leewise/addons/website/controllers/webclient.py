# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import http
from leewise.http import request
from leewise.addons.web.controllers.webclient import WebClient


class WebsiteWebClient(WebClient):
    @http.route()
    def bundle(self, bundle_name, **bundle_params):
        if 'website_id' in bundle_params:
            request.update_context(website_id=int(bundle_params['website_id']))
        return super().bundle(bundle_name, **bundle_params)
