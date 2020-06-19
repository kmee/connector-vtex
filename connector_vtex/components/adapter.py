# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import requests

from odoo.addons.component.core import AbstractComponent


class VtexCRUDAdapter(AbstractComponent):
    """ External Records Adapter for Vtex """
    _name = 'vtex.crud.adapter'
    _inherit = ['base.backend.adapter', 'base.vtex.connector']
    _usage = 'backend.adapter'

    def _call(self, url, params, **kwargs):
        pass


class GenericAdapter(AbstractComponent):
    _name = 'vtex.adapter'
    _inherit = 'vtex.crud.adapter'

    _model_name = None
    _api = None

    def search(self, params, from_date, to_date):
        return self._call(self._api, params if params else {})
