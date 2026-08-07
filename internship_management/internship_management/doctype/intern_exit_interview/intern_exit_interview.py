# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class InternExitInterview(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		career_path_and_support: DF.SmallText | None
		certificate_recommended: DF.Check
		communication: DF.Int | None
		department: DF.Link | None
		eligible_for_future_opportunities: DF.Check
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
		interviewed_by: DF.Data | None
		learning_experience: DF.Int | None
		most_challenging_experience: DF.SmallText | None
		most_rewarding_experience: DF.SmallText | None
		orientation: DF.Int | None
		overall_satisfaction: DF.Int | None
		pre_internship_expectations: DF.SmallText | None
		remarks: DF.SmallText | None
		resources: DF.Int | None
		skills_techniques_and_knowledge_gained: DF.SmallText | None
		status: DF.Literal["Pending", "Completed"]
		suggested_changes: DF.SmallText | None
		supervision: DF.Int | None
		training_and_mentoring_feedback: DF.SmallText | None
		unit: DF.Data | None
		work_environment: DF.Int | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Intern Exit Interview"
