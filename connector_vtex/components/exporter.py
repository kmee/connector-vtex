# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import AbstractComponent


class VtexExporter(AbstractComponent):
    """ Base exporter for Vtex """
    _name = 'vtex.exporter'
    _inherit = ['base.exporter', 'base.vtex.connector']
    _usage = 'record.exporter'

    def __init__(self, work_context):
        super(VtexExporter, self).__init__(work_context)
        self._vtex_record = None

    def export(self, map_record):
        return map_record.values()

    def _map_data(self):
        return self.mapper.map_record(self._vtex_record)
