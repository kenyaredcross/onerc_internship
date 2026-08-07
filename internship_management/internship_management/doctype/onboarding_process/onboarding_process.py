# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class OnboardingProcess(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from internship_management.internship_management.doctype.onboarding_document.onboarding_document import OnboardingDocument
		from internship_management.internship_management.doctype.onboarding_resource.onboarding_resource import OnboardingResource

		access_granted_date: DF.Date | None
		code_of_conduct_signed: DF.Check
		confidentiality_agreement_signed: DF.Check
		county: DF.Data | None
		course: DF.Link | None
		department: DF.Link | None
		documents: DF.Table[OnboardingDocument]
		email: DF.Data | None
		email_address: DF.Data | None
		email_created: DF.Check
		employee_number: DF.Data | None
		end_date: DF.Date | None
		hr_approval: DF.Check
		hr_officer: DF.Link | None
		ict_policy_accepted: DF.Check
		institution: DF.Link | None
		intern: DF.Link
		intern_full_name: DF.Data | None
		internship_category: DF.Data | None
		onboarding_complete: DF.Check
		orientation_completed: DF.Check
		orientation_conducted_by: DF.Link | None
		orientation_date: DF.Date | None
		orientation_notes: DF.SmallText | None
		other_systems: DF.SmallText | None
		phone: DF.Data | None
		region: DF.Data | None
		remarks: DF.SmallText | None
		reporting_date: DF.Date | None
		resources: DF.Table[OnboardingResource]
		safety_policy_accepted: DF.Check
		signature_date: DF.Date | None
		start_date: DF.Date | None
		status: DF.Literal["Pending", "In Progress", "Completed", "Cancelled"]
		supervisor: DF.Data | None
		supervisor_approval: DF.Check
		workstation: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Onboarding Process"

	def validate(self):
		"""Validation logic for the Onboarding Process."""
		self.validate_intern()
		self.validate_unique_onboarding()
		self.validate_onboarding_complete()

	def after_insert(self):
		"""Link this Onboarding Process back to the Intern Profile."""
		self.update_intern_profile_link()

	def on_update(self):
		"""Keep the Intern Profile's onboarding_process link in sync."""
		if self.intern:
			self.update_intern_profile_link()

	def on_submit(self):
		"""When the Onboarding Process is submitted, mark it as complete."""
		self.status = "Completed"
		self.onboarding_complete = 1

	def on_cancel(self):
		"""When the Onboarding Process is cancelled, reset the status."""
		self.status = "Cancelled"
		self.onboarding_complete = 0

	def update_intern_profile_link(self):
		"""Set the intern's `onboarding_process` field to this Onboarding Process."""
		if not self.intern:
			return

		profile = frappe.get_doc("Intern Profile", self.intern)
		if profile.onboarding_process != self.name:
			profile.db_set("onboarding_process", self.name)
			frappe.msgprint(
				_("Linked to Onboarding Process {0} on Intern Profile {1}").format(
					self.name, self.intern
				),
				alert=True,
			)

	def validate_intern(self):
		"""Ensure an Intern is selected."""
		if not self.intern:
			frappe.throw(_("Please select an Intern."))

	def validate_unique_onboarding(self):
		"""Ensure only one Onboarding Process exists per Intern."""
		if self.get("__islocal") or not self.name:
			return

		existing = frappe.get_all(
			"Onboarding Process",
			filters={"intern": self.intern, "name": ["!=", self.name]},
			fields=["name"],
			limit=1,
		)

		if existing:
			frappe.throw(
				_(
					"An Onboarding Process already exists for this Intern: {0}".format(
						existing[0].name
					)
				)
			)

	def validate_onboarding_complete(self):
		"""When Onboarding Complete is checked, validate prerequisites and set Status."""
		if not self.onboarding_complete:
			return

		if not self.orientation_completed:
			frappe.throw(_("Orientation must be completed before onboarding can be marked complete."))

		if not self.hr_approval:
			frappe.throw(_("HR Approval is required before onboarding can be marked complete."))

		self.status = "Completed"

