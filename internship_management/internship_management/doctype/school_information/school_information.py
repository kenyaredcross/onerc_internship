# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SchoolInformation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		alternative_phone_number: DF.Data | None
		city__town: DF.Data | None
		email_address: DF.Data | None
		institution_code: DF.Data | None
		institution_name: DF.Data
		institution_type: DF.Literal["Private", "Public"]
		logo: DF.AttachImage | None
		phone_number: DF.Data | None
		physical_address: DF.SmallText | None
		postal_address: DF.Data | None
		registration_number: DF.Data | None
		website: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "School Information"
