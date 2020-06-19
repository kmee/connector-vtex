# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class VtexProductBrand(models.Model):
    _name = 'vtex.product.brand'
    _inherit = 'vtex.binding'
    _inherits = {'product.brand': 'odoo_id'}
    _description = 'vtex product brand'

    _rec_name = 'name'

    odoo_id = fields.Many2one(
        comodel_name='product.brand',
        string='brand',
        required=True,
        ondelete='cascade'
    )
    image_url = fields.Char(
        string='Category Image URL',
        help='imageUrl'
    )
    active = fields.Boolean(
        string='If the Brand is active',
        default=True,
        help='isActive'
    )
    title = fields.Char(
        string='Meta Title for the Brand page',
        help='title'
    )
    meta_tag_description = fields.Char(
        string='Meta Description for the Brand page',
        help='metaTagDescription',
    )
