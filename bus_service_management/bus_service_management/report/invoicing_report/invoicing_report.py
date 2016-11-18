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
	columns = [_("Transport Order No") + "::100",_("Billing Month") + "::100",_("Customer") + "::100",_("Rate") + "::100",
		_("Billed") + "::100",_("Bill To") + "::100",_("Invoice Number") + "::100"]
		
	return columns

def get_conditions(filters):
	conditions = ""
	if filters.get("billing_month"):
		conditions += "and billing_month = '%s'" % frappe.db.escape(filters["billing_month"])
	

	if not filters.get("billing_month"):
		frappe.throw(_("Billing Month is required"))

	if filters.get("customer"):
		conditions += " and customer = '%s'" % filters["customer"]

	return conditions

def get_data(filters):
	conditions = get_conditions(filters)
	to_list = get_to_list(filters)
	data = []

	for li in to_list:
		data.append([li.transport_order_no, li.billing_month, li.customer, li.rate, li.billed, li.bill_to, li.invoice_number])

	return data

def get_to_list(filters):
	conditions = get_conditions(filters)
	
	to_list = frappe.db.sql("""select tr.transport_order_no, tr.billing_month, tr.customer, sum(toi.rate) as rate, tr.billed, tr.bill_to, tr.invoice_number from `tabTransport Orders` tr, `tabTransport Order Item` toi where tr.name=toi.parent %s""" % (conditions), as_dict=1)
	
	return to_list