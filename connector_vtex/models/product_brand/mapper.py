# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import convert

_logger = logging.getLogger(__name__)


class ProductBrandImportMapper(Component):
    _name = 'vtex.product.brand.import.mapper'
    _inherit = 'vtex.import.mapper'
    _apply_on = 'vtex.product.brand'

    direct = [
        ('name', 'name'),
        ('image_url', 'imageUrl'),
        ('active', 'isActive'),
        ('title', 'title'),
        ('meta_tag_description', 'metaTagDescription'),
    ]


class ProductBrandExportMapper(Component):
    _name = 'vtex.product.brand.export.mapper'
    _inherit = 'vtex.export.mapper'
    _apply_on = 'vtex.product.brand'

    direct = [
        ('name', 'Name'),
        ('description', 'Text'),
        # ('image_url', 'imageUrl'),
        ('active', 'Active'),
        ('title', 'SiteTitle'),
        ('meta_tag_description', 'metaTagDescription'),
        ('menu_home', 'MenuHome'),
    ]
