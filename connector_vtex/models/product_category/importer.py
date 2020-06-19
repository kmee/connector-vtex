# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class CategoryBatchImporter(Component):
    _name = 'vtex.product.category.batch.importer'
    _inherit = 'vtex.delayed.batch.importer'
    _apply_on = ['vtex.product.category']


class ProductCategoryImporter(Component):
    _name = 'vtex.product.category.importer'
    _inherit = 'vtex.importer'
    _apply_on = ['vtex.product.category']

    def _import_dependencies(self):
        """ Import the dependencies for the record"""
        record = self.vtex_record
        # import parent category
        # the root category has a 0 parent_id
        if record.get('parent'):
            self._import_dependency(record.get('parent'), self.model)
