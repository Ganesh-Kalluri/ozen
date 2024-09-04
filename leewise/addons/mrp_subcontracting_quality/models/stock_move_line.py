# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.


from leewise import models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _unlink_quality_check(self):
        if self.env.user.partner_id.is_subcontractor and not self.env.su:
            super(StockMoveLine, self.sudo())._unlink_quality_check()
            self.sudo(False)
        else:
            super()._unlink_quality_check()
