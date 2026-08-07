// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Interview", {
	intern_profile(frm) {
		if (!frm.doc.intern_profile) {
			return;
		}

		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype: "Intern Profile",
				name: frm.doc.intern_profile
			},
			callback: function(r) {
				if (r.message) {
					frm.set_value("applicant", r.message.full_name || r.message.name);
					frm.refresh_field("applicant");
				}
			}
		});
	}
});
