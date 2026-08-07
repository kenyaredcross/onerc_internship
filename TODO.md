# Fix: "Intern should be indexed because it's referred in dashboard connections"

## Root Cause
- Frappe's `DocType.validate()` → `check_indexing_for_dashboard_links()` requires any `Link` field
  referenced in another doctype's dashboard connections (`links` table) to be indexed
  (`search_index: 1`) unless it is `unique`.
- The `intern` Link field on Work Log, Assigned Task, Evaluation, Intern Clearance, and
  Intern Exit Interview is neither unique nor indexed.
- Additionally, Onboarding Process and Intern Clearance are linked doctypes that are NOT
  submittable, so they cannot be submitted.

## Steps
- [x] 1. Add `search_index: 1` to the `intern` field in Work Log
- [x] 2. Add `search_index: 1` to the `intern` field in Assigned Task
- [x] 3. Add `search_index: 1` to the `intern` field in Evaluation
- [x] 4. Add `search_index: 1` to the `intern` field in Intern Clearance
- [x] 5. Add `search_index: 1` to the `intern` field in Intern Exit Interview
- [x] 6. Add `is_submittable: 1` + `submit: 1` permission to Onboarding Process
- [x] 7. Add `is_submittable: 1` + `submit: 1` permission to Intern Clearance
- [x] 8. Add `on_submit`/`on_cancel` handlers to Onboarding Process and Intern Clearance controllers
- [ ] 9. Run `bench --site internship.localhost migrate`
- [ ] 10. Run `bench --site internship.localhost clear-cache` and verify the alert is gone
