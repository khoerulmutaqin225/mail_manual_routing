# -*- coding: utf-8 -*-
{
    'name': "Lost Messages Routing",
    'summary': "Manage and route lost incoming messages in Odoo, ensuring no message is missed and enhancing client satisfaction.",
    'description': """
        Lost Messages Routing module helps manage messages that Odoo fails to address, 
        such as when a customer sends a direct email to a catchall address. 
        This tool captures those messages and allows users to attach them to the appropriate 
        document thread, preventing lost communications and improving customer experience.
    """,
    'author': "KHOERUL MUTAQIN",
    'website': "https://www.doodex.net",
    'category': 'Mail',
    'version': '17.0',
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'images': [
        'static/description/icon.png'
    ],    
    # only loaded in demonstration mode
}

