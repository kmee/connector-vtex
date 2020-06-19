# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import requests
import json

from odoo.addons.component.core import AbstractComponent


class VtexCRUDAdapter(AbstractComponent):
    """ External Records Adapter for Vtex """
    _name = 'vtex.crud.adapter'
    _inherit = ['base.backend.adapter', 'base.vtex.connector']
    _usage = 'backend.adapter'

    def process_request(self, http_request, url, headers=None, params=None, data=None):
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        if data is None:
            data = {}
        response = http_request(url, headers=headers, params=params, data=data)
        if response.status_code != 200:
            error = response.json()
            message = '%s - %s' % (error['error']['code'],
                                   error['error']['message'])
            raise Exception(message)
        return response.json()

    def _prepare_headers(self):
        return {
            'Content-Type': 'application/json',
            'X-VTEX-API-AppKey': self.backend_record.app_key,
            'X-VTEX-API-AppToken': self.backend_record.app_token,
        }

    def _prepare_url(self, url):
        return 'https://{accountName}.{environment}.com.br/api/{endpoint}'.format(
            accountName=self.backend_record.account_name,
            environment=self.backend_record.environment,
            endpoint=url,
        )

    def _call(self, http_request, url, params, data=None, **kwargs):
        return self.process_request(
            http_request,
            url=self._prepare_url(url),
            headers=self._prepare_headers(),
            params=params,
            data=data,
            **kwargs
        )


class GenericAdapter(AbstractComponent):
    _name = 'vtex.adapter'
    _inherit = 'vtex.crud.adapter'

    _model_name = None
    _api = None
    _api_search = None

    def search(self, params, from_date, to_date):
        return self._call(
            requests.get,
            url=self._api_search or self._api,
            params=params if params else {}
        )
