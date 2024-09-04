# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import http
from leewise.addons.website.controllers import main


class Website(main.Website):
    @http.route()
    def autocomplete(self, search_type=None, term=None, order=None, limit=5, max_nb_chars=999, options=None):
        """
            For the search results, concatenate the appointment names with
            their respective duration in the search bar dropdown display.
        """
        res = super().autocomplete(search_type, term, order, limit, max_nb_chars, options)
        if search_type == 'appointments':
            for result in res['results']:
                if result['name'] and result['detail']:
                    result['name'] += ' (' + result['detail'] + ')'
        return res
