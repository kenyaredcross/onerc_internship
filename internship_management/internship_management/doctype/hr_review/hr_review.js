// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on('HR Review', {
	// refresh: function(frm) {

	// }

	intern: function (frm) {
		if (frm.doc.intern) {
			frappe.call({
				method: "frappe.client.get",
				args: {
					doctype: "Intern Profile",
					name: frm.doc.intern
				},
				callback: function (r) {
					if (!r.exc && r.message) {
						let d = r.message;
						frm.set_value("full_name", d.full_name);
						frm.set_value("email", d.email_address);
						frm.set_value("phone", d.phone_number);
					}
				}
			});
		}
	}
});
