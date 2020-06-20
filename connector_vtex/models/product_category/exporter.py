# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class ProductCategoryExporter(Component):
    _name = 'vtex.product.category.exporter'
    _inherit = 'vtex.exporter'
    _apply_on = ['vtex.product.category']
