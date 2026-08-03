# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InternshipExpectations(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		additional_comment: DF.SmallText | None
		career_objective: DF.SmallText | None
		learning_expectation: DF.SmallText | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		skill_to_acquire: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Internship Expectations"
