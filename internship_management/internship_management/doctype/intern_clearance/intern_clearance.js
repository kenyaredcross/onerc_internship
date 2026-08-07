// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Intern Clearance", {
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
					const profile = r.message;

					frm.set_value("full_name", profile.full_name);
					frm.set_value("positiontitle", profile.internship_type);
					frm.set_value("phone_number", profile.phone_number);
					frm.set_value("email_address", profile.email_address);
					frm.set_value("department", profile.assigned_department);
					frm.set_value("internship_start_date", profile.internship_start_date);
					frm.set_value("internship_end_date", profile.internship_end_date);

					frm.refresh_field("full_name");
					frm.refresh_field("positiontitle");
					frm.refresh_field("phone_number");
					frm.refresh_field("email_address");
					frm.refresh_field("department");
					frm.refresh_field("internship_start_date");
					frm.refresh_field("internship_end_date");
				}
			}
});
	},

	refresh(frm) {

	}
});
