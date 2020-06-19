# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class BrandBatchImporter(Component):
    _name = 'vtex.product.brand.batch.importer'
    _inherit = 'vtex.delayed.batch.importer'
    _apply_on = ['vtex.product.brand']

    def run(self, filters=None):
        """ Run the synchronization """
        from_date = filters.pop('from_date', None)
        to_date = filters.pop('to_date', None)
        record_ids = self.backend_adapter.search(
            filters,
            from_date=from_date,
            to_date=to_date,
        )
        _logger.debug('search for vtex Product Brand %s returned %s',
                      filters, record_ids)
        for record_data in record_ids:
            self._import_record(
                external_id=record_data['id'],
                record_data=record_data
            )


class ProductBrandImporter(Component):
    _name = 'vtex.product.brand.importer'
    _inherit = 'vtex.importer'
    _apply_on = ['vtex.product.brand']
