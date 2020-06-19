# Copyright 2020 KMEE INFORMATICA LTDA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from lxml import etree
from odoo import api, fields, models, tools
from odoo.osv.orm import setup_modifiers


class VtexMixin(models.AbstractModel):
    _name = 'vtex.mixin'
    _description = 'Vtex mixin'

    # Override it on inherited models
    vtex_ids = fields.One2many(
        comodel_name='vtex.binding',
        # inverse_name='odoo_id'
    )

    @api.model
    def fields_view_get(self, view_id=None, view_type="form",
                        toolbar=False, submenu=False):

        model_view = super().fields_view_get(view_id, view_type, toolbar, submenu)

        if view_type == 'form':
            try:
                vtex_view = self.env.ref("connector_vtex.vtex_mixin_form_view")
                vtex_arch = etree.fromstring(vtex_view["arch"])
                doc = etree.fromstring(model_view.get('arch'))
                # Replace page
                doc_page_node = doc.xpath("//notebook")

                if doc_page_node:
                    page_node = vtex_arch.xpath("//page[@name='vtex_page']")[0]
                    for n in page_node.getiterator():
                        setup_modifiers(n)
                    doc_page_node[0].append(page_node)
                else:
                    sheet_page_node = doc.xpath("//sheet") or doc.xpath("//form")

                    field_node = vtex_arch.xpath("//field[@name='vtex_ids']")[0]
                    for n in field_node.getiterator():
                        setup_modifiers(n)
                    sheet_page_node[0].append(field_node)

                model_view["arch"] = etree.tostring(doc, encoding='unicode')
            except Exception:
                return model_view

        return model_view
