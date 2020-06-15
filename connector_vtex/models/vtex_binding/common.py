# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields
from odoo.addons.queue_job.job import job, related_action


class VtexBinding(models.AbstractModel):

    """ Abstract Model for the Bindigs.

    All the models used as bindings between Vtex and OpenERP
    (``vtex.res.partner``, ``vtex.product.product``, ...) should
    ``_inherit`` it.
    """
    _name = 'vtex.binding'
    _inherit = 'external.binding'
    _description = 'Vtex Binding (abstract)'

    # odoo_id = openerp-side id must be declared in concrete model
    backend_id = fields.Many2one(
        comodel_name='vtex.backend',
        string='Vtex Backend',
        required=True,
        ondelete='restrict',
    )
    external_id = fields.Char(string='ID on Vtex')

    _sql_constraints = [
        ('vtex_uniq', 'unique(backend_id, external_id)',
         'A binding already exists with the same Vtex ID.'),
    ]
