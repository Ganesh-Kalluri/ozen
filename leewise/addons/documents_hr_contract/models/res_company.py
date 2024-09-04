# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    documents_hr_contracts_tags = fields.Many2many('documents.tag', 'documents_hr_contracts_tags_table')
