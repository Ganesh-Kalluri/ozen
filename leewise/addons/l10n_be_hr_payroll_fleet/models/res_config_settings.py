# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    max_unused_cars = fields.Integer(string='Maximum unused cars', default=1000, config_parameter='l10n_be_hr_payroll_fleet.max_unused_cars')
