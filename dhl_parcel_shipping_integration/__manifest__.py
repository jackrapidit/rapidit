# -*- coding: utf-8 -*-pack
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{

    # App information
    'name': 'DHL Parcel(UK) Shipping Integration',
    'category': 'Website',
    'version': '14.0.04.08.21',
    'summary': '',
    'license': 'OPL-1',

    # Dependencies
    'depends': ['delivery'],

    # Views
    'data': [
        'view/res_company.xml',
        'view/delivery_carrier_view.xml',
        'view/stock_picking_view.xml',
        'view/res_country.xml',
        'data/dhl_parcel_credential_cron.xml'
    ],



    # Odoo Store Specific
    'images': ['static/description/cover.jpg'],

    # Author
    'author': 'Vraja Technologies',
    'website': 'http://www.vrajatechnologies.com',
    'maintainer': 'Vraja Technologies',

    # Technical
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'live_test_url': 'http://www.vrajatechnologies.com/contactus',
    'price': '99',
    'currency': 'EUR',

}
# version changelog
# 12.0.23.02.2020 Intial Version Of the App
# 14.0.02.07.201 Custome Changes In stock.picking.batch Given By Client(Tested By : Shyam and Mithilesh)
# 14.0.07.7.21 fix some issue
# without batch process
# 14.0.04.08.21 fix authentication issue
