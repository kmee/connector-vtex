# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Connector Vtex',
    'summary': """
        Connector Odoo with Vtex""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'KMEE,Odoo Community Association (OCA)',
    'website': 'https://www.kmee.com.br',
    'depends': [
        "account",
        "product",
        "product_multi_category",  # oca/product-attribute
        "connector_ecommerce",  # oca/connector-ecommerce
        "product_brand",
        # "base_multi_image",  # oca/server-tools # not migrated yet
    ],
    "external_dependencies": {
        'python': [
            "html2text",
            # tests dependencies
            "freezegun",
            "vcr",
            "bs4",
        ],
    },
    'data': [
        'security/vtex_backend.xml',

        'wizards/wizard_vtex_product_category.xml',
        'wizards/wizard_vtex_product_brand.xml',

        'views/vtex_mixin.xml',
        'views/vtex_backend.xml',
        'views/vtex_menu.xml',
    ],
    'demo': [
        'demo/vtex_backend.xml',
    ],
}
