# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping
from odoo.addons.connector.exception import MappingError


_logger = logging.getLogger(__name__)

class ProductCategoryImportMapper(Component):
    _name = 'vtex.product.category.import.mapper'
    _inherit = 'vtex.import.mapper'
    _apply_on = 'vtex.product.category'

    direct = [
        ('name', 'name'),
        ('title', 'Title'),
        ('meta_tag_description', 'MetaTagDescription'),
        ('has_children', 'hasChildren'),
    ]

    @mapping
    def parent_id(self, record):
        if not record.get('parent'):
            return
        binder = self.binder_for()
        parent_binding = binder.to_internal(record['parent'])

        if not parent_binding:
            raise MappingError("The product category with "
                               "vtex id %s is not imported." %
                               record['parent_id'])

        parent = parent_binding.odoo_id
        return {'parent_id': parent.id, 'vtex_parent_id': parent_binding.id}


class ProductCategoryExportMapper(Component):
    _name = 'vtex.product.category.export.mapper'
    _inherit = 'vtex.export.mapper'
    _apply_on = 'vtex.product.category'

    direct = [
        ('name', 'name'),
        ('title', 'Title'),
        ('meta_tag_description', 'MetaTagDescription'),
        ('has_children', 'hasChildren'),
    ]

