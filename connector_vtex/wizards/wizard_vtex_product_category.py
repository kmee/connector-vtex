# -*- coding: utf-8 -*-
# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class WizardVtexProductCategory(models.TransientModel):

    _name = 'wizard.vtex.product.category'

    def _default_backend(self):
        return self.env['vtex.backend'].search([], limit=1).id

    backend_id = fields.Many2one(
        comodel_name='vtex.backend',
        default=_default_backend,
        string='Backend',
    )

    @api.multi
    def doit(self):
        self.ensure_one()
        for wizard in self:
            vtex_category_obj = self.env['vtex.product.category']

            for category in self.env['product.category'].browse(
                    wizard.env.context['active_ids']):

                if not vtex_category_obj.search_count([
                    ('odoo_id', '=', category.id),
                    ('backend_id', '=', self.backend_id.id),
                ]):
                    vtex_category_obj.create({
                        'backend_id': self.backend_id.id,
                        'odoo_id': category.id,
                    })