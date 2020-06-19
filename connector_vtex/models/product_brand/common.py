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
    keywords = fields.Char(
        string='Keywords'
    )
    site_title = fields.Char(
        string='SiteTitle'
    )
    active = fields.Boolean(
        default=True
    )
    menu_home = fields.Boolean(
        string="MenuHome",
    )
    adwords_remarketing_code = fields.Char(
        string="AdWordsRemarketingCode"
    )
    lomadee_campaing_code = fields.Char(
        string="LomadeeCampaignCode"
    )
    score = fields.Char(
        string="Score"
    )
    link_id = fields.Char(
        string='Link ID'
    )
