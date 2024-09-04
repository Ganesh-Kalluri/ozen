# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models

class ProjectTaskConvertWizard(models.TransientModel):
    _inherit = 'project.task.convert.wizard'

    def _default_team_id(self):
        tasks_to_convert = self._get_tasks_to_convert()
        teams = tasks_to_convert.project_id.helpdesk_team
        if len(teams) == 1:
            return teams.id
        elif len(teams) > 1:
            return teams.sorted('sequence')[0].id
        else:
            return False
