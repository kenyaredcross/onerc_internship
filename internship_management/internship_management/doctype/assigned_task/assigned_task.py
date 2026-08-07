# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class AssignedTask(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		assigned_by: DF.Data | None
		assigned_date: DF.Date | None
		completion_date: DF.Date | None
		department: DF.Link | None
		due_date: DF.Date | None
		feedback_date: DF.Date | None
		intern: DF.Link
		intern_full_name: DF.Data | None
		onboarding_process: DF.Link | None
		priority: DF.Literal["Low", "Medium", "High", "Urgent"]
		progress_percent: DF.Percent
		status: DF.Literal["Pending", "In Progress", "Completed", "Cancelled"]
		submitted_work: DF.Attach | None
		supervisor_feedback: DF.SmallText | None
		task_description: DF.SmallText | None
		task_title: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "Assigned Task"

	def validate(self):
		"""Link this Task to the intern's Onboarding Process and auto update status."""
		if self.intern:
			profile = frappe.get_cached_doc("Intern Profile", self.intern)
			if profile.onboarding_process:
				self.onboarding_process = profile.onboarding_process

		# Auto update status based on progress.
		if self.progress_percent >= 100:
			self.status = "Completed"
			if not self.completion_date:
				self.completion_date = frappe.utils.today()
		elif self.progress_percent > 0:
			if self.status == "Pending":
				self.status = "In Progress"
