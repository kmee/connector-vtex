# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.tools.translate import _
from odoo.addons.component.core import AbstractComponent


class VtexDeleter(AbstractComponent):
    """ Base deleter for Vtex """
    _name = 'vtex.deleter'
    _inherit = ['base.deleter', 'base.vtex.connector']
    _usage = 'record.exporter.deleter'

    def run(self, external_id):
        """ Run the synchronization, delete the record on Vtex

        :param external_id: identifier of the record to delete
        """
        self.backend_adapter.delete(external_id)
        return _('Record %s deleted on Vtex') % (external_id,)
