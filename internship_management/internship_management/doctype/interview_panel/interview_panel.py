# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class InterviewPanel(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		department: DF.Link | None
		designation: DF.Data | None
		interviewer: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		signature: DF.Signature | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Interview Panel"
