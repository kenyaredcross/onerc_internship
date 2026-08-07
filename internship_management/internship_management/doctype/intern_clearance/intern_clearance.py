# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class InternClearance(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from internship_management.internship_management.doctype.clearance_checklist.clearance_checklist import ClearanceChecklist
		from internship_management.internship_management.doctype.intern_system_access.intern_system_access import InternSystemAccess

		agreement_accepted: DF.Check
		agreement_date: DF.Date | None
		clearance_checklist: DF.Table[ClearanceChecklist]
		clearance_status: DF.Literal["Pending", "Approved", "Rejected"]
		department: DF.Link | None
		designation: DF.Data | None
		email_account: DF.Literal["Deactivated", "Not Applicable", "Still Active"]
		email_address: DF.Data | None
		exit_interview: DF.Link | None
		full_name: DF.Data | None
		hod_date: DF.Date | None
		hod_signature: DF.Signature | None
		hr_approval: DF.Check
		i_declare_that_the_information_above_is_accurate_and_truth: DF.Check
		id_card: DF.Literal["Returned", "Not Applicable", "Not Returned"]
		intern: DF.Link | None
		intern_signature: DF.Signature | None
		internship_end_date: DF.Date | None
		internship_start_date: DF.Date | None
		laptop: DF.Literal["Returned", "Not Applicable", "Not Returned"]
		other_assets: DF.SmallText | None
		overall_status: DF.Literal["Pending", "Cleared", "Not Cleared"]
		phone_number: DF.Data | None
		positiontitle: DF.Data | None
		remarks: DF.SmallText | None
		signature_date: DF.Date | None
		supervisor_date: DF.Date | None
		supervisor_remarks: DF.SmallText | None
		supervisors_signature: DF.Signature | None
		system_access: DF.Table[InternSystemAccess]
	# end: auto-generated types

	_DOCTYPE_NAME = "Intern Clearance"

	def on_submit(self):
		"""When the Intern Clearance is submitted, mark it as cleared."""
		self.overall_status = "Cleared"
		self.clearance_status = "Approved"

	def on_cancel(self):
		"""When the Intern Clearance is cancelled, reset the status."""
		self.overall_status = "Not Cleared"
		self.clearance_status = "Rejected"

