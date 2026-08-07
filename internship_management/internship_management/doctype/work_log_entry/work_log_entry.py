# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class WorkLogEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		activities_done: DF.SmallText | None
		attendance_status: DF.Literal["Present", "Absent", "Leave", "Holiday"]
		challenges: DF.SmallText | None
		check_in: DF.Time | None
		check_out: DF.Time | None
		date: DF.Date | None
		day: DF.Data | None
		hours_worked: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		skills_learned: DF.SmallText | None
		supervisor_comment: DF.SmallText | None
		task_assigned: DF.SmallText | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Work Log Entry"

