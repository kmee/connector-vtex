# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class BrandAdapter(Component):
    _name = 'vtex.product.brand.adapter'
    _inherit = 'vtex.adapter'
    _apply_on = 'vtex.product.brand'
    _api = 'catalog/pvt/brand'
    _api_search = 'catalog_system/pvt/brand/list'
