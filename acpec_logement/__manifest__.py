# -*- coding: utf-8 -*-
{
	'name': "acpec_logement",
	'summary': """Rapports sur le logemen""",
	'description': "Long description of module's purpose",
	'author': "ACPEC SARL",
	'website': "https://www.acpec-sarl.com",
	'category': 'Uncategorized',
	'version': '0.1',

	# any module necessary for this one to work correctly
	'depends': ['account', 'sale_subscription'],

	# always loaded
	'data': [
		'security/ir.model.access.csv',
		'security/groups.xml',
		'wizards/wizard_view.xml',
		'views/inherit_account_move.xml',
		'reports/report.xml',
	],
	'installable': True,
	'application': True,
	'auto_install': False,
	'license': 'LGPL-3',
}
