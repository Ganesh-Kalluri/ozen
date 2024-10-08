# coding: utf-8
# Part of Leewise. See LICENSE file for full copyright and licensing details.

{
    "name": "Mexico - Month 13 Trial Balance",
    'countries': ['mx'],
    "summary": "Mexico Month 13 Trial Balance Report",
    "version": "1.0",
    "author": "Vauxoo / Leewise",
    "category": "Accounting/Localizations/Reporting",
    "website": "http://www.leewise.in",
    "license": "OEEL-1",
    "depends": [
        "l10n_mx_reports",
    ],
    "data": [
        "views/account_move_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'l10n_mx_reports_closing/static/src/components/**/*',
        ],
    },
    "installable": True,
    "auto_install": True,
}
