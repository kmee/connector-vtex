# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class ProductBrandImportMapper(Component):
    _name = 'vtex.product.brand.import.mapper'
    _inherit = 'vtex.import.mapper'
    _apply_on = 'vtex.product.brand'

    direct = [
        ('name', 'name'),
        ('image_url', 'imageUrl'),
        ('site_title', 'title'),
        ('active', 'isActive'),
        ('title', 'title'),
        ('meta_tag_description', 'meta_tag_description'),
    ]
