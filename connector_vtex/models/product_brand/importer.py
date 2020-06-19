# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class BrandBatchImporter(Component):
    _name = 'vtex.product.brand.batch.importer'
    _inherit = 'vtex.delayed.batch.importer'
    _apply_on = ['vtex.product.brand']


class ProductBrandImporter(Component):
    _name = 'vtex.product.brand.importer'
    _inherit = 'vtex.importer'
    _apply_on = ['vtex.product.brand']
