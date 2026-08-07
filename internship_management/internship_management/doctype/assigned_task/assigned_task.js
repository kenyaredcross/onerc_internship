// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assigned Task', {
	// refresh: function(frm) {

	// }

	intern: function (frm) {
		if (frm.doc.intern) {
			frappe.call({
				method: "frappe.client.get",
				args: { doctype: "Intern Profile", name: frm.doc.intern },
				callback: function (r) {
					if (!r.exc && r.message) {
						frm.set_value("intern_full_name", r.message.full_name);
						frm.set_value("department", r.message.assigned_department);
						frm.set_value("onboarding_process", r.message.onboarding_process || "");
						frm.refresh_field("department");
						frm.refresh_field("onboarding_process");
					}
				}
			});
		}
	},

	refresh: function (frm) {
		if (frm.doc.intern) {
			frappe.call({
				method: "frappe.client.get_list",
				args: {
					doctype: "Onboarding Process",
					filters: { intern: frm.doc.intern },
					fields: ["supervisor", "name"],
					limit_page_length: 1
				},
				callback: function (r) {
					if (r.message && r.message.length) {
						if (!frm.doc.supervisor) {
							frm.set_value("assigned_by", r.message[0].supervisor);
						}
						frm.set_value("onboarding_process", r.message[0].name);
						frm.refresh_field("assigned_by");
						frm.refresh_field("onboarding_process");
					}
				}
			});
		}
	}
});
