// Copyright (c) 2026, sumeya bishar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Onboarding Process", {
	refresh(frm) {
		if (frm.doc.__islocal || !frm.doc.intern) {
			return;
		}

		// Internship Progress buttons — create Work Log / Task / Evaluation for this intern
		frm.add_custom_button(
			__("New Work Log"),
			function() {
				frappe.new_doc("Work Log", {
					intern: frm.doc.intern,
					intern_full_name: frm.doc.intern_full_name,
					supervisor: frm.doc.supervisor,
					department: frm.doc.department,
					onboarding_process: frm.doc.name
				});
			},
			__("Internship Progress")
		);

		frm.add_custom_button(
			__("New Assigned Task"),
			function() {
				frappe.new_doc("Assigned Task", {
					intern: frm.doc.intern,
					intern_full_name: frm.doc.intern_full_name,
					assigned_by: frm.doc.supervisor,
					department: frm.doc.department,
					onboarding_process: frm.doc.name
				});
			},
			__("Internship Progress")
		);

		frm.add_custom_button(
			__("New Evaluation"),
			function() {
				frappe.new_doc("Evaluation", {
					intern: frm.doc.intern,
					supervisor: frm.doc.supervisor,
					onboarding_process: frm.doc.name
				});
			},
			__("Internship Progress")
		);
	},

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

					// Auto-fetch intern details from Intern Profile (read-only)
					frm.set_value("intern_full_name", profile.full_name || "");
					frm.set_value("institution", profile.school_information);
					frm.set_value("course", profile.course);
					frm.set_value("county", profile.county);
					frm.set_value("region", profile.region);
					frm.set_value("email", profile.email_address);
					frm.set_value("phone", profile.phone_number);
					frm.set_value("internship_category", profile.internship_type);
					frm.set_value("start_date", profile.internship_start_date);
					frm.set_value("end_date", profile.internship_end_date);

					// Populate documents from the Intern Profile's uploaded documents
					populate_documents(frm, profile);

					frm.refresh_field("intern_full_name");
					frm.refresh_field("institution");
					frm.refresh_field("course");
					frm.refresh_field("county");
					frm.refresh_field("region");
					frm.refresh_field("email");
					frm.refresh_field("phone");
					frm.refresh_field("internship_category");
					frm.refresh_field("start_date");
					frm.refresh_field("end_date");
					frm.refresh_field("documents");
				}
			}
		});
	}
});

function populate_documents(frm, profile) {
	// Define the mapping of required documents to their field on the Intern Profile
	const document_map = [
		{ label: "National ID / Passport Copy", field: "national_id__passport_copy" },
		{ label: "Curriculum Vitae (CV)", field: "curriculum_vitae_cv" },
		{ label: "Application Letter", field: "application_letter" },
		{ label: "Institution Letter", field: "school_introduction_letter" },
		{ label: "Insurance Cover", field: "insurance_cover" },
		{ label: "Academic Transcript", field: "academic_transcript" },
		{ label: "Student ID Copy", field: "student_id_copy" },
		{ label: "Other Supporting Documents", field: "other_supporting_documents" }
	];

	// Clear existing documents only if adding fresh (avoid duplicates on re-selection)
	frm.clear_table("documents");

	document_map.forEach(function(doc) {
		const submitted = profile[doc.field] ? 1 : 0;
		const row = frm.add_child("documents", {
			document: doc.label,
			submitted: submitted
		});
		frm.fields_dict.documents.grid.refresh_row(row);
	});

	frm.refresh_field("documents");
}
