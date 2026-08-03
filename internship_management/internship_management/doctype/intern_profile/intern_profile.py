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

		academic_transcript: DF.Attach | None
		amended_from: DF.Link | None
		assigned_branch: DF.Link | None
		assigned_department: DF.Link | None
		curriculum_vitae_cv: DF.Attach | None
		email_address: DF.Data | None
		emergency_contact_name: DF.Data | None
		emergency_contact_phone_number: DF.Data | None
		expected_graduation_date: DF.Date | None
		first_name: DF.Data
		gender: DF.Literal["Female", "Male", "Others"]
		insurance_cover: DF.Attach | None
		internship_end_date: DF.Date | None
		internship_start_date: DF.Date | None
		internship_type: DF.Literal["Internship", "Industrial Attachment"]
		last_name: DF.Data | None
		national_id__passport_copy: DF.Attach | None
		other_supporting_documents: DF.Attach | None
		phone_number: DF.Data | None
		physical_address: DF.SmallText | None
		school_introduction_letter: DF.Attach | None
		start_date_of_study: DF.Date | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Intern Profile"
