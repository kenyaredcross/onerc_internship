# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InternProfile(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from internship_management.internship_management.doctype.internship_expectations.internship_expectations import InternshipExpectations

		academic_transcript: DF.Attach | None
		active: DF.Check
		amended_from: DF.Link | None
		assigned_department: DF.Link | None
		county: DF.Link | None
		course: DF.Link
		current_academic_level: DF.Literal["Certificate", "Diploma", "Higher Diploma", "Bachelor's Degree", "Postgraduate Diploma", "Master's Degree", "PhD", "Other"]
		curriculum_vitae_cv: DF.Attach | None
		date_of_birth: DF.Date | None
		email_address: DF.Data
		emergency_contact_name: DF.Data | None
		emergency_contact_phone_number: DF.Data | None
		emergency_email_address: DF.Data | None
		expected_graduation_date: DF.Date | None
		first_name: DF.Data
		gender: DF.Literal["Female", "Male", "Others"]
		insurance_cover: DF.Attach | None
		internship_end_date: DF.Date | None
		internship_expectations: DF.Table[InternshipExpectations]
		internship_start_date: DF.Date | None
		internship_type: DF.Literal["Industrial Attachment", "Internship", "Community Service"]
		last_name: DF.Data
		national_id__passport_copy: DF.Attach | None
		national_idpassport_number: DF.Data | None
		office: DF.Data | None
		other_supporting_documents: DF.Attach | None
		phone_number: DF.Data
		physical_address: DF.SmallText | None
		region: DF.Data | None
		relationship: DF.Data | None
		school_information: DF.Link
		school_introduction_letter: DF.Attach | None
		start_date_of_study: DF.Date | None
		status: DF.Literal["Pending", "Assigned", "Active", "Completed", "Terminated"]
		student_id_copy: DF.Attach | None
		supervisor: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Intern Profile"
