# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise import models


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    def _reset_carrier_id(self, new_picking):
        """ For starshipit, we want to keep the provider when generating a return. """
        picking = self.env['stock.picking'].browse(new_picking)
        if picking.carrier_id.delivery_type != 'starshipit' or not picking.carrier_id.can_generate_return:
            super()._reset_carrier_id(new_picking)
