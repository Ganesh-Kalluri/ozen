# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
{
    'name': 'Inter Company Module for Sale/Purchase Orders and Invoices',
    'version': '1.1',
    'summary': 'Intercompany SO/PO/INV rules',
    'category': 'Productivity',
    'description': ''' Module for synchronization of Documents between several companies. For example, this allow you to have a Sales Order created automatically when a Purchase Order is validated with another company of the system as vendor, and inversely.

    Supported documents are SO, PO.
''',
    'depends': [
        'sale_management',
        'purchase_stock',
        'sale_stock',
        'account_inter_company_rules',
    ],
    'data': [
        'views/inter_company_so_po_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
