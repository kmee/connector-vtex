# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class CategoryBatchImporter(Component):
    _name = 'vtex.product.category.batch.importer'
    _inherit = 'vtex.delayed.batch.importer'
    _apply_on = ['vtex.product.category']

    def run(self, filters=None):
        """ Run the synchronization """
        from_date = filters.pop('from_date', None)
        to_date = filters.pop('to_date', None)
        record_ids = self.backend_adapter.search(
            filters,
            from_date=from_date,
            to_date=to_date,
        )
        _logger.debug('search for vtex %s - %s returned %s',
                      self._name, filters, record_ids)

        base_priority = 10

        def import_nodes(tree, level=0):
            for item in tree:
                # By changing the priority, the top level category has
                # more chance to be imported before the childrens.
                # However, importers have to ensure that their parent is
                # there and import it if it doesn't exist
                children = False
                job_options = {
                    'priority': base_priority + level,
                }

                if item.get('children'):
                    children = item.pop('children')

                self._import_record(
                    external_id=item['id'],
                    record_data=item,
                    job_options=job_options
                )

                if children:
                    for c in children:
                        c['parent'] = item['id']
                    import_nodes(children, level=level + 1)
        import_nodes(record_ids)


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
            self._import_dependency(
                vtex_id=record.get('parent'),
                binding_model=self.model,
                vtex_data=record
            )
