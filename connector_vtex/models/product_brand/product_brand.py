# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class ProductBrand(models.Model):
    _name = 'product.brand'
    _inherit = ['product.brand', 'vtex.mixin']

    vtex_bind_ids = fields.One2many(
        comodel_name='vtex.product.brand',
        inverse_name='odoo_id',
    )
