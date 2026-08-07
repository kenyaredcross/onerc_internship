# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Evaluation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		approval_date: DF.Date | None
		areas_for_improvement: DF.SmallText | None
		attendance: DF.Int
		communication: DF.Int
		evaluation_period: DF.Data | None
		hr_approval: DF.Check
		initiative: DF.Int
		intern: DF.Link
		learning_ability: DF.Int
		onboarding_process: DF.Link | None
		overall: DF.Int
		overall_rating: DF.Literal["Excellent", "Good", "Fair", "Poor"]
		problem_solving: DF.Int
		professionalism: DF.Int
		punctuality: DF.Int
		quality_of_work: DF.Int
		recommendation: DF.Literal["Excellent", "Good", "Fair", "Poor"]
		status: DF.Literal["Draft", "Completed"]
		strengths: DF.SmallText | None
		supervisor: DF.Data | None
		supervisor_approval: DF.Check
		teamwork: DF.Int
		technical_skills: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Evaluation"

	def validate(self):
		"""Link this Evaluation to the intern's Onboarding Process."""
		if self.intern:
			profile = frappe.get_cached_doc("Intern Profile", self.intern)
			if profile.onboarding_process:
				self.onboarding_process = profile.onboarding_process

	def validate_ratings(self):
		"""Basic validation for the Evaluation performance."""
		ratings = [
			self.attendance,
			self.punctuality,
			self.communication,
			self.teamwork,
			self.initiative,
			self.technical_skills,
			self.problem_solving,
			self.quality_of_work,
			self.professionalism,
			self.learning_ability,
		]

		valid = [r for r in ratings if r]
		if valid:
			self.overall = round(sum(valid) / len(valid))
