# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class HRReview(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		approval_date: DF.Date | None
		assigned_date: DF.Date | None
		assignment_remarks: DF.SmallText | None
		decision: DF.Literal["Pending", "Approved", "Rejected"]
		department: DF.Link | None
		email: DF.Data | None
		full_name: DF.Data | None
		hr_officer: DF.Link | None
		intern: DF.Link
		interview: DF.Link | None
		interview_required: DF.Check
		phone: DF.Data | None
		remarks: DF.SmallText | None
		review_date: DF.Date | None
		review_status: DF.Literal["Pending", "Under Review", "Reviewed"]
		reviewer: DF.Link | None
		selection_status: DF.Literal["Pending", "Selected", "Not Selected"]
		supervisor: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "HR Review"

	def validate(self):
		"""Validation logic for HR Review."""
		self.validate_unique_review()
		self.validate_interview_requirement()

	def validate_unique_review(self):
		"""Ensure one HR Review per intern."""
		if self.get("__islocal") or not self.name:
			return

		existing = frappe.get_all(
			"HR Review",
			filters={"intern": self.intern, "name": ["!=", self.name]},
			fields=["name"],
			limit=1,
		)
		if existing:
			frappe.throw(_("An HR Review already exists for this Intern: {0}".format(existing[0].name)))

	def validate_interview_requirement(self):
		"""Enforce interview requirement when selected."""
		if self.interview_required and not self.interview:
			frappe.throw(_("Interview is required. Please link an Interview record."))
