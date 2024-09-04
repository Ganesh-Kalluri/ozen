# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models

class PayrollNote(models.Model):
    _name = 'hr.payroll.note'
    _description = "Payroll Note"

    name = fields.Char(required=True)
    note = fields.Html(required=True)
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
