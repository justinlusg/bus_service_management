# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import datetime,timedelta
from frappe.utils import flt, getdate, today

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns(filters)
	data = get_data(filters)
	
	return columns,data
	
def get_columns(filters):
	columns = [_("Transport Order No") + "::100",_("Customer") + "::100",_("Origin") + "::100",_("Destination") + "::100",
		_("Type of Trip") + "::100",_("Date & Time") + "::100",_("Driver Name") + "::100",_("Driver Mobile") + "::100",_("Bus Capacity") + "::100"]
		
	return columns

def get_conditions(filters):
	conditions = ""
	if filters.get("start_date") and filters.get("end_date"):
		conditions += "and toi.date_n_time >= '%s' and toi.date_n_time <= '%s'" % (frappe.db.escape(filters["start_date"]), frappe.db.escape(filters["end_date"]))

	if filters.get("status"):
		if filters.get("status")=='Assigned':
			conditions += "and toi.driver_name != ''"
		elif filters.get("status")=='Not Assigned':
			conditions += "and toi.driver_name = ''"

	if not filters.get("start_date"):
		frappe.throw(_("Start Date is required"))
	if not filters.get("end_date"):
		frappe.throw(_("End Date is required"))

	if filters.get("customer"):
		conditions += " and customer = '%s'" % (frappe.db.escape(filters["customer"]))

	return conditions

def get_data(filters):
	conditions = get_conditions(filters)
	to_list = get_to_list(filters)
	data = []

	for li in to_list:
		data.append([li.transport_order_no,li.customer,li.origin,li.destination,li.type_of_trip,li.date_n_time,li.driver_name,li.driver_mobile,li.bus_capacity])

	return data

def get_to_list(filters):
	conditions = get_conditions(filters)
	
	to_list = frappe.db.sql("""select tr.transport_order_no, tr.customer, toi.origin, toi.destination, toi.type_of_trip, toi.date_n_time, toi.driver_name, toi.driver_mobile, toi.bus_capacity from `tabTransport Orders` tr, `tabTransport Order Item` toi where tr.name=toi.parent %s""" % (conditions), as_dict=1)

	return to_list
