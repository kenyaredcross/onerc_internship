# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WorkLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from internship_management.internship_management.doctype.work_log_entry.work_log_entry import WorkLogEntry

		approval_date: DF.Date | None
		approved_by: DF.Link | None
		challenges: DF.SmallText | None
		work_log_entries: DF.Table[WorkLogEntry]
		department: DF.Link | None
		intern: DF.Link
		month: DF.Data | None
		next_week_plan: DF.SmallText | None
		onboarding_process: DF.Link | None
		remarks: DF.SmallText | None
		status: DF.Literal["Draft", "Submitted", "Approved"]
		supervisor: DF.Link | None
		week: DF.Data | None
		weekly_achievement: DF.SmallText | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Work Log"

	def validate(self):
		"""Link this Work Log to the intern's Onboarding Process."""
		if self.intern:
			profile = frappe.get_cached_doc("Intern Profile", self.intern)
			if profile.onboarding_process:
				self.onboarding_process = profile.onboarding_process

