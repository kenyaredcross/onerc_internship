// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Intern Profile", {
	refresh(frm) {
		// specify_institution and specify_course are now optional Data fields
		// that are always visible alongside the Institution/Course Link fields.

		if (frm.doc.__islocal) {
			return;
		}

		frm.clear_custom_buttons();

		if (frm.doc.onboarding_process) {
			// Onboarding Process already exists -> provide navigation
			frm.add_custom_button(
				__("View Onboarding Process"),
				function() {
					frappe.set_route("Form", "Onboarding Process", frm.doc.onboarding_process);
				},
				__("Onboarding")
			);
		} else {
			// No Onboarding Process -> allow creating the flow
			frm.add_custom_button(
				__("Create Onboarding Process"),
				function() {
					frappe.call({
						method: "frappe.client.insert",
						args: {
							doc: {
								doctype: "Onboarding Process",
								intern: frm.doc.name,
								intern_full_name: frm.doc.full_name,
								institution: frm.doc.school_information,
								course: frm.doc.course,
								county: frm.doc.county,
								region: frm.doc.region,
								email: frm.doc.email_address,
								phone: frm.doc.phone_number,
								internship_category: frm.doc.internship_type,
								start_date: frm.doc.internship_start_date,
								end_date: frm.doc.internship_end_date
							}
						},
						callback: function(r) {
							if (r.message) {
								frm.set_value("onboarding_process", r.message.name);
								frm.save();
								frappe.set_route("Form", "Onboarding Process", r.message.name);
							}
						}
					});
				},
				__("Onboarding")
			);
		}
	},

	onboarding_process(frm) {
		frm.refresh();
	}
});
