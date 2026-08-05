// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Intern Exit Interview", {
	intern: function(frm) {
		if (frm.doc.intern) {
			frappe.call({
				method: "frappe.client.get_value",
				args: {
					doctype: "Intern Profile",
					filters: { "name": frm.doc.intern },
					fieldname: [
						"full_name",
						"assigned_department",
						"internship_start_date",
						"internship_end_date"
					]
				},
				callback: function(r) {
					if (r.message) {
						frappe.model.set_value(frm.doctype, frm.docname, "full_name", r.message.full_name);
						frappe.model.set_value(frm.doctype, frm.docname, "department", r.message.assigned_department);
						frappe.model.set_value(frm.doctype, frm.docname, "internship_start_date", r.message.internship_start_date);
						frappe.model.set_value(frm.doctype, frm.docname, "internship_end_date", r.message.internship_end_date);
					}
				}
			});
		} else {
			// Clear fetched fields when intern is removed
			["full_name", "department", "internship_start_date", "internship_end_date"].forEach(function(field) {
				frappe.model.set_value(frm.doctype, frm.docname, field, null);
			});
		}
	}
});
