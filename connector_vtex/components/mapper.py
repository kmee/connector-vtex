# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.addons.component.core import AbstractComponent
from odoo.addons.connector.components.mapper import mapping


class VtexImportMapper(AbstractComponent):
    _name = 'vtex.import.mapper'
    _inherit = ['base.vtex.connector', 'base.import.mapper']
    _usage = 'import.mapper'

    @mapping
    def backend_id(self, record):
        return {'backend_id': self.backend_record.id}


class VtexExportMapper(AbstractComponent):
    _name = 'vtex.export.mapper'
    _inherit = ['base.vtex.connector', 'base.export.mapper']
    _usage = 'export.mapper'
