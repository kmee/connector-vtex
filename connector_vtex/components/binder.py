# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.addons.component.core import Component
from odoo import tools


class VtexModelBinder(Component):
    _name = 'vtex.binder'
    _inherit = ['base.binder', 'base.vtex.connector']
    _apply_on = [
        'vtex.product.brand',
        'vtex.product.category',
    ]
    _external_field = 'vtex_id'

    def to_internal(self, external_id, unwrap=False):
        """ Give the Odoo recordset for an external ID

        :param external_id: external ID for which we want
                            the Odoo ID
        :param unwrap: if True, returns the normal record
                       else return the binding record
        :return: a recordset, depending on the value of unwrap,
                 or an empty recordset if the external_id is not mapped
        :rtype: recordset
        """
        bindings = self.model.with_context(active_test=False).search(
            [(self._external_field, '=', tools.ustr(external_id)),
             (self._backend_field, '=', self.backend_record.id)]
        )
        if not bindings:
            return None

        if len(bindings) > 1:
            # can be the case for vtex.product.product because the same
            # product can be binded to several catalogue
            assert len(set([binding[self._odoo_field]
                            for binding in bindings])) == 1, (
                    "Multiple value for same id %s" % external_id)
            bindings = bindings[0]

        if unwrap:
            bindings = bindings[self._odoo_field]
        return bindings
