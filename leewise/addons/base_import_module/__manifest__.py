# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.
{
    'name': 'Base import module',
    'description': """
Import a custom data module
===========================

This module allows authorized users to import a custom data module (.xml files and static assests)
for customization purpose.
""",
    'category': 'Hidden/Tools',
    'depends': ['web'],
    'installable': True,
    'auto_install': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_import_module_view.xml',
        'views/ir_module_views.xml',
    ],
    'license': 'LGPL-3',
}
