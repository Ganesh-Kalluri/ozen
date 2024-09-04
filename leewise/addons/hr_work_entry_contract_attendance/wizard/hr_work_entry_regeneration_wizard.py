# -*- coding:utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models

class HrWorkEntryRegenerationWizard(models.TransientModel):
    _inherit = 'hr.work.entry.regeneration.wizard'

    def _work_entry_fields_to_nullify(self):
        return super()._work_entry_fields_to_nullify() + ['attendance_id']
