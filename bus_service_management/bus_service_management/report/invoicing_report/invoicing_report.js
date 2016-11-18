// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Invoicing Report"] = {
	"filters": [
		{
			"fieldname":"customer",
			"label": __("Customer"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"billing_month",
			"label": __("Billing Month"),
			"fieldtype": "Select",
			"options": "\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember",
			"default": ["nJanuary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", 
				"December"][frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth()],
		}
	]
}
