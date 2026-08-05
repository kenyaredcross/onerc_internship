# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InternExitInterview(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		career_path_and_support: DF.SmallText | None
		department: DF.Link | None
		full_name: DF.Data | None
		greatest_lesson_learned: DF.SmallText | None
		intern: DF.Link | None
		internship_challenges_and_improvements: DF.SmallText | None
		internship_end_date: DF.Date | None
		internship_expectations_match: DF.SmallText | None
		internship_experience_description: DF.SmallText | None
		internship_recommendation: DF.SmallText | None
		internship_start_date: DF.Date | None
		internship_strong_points: DF.SmallText | None
		interview_date: DF.Date | None
		most_challenging_experience: DF.SmallText | None
		most_rewarding_experience: DF.SmallText | None
		pre_internship_expectations: DF.SmallText | None
		skills_techniques_and_knowledge_gained: DF.SmallText | None
		suggested_changes: DF.SmallText | None
		training_and_mentoring_feedback: DF.SmallText | None
		unit: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Intern Exit Interview"
