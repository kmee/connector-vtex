# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

try:
    from vtex import Vtex
except ImportError:
    _logger.debug("Cannot import 'vtex'")


class VtexBackend(models.Model):

    _name = 'vtex.backend'
    _description = 'Vtex Backend'

    name = fields.Char()

    app_key = fields.Char()
    app_token = fields.Char()
    environment = fields.Char()
    account_name = fields.Char()
    base_url = fields.Char(readonly=True)

    def get_client(self):
        return Vtex(self.account_name, self.environment, self.app_key, self.app_token)

    @api.multi
    def test_connection(self):
        for record in self:
            client = record.get_client()
            try:
                record.base_url = client.master_data.base_url
            except Exception as e:
                raise UserError(
                    _("Error {}".format(e))
                )
