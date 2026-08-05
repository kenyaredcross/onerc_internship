# TODO: Intern Exit Interview & Related Changes

## Steps
- [x] Analyze current state of files
- [x] Get user confirmation on plan

## Implementation Ordered by Dependency

### 1. Create Unit doctype (needed for `unit` Link field)
- [x] Create `unit/__init__.py`
- [x] Create `unit/unit.json`
- [x] Create `unit/unit.py`

### 2. Update Intern Exit Interview doctype
- [x] Fix missing `column_break_ouza` field and two-column layout in `intern_exit_interview.json`
- [x] Update `intern_exit_interview.py` auto-generated types
- [x] Update `intern_exit_interview.js` client script for fetch (`assigned_department`)

### 3. Update Intern Profile doctype types
- [x] Update `intern_profile.py` auto-generated types (workspace_supervisor, institution_supervisor, full_name)

### 4. Post-edits
- [x] Run `bench migrate` (doctype sync succeeded; failed later on unrelated HRMS fixture `job_opening_template`)
- [x] Verify intern_profile.py and intern_exit_interview.py compile cleanly
- [ ] Verify doctype renders with both tabs in the UI
