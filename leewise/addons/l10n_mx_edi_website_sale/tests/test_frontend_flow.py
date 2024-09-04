# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.tests import tagged, HttpCase
from leewise.addons.l10n_mx_edi.tests.common import TestMxEdiCommon

@tagged('post_install_l10n', 'post_install', '-at_install')
class TestFrontendFlow(HttpCase, TestMxEdiCommon):
    def test_validate_required_additional_fields(self):
        self.env.company = self.company_data['company']
        self.env['product.product'].create({
            'name': 'Test Product',
            'sale_ok': True,
            'website_published': True,
        })
        self.env['ir.config_parameter'].set_param('sale.automatic_invoice', True)
        self.env['website'].get_current_website().company_id = self.env.company.id
        user_admin = self.env.ref('base.user_admin')
        user_admin.company_ids = user_admin.company_ids + self.env.company
        self.start_tour('/shop', 'test_validate_additional_fields', login='admin')
