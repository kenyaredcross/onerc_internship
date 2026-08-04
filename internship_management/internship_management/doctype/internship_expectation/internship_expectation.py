# Copyright (c) 2026, sumeya bishar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InternshipExpectation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from internship_management.internship_management.doctype.additional_comment.additional_comment import AdditionalComment
		from internship_management.internship_management.doctype.career_objective.career_objective import CareerObjective
		from internship_management.internship_management.doctype.learning_expectation.learning_expectation import LearningExpectation
		from internship_management.internship_management.doctype.skill_to_acquire.skill_to_acquire import SkilltoAcquire

		additional_comments: DF.Table[AdditionalComment]
		career_objective: DF.Table[CareerObjective]
		learning_expectation: DF.Table[LearningExpectation]
		skills_to_acquire: DF.Table[SkilltoAcquire]
	# end: auto-generated types

	_DOCTYPE_NAME = "Internship Expectation"
