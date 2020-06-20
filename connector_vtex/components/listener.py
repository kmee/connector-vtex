# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component
from odoo.addons.component_event import skip_if

_logger = logging.getLogger(__name__)


class VtexBaseEventListener(Component):
    _name = 'vtex.base.event.listener'
    _inherit = 'base.connector.listener'
    _apply_on = [
        'product.brand',
        'product.category',
    ]

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_create(self, record, fields=None):
        for binding in record.vtex_bind_ids:
            binding.with_delay(
                description="VTEX - CREATE - {}/{} ".format(record._name, record.id)
            ).export_record()

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_write(self, record, fields=None):
        for binding in record.vtex_bind_ids:
            binding.with_delay(
                description="VTEX - WRITE - {}/{} ".format(record._name, record.id)
            ).export_record()

    def on_record_unlink(self, record, fields=None):
        for binding in record.vtex_bind_ids:
            binding.with_delay(
                description="VTEX - DELETE - {}/{} ".format(record._name, record.id)
            ).export_delete_record(binding.backend_id, binding.vtex_id)


class VtexBaseEventListener(Component):
    """
    USE ONLY WITH models _inherit = 'vtex.<odoo.model.name>'
    """
    _name = 'vtex.binding.event.listener'
    _inherit = 'base.connector.listener'

    _apply_on = [
        'vtex.product.brand',
        'vtex.product.category',
    ]

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_create(self, record, fields=None):
        record.with_delay(
            description="VTEX - CREATE - {}/{} ".format(record._name, record.id)
        ).export_record()

    @skip_if(lambda self, record, **kwargs: self.no_connector_export(record))
    def on_record_write(self, record, fields=None):
        record.with_delay(
            description="VTEX - WRITE - {}/{} ".format(record._name, record.id)
        ).export_record()

    def on_record_unlink(self, record, fields=None):
        record.with_delay(
            description="VTEX - DELETE - {}/{} ".format(record._name, record.id)
        ).export_delete_record(record.backend_id, record.vtex_id)
