# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class CategoryAdapter(Component):
    _name = 'vtex.product.category.adapter'
    _inherit = 'vtex.adapter'
    _apply_on = 'vtex.product.category'
    _api = 'catalog/pvt/category'
    _api_search = 'catalog_system/pub/category/tree/100'
