# extend_account_invoice/__manifest__.py
{
    'name': 'Extend Account Invoice',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Adds sbu_jurnal dropdown to account.move',
    'author': 'handaru',
    'depends': ['account'],
    'data': [
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
}
