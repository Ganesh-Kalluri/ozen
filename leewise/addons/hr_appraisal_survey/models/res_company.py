# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    def _get_default_appraisal_survey_template_id(self):
        return self.env.ref('hr_appraisal_survey.appraisal_360_feedback_template', raise_if_not_found=False)

    appraisal_survey_template_id = fields.Many2one('survey.survey')
