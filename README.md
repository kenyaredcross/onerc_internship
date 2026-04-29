# OIV ONERC Intern & Volunteer Platform
> A custom Frappe application for managing ONERC interns and volunteers covering profile onboarding, weekly activity reporting, field mission documentation and timesheet tracking.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Module & App Registration](#module--app-registration)
- [DocTypes](#doctypes)
  - [User Profiles](#1-user-profiles)
  - [Weekly Reports](#2-weekly-reports)
  - [Weekly Activities](#3-weekly-activities-child-table)
  - [Mission Reports](#4-mission-reports)
  - [ONERC OIV Timesheet](#5-onerc-oiv-timesheet)
  - [Programme Posting](#6-programme-posting)
- [Roles & Permissions Summary](#roles--permissions-summary)
- [External DocType Dependencies](#external-doctype-dependencies)
- [Tooling & Code Quality](#tooling--code-quality)
- [Installation](#installation)
- [Contributing](#contributing)
- [Known Bugs & Incomplete Work](#known-bugs--incomplete-work)
- [License](#license)

---

## Overview

OIV digitises the intern and volunteer lifecycle at ONERC. It is built entirely on the Frappe framework and integrates with ERPNext's existing `Department`, `Employee` and `Job Opening` doctypes.

The platform supports four roles **Intern**, **Supervisor**, **HR Manager** and **System Manager** each with distinct access levels across six custom DocTypes.

At the time of writing the app is at **v0.0.1** and is in active early development. All Python controller files contain no logic (`pass` only), all JavaScript form files are fully commented out and all test files are empty stubs. The data models (DocType JSON schemas) are the most complete part of the codebase.

---

## Tech Stack

| Layer | Detail |
|---|---|
| Framework | Frappe Framework v15+ (managed by bench) |
| Backend language | Python ≥ 3.10 |
| Frontend | Frappe Desk (JS), Vue.js available via Frappe globals |
| Database | MariaDB InnoDB, Dynamic row format |
| Python linter/formatter | Ruff v0.8.1 (line-length 110, target py310) |
| JS linter | ESLint v8.44.0 (eslint:recommended, quiet mode) |
| JS formatter | Prettier v2.7.1 |
| Pre-commit | pre-commit-hooks v5.0.0 |
| Build backend | flit_core ≥3.4, <4 |

---

## Project Structure

```
oiv/                               # Bench app root
├── oiv/                           # Python package
│   ├── __init__.py                # __version__ = "0.0.1"
│   ├── hooks.py                   # App metadata; all hooks commented out
│   ├── modules.txt                # Single entry: "Oiv"
│   ├── patches.txt                # pre_model_sync / post_model_sync (both empty)
│   ├── patches/
│   │   └── __init__.py
│   ├── public/
│   │   └── .gitkeep               # No assets yet
│   ├── templates/
│   │   ├── __init__.py
│   │   └── pages/
│   │       └── __init__.py        # No web pages yet
│   ├── config/
│   │   └── __init__.py            # No desk icons or app screen entry yet
│   └── oiv/                       # "Oiv" Frappe module
│       ├── __init__.py
│       └── doctype/
│           ├── __init__.py
│           ├── user_profiles/
│           │   ├── __init__.py
│           │   ├── user_profiles.json       # 47 fields across 8 sections
│           │   ├── user_profiles.py         # Empty controller
│           │   ├── user_profiles.js         # Commented out
│           │   └── test_user_profiles.py    # Empty test stub
│           ├── weekly_reports/
│           │   ├── __init__.py
│           │   ├── weekly_reports.json      # Submittable; 7 fields
│           │   ├── weekly_reports.py        # Empty controller
│           │   ├── weekly_reports.js        # Commented out
│           │   └── test_weekly_reports.py   # Empty test stub
│           ├── weekly_activities/
│           │   ├── __init__.py
│           │   ├── weekly_activities.json   # Child table; 14 fields
│           │   ├── weekly_activities.py     # Empty controller
│           │   └── (no test file)
│           ├── mission_reports/
│           │   ├── __init__.py
│           │   ├── mission_reports.json     # 19 fields; not submittable
│           │   ├── mission_reports.py       # Empty controller
│           │   ├── mission_reports.js       # Commented out
│           │   └── test_mission_reports.py  # Empty test stub
│           ├── onerc_oiv_timesheet/
│           │   ├── __init__.py
│           │   ├── onerc_oiv_timesheet.json # 10 fields; not submittable
│           │   ├── onerc_oiv_timesheet.py   # Empty controller
│           │   ├── onerc_oiv_timesheet.js   # Commented out
│           │   └── test_onerc_oiv_timesheet.py  # Empty test stub
│           └── programme_posting/
│               ├── __init__.py
│               ├── programme_posting.json   # 1 data field only
│               ├── programme_posting.py     # Empty controller
│               ├── programme_posting.js     # Commented out
│               └── test_programme_posting.py # Empty test stub
├── pyproject.toml
├── .editorconfig
├── .eslintrc
├── .gitignore
├── .pre-commit-config.yaml
├── license.txt
└── README.md
```

---

## Module & App Registration

**`hooks.py`** registers the app with Frappe. Every optional hook (doc_events, scheduler_events, CSS/JS includes, permission hooks, install hooks, website generators, jinja, notifications, etc.) is present as commented-out boilerplate nothing is active beyond the five required metadata fields:

```python
app_name        = "oiv"
app_title       = "Oiv"
app_publisher   = "emm"
app_description = "onerc intern and volunteer platfrom"
app_email       = "matolojr@gmail.com"
app_license     = "mit"
```

**`modules.txt`** registers a single Frappe module named `Oiv`.

**`patches.txt`** defines the two standard patch sections (`pre_model_sync`, `post_model_sync`) but contains no patch entries.

---

## DocTypes

### 1. User Profiles

**Internal name:** `user profiles`
**File:** `oiv/oiv/doctype/user_profiles/`
**Allow rename:** Yes | **Submittable:** No | **Is Table:** No

The central record for every intern or volunteer. Contains 47 fields across 8 sections.

---

#### Section: Personal Details

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `first_name` | First Name | Data | |
| `last_name` | Last Name | Data | |
| `full_name` | Full Name | Data | `read_only: 1` **never auto-populated; no fetch_from or formula defined** |
| `gender` | Gender | Select | Male / Female |
| `date_of_birth` | Date of Birth | Date | |
| `age` | Age | Int | `read_only: 1` **never auto-populated; no formula defined** |
| `phone_number` | Phone number | Phone | |
| `email` | Email | Data | Plain Data, not Email fieldtype no format validation |
| `nationality` | Nationality | Select | Kenyan / Foreigner |
| `county` | County | Select | All 47 Kenya counties; `depends_on: doc.nationality == "Kenyan"` |
| `country` | Country | Link → Country | `depends_on: doc.nationality == "Foreigner"` |
| `city` | City | Data | `depends_on: doc.nationality == "Foreigner"` |
| `area_of_residency` | Area of Residency | Data | |
| `profile_photo` | Profile Photo | Attach Image | |
| `column_break_xira` | | Column Break | Splits layout into two columns |

#### Section: Emergency Contacts

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `f_name` | Full Name | Data | Fieldname `f_name` to avoid clash with `first_name` |
| `occupation` | Occupation | Data | |
| `phone_number_1` | Phone Number | Phone | |
| `relationship_type` | Relationship Type | Select | Father / Mother / Sibling / Spouse / Cousin / Neighbor / Other |
| `column_break_wjwi` | | Column Break | |

> ⚠️ Only one emergency contact is supported. There is no child table adding multiple contacts is not possible with the current schema.

#### Section: Skills and Interests

| Fieldname | Label | Type |
|---|---|---|
| `specify_your_skill_set` | Specify your skill set | Long Text |
| `outline_your_interests` | Outline your Interests | Long Text |
| `column_break_ebyv` | | Column Break |

#### Section: School Details

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `academic_level` | Academic Level | Select | Certificate / Diploma / Degree |
| `course` | Course | Data | |
| `institution_name` | Institution Name | Data | |
| `year_of_study` | Year of Study | Data | Stored as text, not Int no numeric validation |
| `campus` | Campus | Data | |
| `lecturers_name` | Lecturer's Name | Data | |
| `lecturers_email` | Lecturer's Email | Data | Plain Data, not Email fieldtype |
| `lecturers_contact` | Lecturer's Contact | Phone | |
| `column_break_exdi` | | Column Break | |

#### Section: Attachment/Internship Details (School side)

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `type` | Type | Select | Industrial Attachment / Internship / Volunteer |
| `department` | Department | Data | **Free text not linked to Department doctype** |
| `duration` | Duration | Duration | Frappe Duration fieldtype (stores value in seconds) |
| `project_title` | Project Title | Data | |

#### Section: Attachment/Internship Details (Placement side)

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `department_1` | Department | Link → Department | **Linked version duplicates the `department` Data field above** |
| `supervisor` | Supervisor | Link → Employee | |
| `work_station` | Work Station | Select | Headquarters, IOMe 001, IOMe 005, + all 47 Kenya counties |
| `column_break_abxe` | | Column Break | |

> ⚠️ Two separate department fields exist: `department` (Data / free text, fieldname in School Details section) and `department_1` (Link → Department, in Placement section). This duplication must be resolved.

#### Section: Documents

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `school_letter` | School Letter | Attach | |
| `insurance` | Insurance | Attach | |
| `school_certificates` | School Certificates | Attach | |
| `copy_of_national_id` | Copy of National ID | Attach | |
| `cv` | CV | Attach | |
| `human_resource_letter` | Human Resource Letter | Attach | `read_only: 1` issued by HR |
| `column_break_gums` | | Column Break | |

#### Section: Intern Activity *(conditionally hidden for non-admins)*

All fields in this section carry `depends_on: eval: frappe.session.user === 'Administrator' || frappe.user.has_role('System Manager')`.

| Fieldname | Label | Type |
|---|---|---|
| `date_of_activity` | Date of activity | Date |
| `activity` | Activity | Data |
| `description_of_activity` | Description of Activity | Text Editor |
| `next_steps` | Next Steps | Data |

> ⚠️ Hidden via `depends_on` (client-side JS) only, not via server-side permissions. Any user with direct API access can read and write these fields regardless of role.

The following fields appear in the same section in `field_order` but have **no** `depends_on` restriction they are visible to all roles:

| Fieldname | Label | Type |
|---|---|---|
| `skills_acquired` | Skills Acquired | Text Editor |
| `challenges` | Challenges | Text Editor |
| `support_needed` | Support Needed | Data |

#### Permissions

| Role | Create | Read | Write | Delete | Export | Print | Share |
|---|---|---|---|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Intern | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Supervisor | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| HR Manager | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |

> ⚠️ The Intern role has no `if_owner: 1` interns can read and write **all** profiles, not just their own.

---

### 2. Weekly Reports

**Internal name:** `weekly reports`
**File:** `oiv/oiv/doctype/weekly_reports/`
**Allow rename:** Yes | **Submittable:** Yes (`is_submittable: 1`) | **Is Table:** No

Interns submit structured weekly reports containing a child table of daily activity entries. The submittable flag enables the Draft → Submitted → Cancelled lifecycle, with amendment support via `amended_from`.

#### Fields

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `intern_name` | Intern Name | Link → user profiles | |
| `department` | Department | Link → Department | |
| `supervisor` | Supervisor | Link → Employee | |
| `status` | Status | Select | (blank) / Draft / Submitted / Reviewed / Approved / Returned |
| `activity` | Activity | Table → Weekly Activities | Inline child table |
| `amended_from` | Amended From | Link → weekly reports | `no_copy: 1`, `read_only: 1`, `print_hide: 1`, `search_index: 1` |

> ⚠️ No `week_start_date` or `week_end_date` on the parent record. Date data only exists per-row in the child table, making it impossible to filter or group reports by week at the list view level.

> ⚠️ `status` has no `read_only` flag and no Frappe Workflow. Any user with write access can manually set any status value.

> ⚠️ No `title_field` or `autoname` defined. Frappe assigns a sequential name like `weekly-reports-0001`.

#### Permissions

| Role | Create | Read | Write | Submit | Delete | Export | Print | Share |
|---|---|---|---|---|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Intern | ✅ | ✅ (own) | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Supervisor | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |

> The Intern role has `if_owner: 1` interns can only read and write their own records.
> ⚠️ The Intern permission entry has no `submit: 1` flag. Interns cannot formally submit their own reports despite the doctype being submittable.

---

### 3. Weekly Activities (Child Table)

**Internal name:** `Weekly Activities`
**File:** `oiv/oiv/doctype/weekly_activities/`
**Allow rename:** Yes | **Is Table:** Yes (`istable: 1`) | **Editable Grid:** Yes (`editable_grid: 1`)

Used exclusively as the `activity` child table inside Weekly Reports. No permissions array inherits from parent. No test file exists for this doctype.

#### Activities Section

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `date` | Date | Date | |
| `title` | Title | Data | |
| `activity_description` | Activity Description | Text | Plain Text (not Text Editor) |
| `skills_applied` | Skills Applied | Small Text | |
| `hours_spent` | Hours Spent | Float | Per-row value; never summed anywhere in the app |

#### Reflections Section

| Fieldname | Label | Type |
|---|---|---|
| `challenges_faced` | Challenges Faced | Text Editor |
| `key_learnings` | Key Learnings | Text Editor |
| `support_needed` | Support Needed | Text Editor |

#### Supervisor Section

These three fields have `allow_on_submit: 1`, remaining editable after the parent report is submitted so supervisors can fill them post-submission.

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `comments` | Comments | Text Editor | |
| `rating` | Rating | Rating | Frappe star rating widget (0–5) |
| `reviewd_on` | Reviewd on | Date | **Typo in both fieldname and label** should be `reviewed_on` |

---

### 4. Mission Reports

**Internal name:** `mission reports`
**File:** `oiv/oiv/doctype/mission_reports/`
**Allow rename:** Yes | **Submittable:** No | **Is Table:** No

Structured reports submitted after field missions or deployments, covering background, activities, findings, challenges, recommendations and an approval trail.

#### Fields

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `intern` | Intern | Data | **Free text not a Link to `user profiles`** |
| `mission_title` | Mission Title | Data | |
| `deployment` | Deployment | Link → Personnel Deployment Request | **DocType does not exist in this app** |
| `project` | Project | Link → Personnel Deployment Request | **Same target as `deployment` likely copy-paste error; should link to a Project doctype** |
| `date` | Mission Start Date | Date | Fieldname is `date`; label is "Mission Start Date" mismatch |
| `mission_end_date` | Mission End Date | Date | |
| `location` | Location | Link → Administrative Location | **DocType does not exist in this app** |
| `status` | Status | Select | (blank) / Draft / Submitted / Approved no "Rejected" or "Returned" option |
| `report` | Report | Text Editor | General narrative field |
| `activities_undertaken` | Activities Undertaken | Text Editor | |
| `findings_and_observations` | Findings and Observations | Text Editor | |
| `challenges` | Challenges | Text Editor | |
| `recommendations` | Recommendations | Text Editor | |
| `lessons_learned` | Lessons Learned | Text Editor | |
| `submitted_to` | Submitted To | Link → Employee | |
| `comments` | Comments | Text Editor | For reviewer use |
| `approved_on` | Approved on | Date | Not read-only; anyone with write can set it |

#### Permissions

| Role | Create | Read | Write | Delete | Export | Print | Share |
|---|---|---|---|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Intern | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Supervisor | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |

> ⚠️ Interns have `delete: 1` they can delete their own (and others') mission reports including approved ones. Almost certainly unintentional.

---

### 5. ONERC OIV Timesheet

**Internal name:** `onerc oiv timesheet`
**File:** `oiv/oiv/doctype/onerc_oiv_timesheet/`
**Allow rename:** Yes | **Submittable:** No | **Is Table:** No

Tracks weekly hours for an intern, linked to one weekly report. Intended to be reviewed by supervisors and then HR.

#### Fields

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `intern` | Intern | Link → user profiles | |
| `department` | Department | Link → Department | `read_only: 1` never auto-populated by any logic |
| `week_start_date` | Week Start Date | Date | |
| `week_end_date` | Week End Date | Date | |
| `linked_weekly_reports` | Linked Weekly Reports | Link → weekly reports | Singular Link only one report can be associated |
| `total_hours` | Total Hours | Float | Plain editable float; not computed from any source |
| `status` | Status | Select | `read_only: 1` (blank) / Draft / Submitted / Approved / Rejected / Flagged for HR |
| `supervisor` | Supervisor | Link → Employee | Not read-only; editable by anyone with write permission |
| `supervisor_comments` | Supervisor Comments | Long Text | `read_only: 1` supervisors cannot enter comments via the form |
| `hr_notes` | HR Notes | Long Text | `read_only: 1` HR managers cannot enter notes via the form |

> ⚠️ `status` is `read_only: 1` with no controller logic to change it. No user can progress the status through the UI it will always remain blank.

> ⚠️ `supervisor_comments` and `hr_notes` are both `read_only: 1`. The Supervisor and HR Manager roles have write permission on the doctype, but these specific fields are locked, making the roles functionally useless for their primary purpose.

> ⚠️ Intern permission has no `write: 1`. Interns can create a timesheet but cannot edit it afterward.

#### Permissions

| Role | Create | Read | Write | Delete | Export | Print | Share |
|---|---|---|---|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| HR Manager | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Supervisor | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Intern | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |

> Note: System Manager has no `delete: 1` on this doctype even admins cannot delete timesheets through normal permissions.

---

### 6. Programme Posting

**Internal name:** `Programme Posting`
**File:** `oiv/oiv/doctype/programme_posting/`
**Allow rename:** Yes | **Submittable:** No | **Is Table:** No

A skeleton doctype linking a programme opening to an ERPNext `Job Opening`. Currently has only one meaningful data field and no additional metadata.

#### Fields

| Fieldname | Label | Type | Notes |
|---|---|---|---|
| `programme_posting_section` | Programme Posting | Section Break | Section header only |
| `opening` | opening | Link → Job Opening | Label uses lowercase "opening" |

#### Permissions

System Manager only: create, read, write, delete, export, print, share.

---

## Roles & Permissions Summary

| DocType | System Manager | HR Manager | Supervisor | Intern |
|---|---|---|---|---|
| User Profiles | Full | Read + Write | Read only | Create + Read + Write (all records, no `if_owner`) |
| Weekly Reports | Full | | Read + Write | Create + Read + Write (own only via `if_owner`) |
| Weekly Activities | (inherits parent) | | | |
| Mission Reports | Full | | Read + Write | Full including Delete |
| OIV Timesheet | Full (no Delete) | Read + Write | Read + Write | Create + Read only |
| Programme Posting | Full | | | |

---

## External DocType Dependencies

The app references DocTypes not defined within it. They must exist in a parent app or be created separately before install:

| Referenced DocType | Used In | Source |
|---|---|---|
| `Department` | User Profiles, Weekly Reports, OIV Timesheet | ERPNext / Frappe HR |
| `Employee` | User Profiles, Weekly Reports, Mission Reports, OIV Timesheet | ERPNext / Frappe HR |
| `Country` | User Profiles | Frappe core |
| `Job Opening` | Programme Posting | ERPNext |
| `Personnel Deployment Request` | Mission Reports (`deployment` + `project` fields) | **Not in this app or standard ERPNext must be created** |
| `Administrative Location` | Mission Reports (`location` field) | **Not in this app or standard ERPNext must be created** |

---

## Tooling & Code Quality

### Python Ruff

Configured in `pyproject.toml`. Key settings:

```toml
[tool.ruff]
line-length = 110
target-version = "py310"

[tool.ruff.lint]
select = ["F", "E", "W", "I", "UP", "B", "RUF"]
```

Notable ignores: `E501` (line too long), `F401` (unused imports), `F403`/`F405` (star imports), `W191`/`E101` (tabs), `E402` (module-level imports not at top), `B904` (raise without from inside except).

Format: double quotes, tab indent, docstring code formatting enabled.

### JavaScript ESLint + Prettier

ESLint extends `eslint:recommended`. Most style rules are disabled (indent, quotes, semi, brace-style are all `"off"`). The globals list covers the full Frappe desk environment:

- Frappe core: `frappe`, `cur_frm`, `cur_dialog`, `cur_list`, `cur_tree`, `cur_page`, `__`, `locals`, `repl`, `Class`
- Frappe helpers: `cint`, `cstr`, `flt`, `precision`, `format_number`, `format_currency`, `strip_html`, `validate_email`, `validate_url`, `refresh_field`, `unhide_field`, `hide_field`, `set_field_options`, `get_field_obj`
- Libraries: `jQuery`/`$`, `moment`, `Vue`, `Chart`, `DataTable`, `Gantt`, `Slick`, `Sortable`, `Showdown`, `Taggle`, `Webcam`, `PhotoSwipe`, `L` (Leaflet), `JsBarcode`, `io` (Socket.IO), `Awesomplete`, `hljs`, `localforage`, `qz`, `posthog`
- Testing: `Cypress`, `cy`, `it`, `describe`, `expect`, `context`, `before`, `beforeEach`, `after`

Prettier targets `.js`, `.vue`, `.scss` files, excluding `dist/`, `node_modules/`, `boilerplate/`, `templates/includes/` and `public/js/lib/`.

### Editor Config

| File type | Indent | Size | Notes |
|---|---|---|---|
| `.py`, `.js`, `.vue`, `.css`, `.scss`, `.html` | Tab | 4 | Max line length 99 |
| `.json` | Space | 2 | No final newline |

All files: LF line endings, UTF-8, trailing whitespace trimmed. Non-JSON files: final newline inserted.

### Pre-commit Hooks

| Hook | Tool | Targets |
|---|---|---|
| `trailing-whitespace` | pre-commit-hooks v5.0.0 | `oiv.*` excluding json/txt/csv/md/svg |
| `check-merge-conflict` | pre-commit-hooks | All |
| `check-ast` | pre-commit-hooks | Python |
| `check-json` | pre-commit-hooks | JSON |
| `check-toml` | pre-commit-hooks | TOML |
| `check-yaml` | pre-commit-hooks | YAML |
| `debug-statements` | pre-commit-hooks | Python |
| Import sort | ruff v0.8.1 (`--select=I --fix`) | Python |
| Lint | ruff v0.8.1 | Python |
| Format | ruff-format v0.8.1 | Python |
| Format | prettier v2.7.1 | JS / Vue / SCSS (with exclusions) |
| Lint | eslint v8.44.0 (quiet) | JS only (with exclusions) |

CI autoupdate schedule: weekly.

---

## Installation

### Prerequisites

- [Frappe Bench](https://github.com/frappe/bench) installed and configured
- ERPNext v15+ on your site (required for `Department`, `Employee`, `Job Opening`)
- Python ≥ 3.10
- Node.js (for frontend asset building)

### Steps

```bash
cd $PATH_TO_YOUR_BENCH

bench get-app $URL_OF_THIS_REPO --branch develop

bench install-app oiv

bench --site <your-site> migrate
```

---

## Contributing

This app uses `pre-commit` for code formatting and linting. Install and enable it before making any commits:

```bash
cd apps/oiv
pre-commit install
```

All Python code must pass `ruff` linting and `ruff-format`. All JS/Vue/SCSS must pass `eslint` and `prettier`. Commits that fail any hook will be blocked.

---

## Known Bugs & Incomplete Work

### 🔴 Broken Will Not Work As-Is

- [ ] **`full_name` is never computed.** The field is `read_only: 1` but there is no `fetch_from`, formula, or `before_save` logic in `user_profiles.py` to concatenate `first_name` and `last_name`. It will always be blank.

- [ ] **`age` is never computed.** Same issue `read_only: 1` with no formula or controller logic to derive it from `date_of_birth`.

- [ ] **Timesheet `status` is permanently stuck.** The `status` field is `read_only: 1` and `onerc_oiv_timesheet.py` is empty (`pass`). No user can change the status through the UI it will always be blank.

- [ ] **Timesheet `supervisor_comments` and `hr_notes` are `read_only: 1`.** Supervisors and HR Managers with write access to the doctype cannot actually enter comments the fields are locked. The `read_only` flags must be removed or replaced with conditional logic.

- [ ] **Timesheet `department` is `read_only: 1` with no auto-population.** The field will always be blank since no logic copies it from the linked intern profile.

- [ ] **`Personnel Deployment Request` and `Administrative Location` do not exist.** Both are referenced in `mission_reports.json` but are defined in neither this app nor standard ERPNext. Mission Reports cannot be saved with those fields populated.

- [ ] **Intern cannot submit Weekly Reports.** The Intern permission entry for `weekly reports` has no `submit: 1` flag. Interns cannot formally submit their own reports despite the doctype being `is_submittable: 1`.

### 🟡 Data Model Problems

- [ ] **`intern` in Mission Reports is a `Data` field**, not `Link → user profiles`. This breaks relational integrity no validation, no lookups, no linking to the actual profile record.

- [ ] **`project` in Mission Reports links to `Personnel Deployment Request`**, the same target as `deployment`. Almost certainly a copy-paste error it should link to a `Project` doctype.

- [ ] **Two conflicting department fields in User Profiles.** `department` (fieldname) is a `Data` free-text field; `department_1` is `Link → Department`. Only one should exist.

- [ ] **No week-level date fields on Weekly Reports.** There is no `week_start_date` or `week_end_date` on the parent only on individual child rows. This makes week-based filtering, list views and timesheet linking impractical.

- [ ] **Timesheet `linked_weekly_reports` is a single `Link`, not a Table.** Only one weekly report can be associated per timesheet. If the intent is to cover multiple reports in a week, a child table is needed.

- [ ] **Single emergency contact.** The profile stores one contact as flat fields. Multiple contacts require a child table.

- [ ] **`email` and `lecturers_email` are `Data` type**, not `Email` fieldtype no email format validation.

- [ ] **`year_of_study` is `Data` type**, not `Int` no numeric validation.

- [ ] **`reviewd_on` is a typo** in both the fieldname and label of `Weekly Activities` (should be `reviewed_on`). A database patch will be required to rename this after data exists.

### 🟠 Security Concerns

- [ ] **Intern Activity section uses client-side `depends_on` only.** Fields such as `description_of_activity` and `next_steps` are not protected at the server or permission level. Any user with API access can read or set them regardless of role.

- [ ] **Interns have `delete: 1` on Mission Reports.** An intern can delete any mission report including submitted or approved ones. This is almost certainly unintentional.

- [ ] **Intern role reads all User Profiles** (no `if_owner: 1`). Every intern can browse every other intern's personal details, documents and supervisor assignments.

### 🟢 Not Yet Started

- [ ] All Python controllers are empty (`pass`). No `validate`, `before_save`, `on_submit`, `on_cancel`, or `after_insert` logic exists anywhere.
- [ ] All JavaScript form files are fully commented out. No client-side behaviour (field toggles, auto-fill, custom buttons) is implemented.
- [ ] No Frappe Workflows defined. Status transitions on all doctypes are uncontrolled manual selects.
- [ ] No scheduler events registered in `hooks.py`. No automated tasks (reminders, escalations, deadline tracking).
- [ ] No notifications configured. No email or in-app alerts on submission, approval, or rejection.
- [ ] No custom reports. No Query Reports or Script Reports for analytics (hours by intern, missions by location, etc.).
- [ ] No dashboard defined. No Frappe Dashboard charts for HR or supervisors.
- [ ] No web forms. Candidates cannot apply or access data without a Frappe desk account.
- [ ] No desk icons or app screen entry. `config/` is empty and `add_to_apps_screen` in `hooks.py` is commented out.
- [ ] No print formats defined for any doctype.
- [ ] `Programme Posting` is a skeleton with one field. No description, eligibility, dates, capacity, or application process fields exist.
- [ ] Zero tests written. All five test files extend `FrappeTestCase` and contain only `pass`.
- [ ] `hooks.py` boilerplate not cleaned up. Dozens of commented-out entries make it hard to distinguish intentionally unused hooks from planned ones.
- [ ] `license.txt` placeholder values (`[year]`, `[fullname]`) have not been filled in.

---

## License

MIT License see [license.txt](license.txt) for full text.

---

*Built on the [Frappe Framework](https://frappeframework.com/) for ONERC.*