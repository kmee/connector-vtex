# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class ProductCategory(models.Model):
    _name = 'product.category'
    _inherit = ['product.category', 'vtex.mixin']

    vtex_bind_ids = fields.One2many(
        comodel_name='vtex.product.category',
        inverse_name='odoo_id',
    )
