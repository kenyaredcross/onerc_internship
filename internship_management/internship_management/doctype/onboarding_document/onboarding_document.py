# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class OnboardingDocument(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		document: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		remarks: DF.SmallText | None
		submitted: DF.Check
		verified: DF.Check
		verified_by: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Onboarding Document"
