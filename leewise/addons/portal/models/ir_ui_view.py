# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models, fields


class View(models.Model):
    _inherit = "ir.ui.view"

    customize_show = fields.Boolean("Show As Optional Inherit", default=False)
