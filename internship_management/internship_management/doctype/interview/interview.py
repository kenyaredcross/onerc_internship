# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class Interview(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from internship_management.internship_management.doctype.interview_panel.interview_panel import InterviewPanel

		applicant: DF.Data | None
		communication: DF.Int | None
		confidence: DF.Int | None
		decision: DF.Literal["Scheduled", "Completed", "Selected", "Not Selected"]
		intern_profile: DF.Link | None
		interview_date: DF.Date | None
		interview_panel: DF.Table[InterviewPanel]
		interview_panel_chair: DF.Data | None
		interview_type: DF.Literal["In Person", "Online", "Phone"]
		overall_rating: DF.Int | None
		problem_solving: DF.Int | None
		professionalism: DF.Int | None
		recommendation: DF.SmallText | None
		registration: DF.Data | None
		remarks: DF.SmallText | None
		result: DF.Literal["Pass", "Fail", "Pending"]
		technical_knowledge: DF.Int | None
		time: DF.Time | None
		venue: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Interview"

	def validate(self):
		"""Basic validation for the Interview assessment."""
		if (
			self.communication
			and self.technical_knowledge
			and self.confidence
			and self.professionalism
			and self.problem_solving
		):
			self.overall_rating = round(
				(
					self.communication
					+ self.technical_knowledge
					+ self.confidence
					+ self.professionalism
					+ self.problem_solving
				)
				/ 5
			)

