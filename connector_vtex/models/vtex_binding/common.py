# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.addons.queue_job.job import job


class VtexBinding(models.AbstractModel):
    """ Abstract Model for the Bindings.

    All the models used as bindings between Vtex and OpenERP
    (``vtex.product.product``, ...) should
    ``_inherit`` it.
    """
    _name = 'vtex.binding'
    _inherit = 'external.binding'
    _description = 'Vtex Binding (abstract)'

    # odoo_id = odoo-side id must be declared in concrete model
    backend_id = fields.Many2one(
        comodel_name='vtex.backend',
        string='Vtex Backend',
        required=True,
        ondelete='restrict',
    )
    vtex_id = fields.Char(string='ID on Vtex')
    create_date = fields.Datetime('Create Date', readonly=True)
    write_date = fields.Datetime('Update Date', readonly=True)
    create_uid = fields.Many2one('res.users', string='Creator', readonly=True)
    write_uid = fields.Many2one('res.users', string='Writer', readonly=True)

    @job(default_channel='root.vtex')
    @api.model
    def import_record(self, backend, external_id, record_data):
        """ Import a Vtex record """
        with backend.work_on(self._name) as work:
            importer = work.component(usage='record.importer')
            return importer.run(external_id, record_data)

    @job(default_channel='root.vtex')
    @api.model
    def import_batch(self, backend, filters=None):
        """ Prepare the import of records modified on Vtex """
        if filters is None:
            filters = {}
        with backend.work_on(self._name) as work:
            importer = work.component(usage='batch.importer')
            return importer.run(filters=filters)

    @job(default_channel='root.vtex')
    @api.multi
    def export_record(self):
        self.ensure_one()
        with self.backend_id.work_on(self._name) as work:
            exporter = work.component(usage='record.exporter')
            return exporter.run(self)
        
    @job(default_channel='root.vtex')
    def export_delete_record(self, backend_id, external_id):
        """ Delete a record on Vtex """
        with backend_id.work_on(self._name) as work:
            deleter = work.component(usage='record.exporter.deleter')
            return deleter.run(external_id)
