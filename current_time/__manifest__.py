# -*- coding: utf-8 -*-
{
    'name': "Current Time",

    'summary': """
        Show Current Time""",

    'description': """
        Show Current Time with seconds can be shown on the top-left corner of
        the Odoo Screen.""",

    'author': "Shivam",
    'website': "",

    'category': 'web',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': {
            '/current_time/static/src/js/current_timer.js',
            '/current_time/static/src/js/automate_current_timer.js',
            '/current_time/static/src/scss/timer.scss',
        },
        'web.assets_qweb': {
            '/current_time/static/src/xml/current_time.xml',
        },
    },
}
