# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    l10n_in_uan = fields.Char(string='UAN', groups="hr.group_hr_user")
    l10n_in_pan = fields.Char(string='PAN', groups="hr.group_hr_user")
    l10n_in_esic_number = fields.Char(string='ESIC Number', groups="hr.group_hr_user")
    l10n_in_relationship = fields.Char("Relationship", groups="hr.group_hr_user", tracking=True)
    l10n_in_residing_child_hostel = fields.Integer("Child Residing in hostel", groups="hr.group_hr_user", tracking=True)

    _sql_constraints = [
        ('unique_l10n_in_uan', 'unique (l10n_in_uan)', 'This UAN already exists'),
        ('unique_l10n_in_pan', 'unique (l10n_in_pan)', 'This PAN already exists'),
        ('unique_l10n_in_esic_number', 'unique (l10n_in_esic_number)', 'This ESIC Number already exists'),
    ]
