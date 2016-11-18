// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Daily Bus Arrangement"] = {
	"filters": [
		{
			"fieldname":"customer",
			"label": __("Customer"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"start_date",
			"label": __("Start Date"),
			"fieldtype": "Date",
			"default": get_today()
		},
		{
			"fieldname":"end_date",
			"label": __("End Date"),
			"fieldtype": "Date",
			"default": get_today()
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nAssigned\nNot Assigned"
		}
	]
}
