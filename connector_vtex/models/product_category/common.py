# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class VtexProductCategory(models.Model):
    _name = 'vtex.product.category'
    _inherit = 'vtex.binding'
    _inherits = {'product.category': 'odoo_id'}
    _description = 'vtex product category'

    _rec_name = 'name'

    odoo_id = fields.Many2one(
        comodel_name='product.category',
        string='category',
        required=True,
        ondelete='cascade'
    )
    title = fields.Char(
        string='title'
    )
    meta_tag_description = fields.Char(
        string='MetaTagDescription'
    )
    has_children = fields.Boolean()
    vtex_parent_id = fields.Many2one(
        comodel_name='vtex.product.category',
        string='Vtex Parent Category',
        ondelete='cascade', )
    vtex_child_id = fields.One2many(
        comodel_name='vtex.product.category',
        inverse_name='vtex_parent_id',
        string='Vtex Child Categories',
    )
