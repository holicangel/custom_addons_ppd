{
    'name': 'Extend Stock Picking',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Extend delivery slip report with a signature table',
    'depends': ['stock'],
    'data': [
	'views/form_picking_extend.xml',
        'report/stock_picking_report_template.xml',
	'report/report_action.xml',
    ],
    'installable': True,
    'application': False,
}
