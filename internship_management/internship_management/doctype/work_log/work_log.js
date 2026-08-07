// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Work Log", {
	intern(frm) {
		if (!frm.doc.intern) {
			return;
		}

		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Intern Profile",
				name: frm.doc.intern
			},
			callback: function(r) {
				if (r.message) {
					frm.set_value("department", r.message.assigned_department);
					frm.set_value("onboarding_process", r.message.onboarding_process || "");
					frm.refresh_field("department");
					frm.refresh_field("onboarding_process");
				}
			}
		});
	},

	refresh(frm) {
		if (frm.doc.intern) {
			frappe.call({
				method: "frappe.client.get_list",
				args: {
					doctype: "Onboarding Process",
					filters: {
						intern: frm.doc.intern
					},
					fields: ["supervisor", "name"],
					limit_page_length: 1
				},
				callback: function(r) {
					if (r.message && r.message.length) {
						frm.set_value("supervisor", r.message[0].supervisor);
						frm.set_value("onboarding_process", r.message[0].name);
						frm.refresh_field("supervisor");
						frm.refresh_field("onboarding_process");
					}
				}
			});
		}
	}
});
