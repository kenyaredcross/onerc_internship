# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class OnboardingResource(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.Data | None
		issued_date: DF.Date | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		resource_type: DF.Literal["Laptop", "Access Card", "Other"]
		returned: DF.Check
		serial_number: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Onboarding Resource"
