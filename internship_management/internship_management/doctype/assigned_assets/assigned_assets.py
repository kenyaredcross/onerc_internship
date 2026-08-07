# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class AssignedAssets(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		asset: DF.Data | None
		condition: DF.Literal["Good", "Fair", "Poor", "New"]
		date_issued: DF.Date | None
		date_returned: DF.Date | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		serial_number: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Assigned Assets"
