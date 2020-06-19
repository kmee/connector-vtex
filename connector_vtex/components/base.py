# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import AbstractComponent


class BaseVtexConnector(AbstractComponent):
    """ Base component for the connector

    Is inherited by every components of the Connector (Binder, Mapper, ...)
    and adds a few methods which are of common usage in the connectors.

    """
    _name = 'base.vtex.connector'
    _inherit = 'base.connector'
    _collection = 'vtex.backend'
