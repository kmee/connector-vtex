# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging
from datetime import timedelta, date

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)


class VtexBackend(models.Model):
    _name = 'vtex.backend'
    _description = 'Vtex Backend'
    _inherit = 'connector.backend'

    @api.model
    def select_versions(self):
        """ Available versions in the backend.

        Can be inherited to add custom versions.  Using this method
        to add a version from an ``_inherit`` does not constrain
        to redefine the ``version`` field in the ``_inherit`` model.
        """
        return [('1.0', '1.0')]

    version = fields.Selection(selection='select_versions', required=True)
    name = fields.Char()
    app_key = fields.Char()
    app_token = fields.Char()
    environment = fields.Char()
    account_name = fields.Char()
    base_url = fields.Char(readonly=True)

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda x: x._get_default_company(),
        required=True
    )
    account_analytic_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic account',
        help='If specified, this analytic account will be used to fill the '
             'field  on the sale order created by the connector. The value can '
             'also be specified on the marketplace.'
    )
    fiscal_position_id = fields.Many2one(
        comodel_name='account.fiscal.position',
        string='Fiscal position',
        help='If specified, this fiscal position will be used to fill the '
             'field fiscal position on the sale order created by the connector.'
             'The value can also be specified on the marketplace.'
    )
    warehouse_id = fields.Many2one(
        comodel_name='stock.warehouse',
        string='Warehouse',
        # required=True,
        help='If specified, this warehouse will be used to fill the '
             'field warehouse on the sale order created by the connector.'
             'The value can also be specified on the marketplace.',
    )

    id_client = fields.Char('Vtex Id Client')

    import_orders_from_date = fields.Date('Import Orders from Date')
    import_customers_from_date = fields.Date('Import Customers from Date')
    import_categories_from_date = fields.Date('Import Categories from Date')
    import_products_from_date = fields.Date('Import Products from Date')
    import_brands_from_date = fields.Date('Import Brands from Date')

    def _get_default_company(self):
        return self.env.user.company_id

    @api.multi
    def synchronize_metadata(self):
        try:
            for backend in self:
                with backend.work_on('vtex.market.place') as work:
                    a = work.component(usage='batch.importer')
                    a.run()
            return True
        except Exception as e:
            _logger.error(e.message, exc_info=True)
            raise UserError(
                _(u"Check your configuration, we can't get the data. "
                  u"Here is the error:\n%s") %
                str(e).decode('utf-8', 'ignore'))

    #
    #  TODO: Refactor import methods
    #

    @api.multi
    def import_sale_orders(self, filters=None):
        if filters is None:
            filters = {}
        start_date = date.today() - timedelta(days=1)
        import_start_time = fields.Date.to_string(start_date)
        if self.import_orders_from_date:
            from_date = self.import_orders_from_date or None
        else:
            from_date = None
        if 'from_date' not in filters:
            filters['from_date'] = from_date
        if 'to_date' not in filters:
            filters['to_date'] = fields.Date.today()

        self.env['vtex.sale.order'].with_delay(priority=1).import_batch(
            self,
            filters=filters
        )
        self.write({'import_orders_from_date': import_start_time})

    @api.multi
    def import_categories(self, filters=None):
        if filters is None:
            filters = {}
        start_date = date.today() - timedelta(days=1)
        import_start_time = fields.Date.to_string(start_date)
        if self.import_categories_from_date:
            from_date = self.import_categories_from_date or None
        else:
            from_date = None
        if 'from_date' not in filters:
            filters['from_date'] = from_date
        if 'to_date' not in filters:
            filters['to_date'] = fields.Date.today()

        self.env['vtex.product.category'].with_delay(priority=1).import_batch(
            self,
            filters=filters
        )
        self.write({'import_categories_from_date': import_start_time})

    @api.multi
    def import_brands(self, filters=None):
        if filters is None:
            filters = {}
        start_date = date.today() - timedelta(days=1)
        import_start_time = fields.Date.to_string(start_date)
        if self.import_brands_from_date:
            from_date = self.import_brands_from_date or None
        else:
            from_date = None
        if 'from_date' not in filters:
            filters['from_date'] = from_date
        if 'to_date' not in filters:
            filters['to_date'] = fields.Date.today()

        self.env['vtex.product.brand'].with_delay(priority=1).import_batch(
            self,
            filters=filters
        )
        self.write({'import_brands_from_date': import_start_time})

    @api.multi
    def import_customers(self, filters=None):
        if filters is None:
            filters = {}
        start_date = date.today() - timedelta(days=1)
        import_start_time = fields.Date.to_string(start_date)
        if self.import_customers_from_date:
            from_date = self.import_customers_from_date or None
        else:
            from_date = None
        if 'from_date' not in filters:
            filters['from_date'] = from_date
        if 'to_date' not in filters:
            filters['to_date'] = fields.Date.today()

        self.env['vtex.sale.order'].with_delay(priority=1).import_batch(
            self,
            filters=filters
        )
        self.write({'import_customers_from_date': import_start_time})

    @api.model
    def _vtex_backend(self, callback, domain=None, filters=None):
        if domain is None:
            domain = []
        if filters is None:
            filters = {}
        backends = self.search(domain)
        if backends:
            getattr(backends, callback)(filters)

    @api.model
    def _scheduler_import_sale_orders(self, domain=None, filters=None):
        self._vtex_backend('import_sale_orders', domain=domain,
                           filters=filters)
