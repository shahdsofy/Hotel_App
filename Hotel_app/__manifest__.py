# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hotel',
    'category': 'Accounting',
    'summary': 'Manage my Hotel',
    'description': "",
    'sequence':-115,
    'version': '1.0',
    'depends': ['mail'],
    'data': [
        'security/security_access.xml',
        # 'security/ir.model.access.csv'
        'views/customer_views.xml',
        'views/room_views.xml',
        'views/booking_views.xml',
        'views/hotel_payment.xml',
        'views/credit_view.xml',
        'views/cash_view.xml',
        'data/import_data.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
