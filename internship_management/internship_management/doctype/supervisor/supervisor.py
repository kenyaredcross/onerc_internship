# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Supervisor(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email_address: DF.Data | None
		gender: DF.Literal["Female", "Male", "Other"]
		institution: DF.Link | None
		phone_number: DF.Data | None
		salutation: DF.Literal["Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "Rev.", "Eng.", "Other"]
		school_department: DF.Data | None
		supervisor_name: DF.Data | None
		title: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Supervisor"
