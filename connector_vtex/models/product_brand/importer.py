# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping
from odoo.addons.connector.exception import MappingError

_logger = logging.getLogger(__name__)


class BrandBatchImporter(Component):
    _name = 'vtex.product.brand.batch.importer'
    _inherit = 'vtex.delayed.batch.importer'
    _apply_on = ['vtex.product.brand']

    def _import_record(self, external_id, job_options=None):
        """ Delay a job for the import """
        super(BrandBatchImporter, self)._import_record(
            external_id, job_options=job_options)

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
        for record_id in record_ids:
            self._import_record(record_id)


class ProductBrandImporter(Component):
    _name = 'vtex.product.brand.importer'
    _inherit = 'vtex.importer'
    _apply_on = ['vtex.product.brand']


class ProductBrandImportMapper(Component):
    _name = 'vtex.product.brand.import.mapper'
    _inherit = 'vtex.import.mapper'
    _apply_on = 'vtex.product.brand'

    direct = [
        ('name', 'Name'),
        ('description', 'Text'),
        ('keywords', 'Keywords'),
        ('site_title', 'SiteTitle'),
        ('active', 'Active'),
        ('menu_home', 'MenuHome'),
        ('adwords_remarketing_code', 'AdWordsRemarketingCode'),
        ('lomadee_campaing_code', 'LomadeeCampaignCode'),
        ('score', 'Score'),
        ('link_id', 'LinkId'),
    ]

    @mapping
    def backend_id(self, record):
        return {'backend_id': self.backend_record.id}
