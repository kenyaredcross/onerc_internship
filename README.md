# OIV — ONERC Intern & Volunteer Platform

> A [Frappe](https://frappeframework.com/) application built to manage interns and volunteers for ONERC (One Red Cross), covering onboarding, activity tracking, weekly reporting, mission documentation, and timesheet management.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [DocTypes (Data Models)](#doctypes-data-models)
  - [User Profiles](#1-user-profiles)
  - [Weekly Reports](#2-weekly-reports)
  - [Weekly Activities](#3-weekly-activities-child-table)
  - [Mission Reports](#4-mission-reports)
  - [ONERC OIV Timesheet](#5-onerc-oiv-timesheet)
  - [Programme Posting](#6-programme-posting)
- [Roles & Permissions](#roles--permissions)
- [Installation](#installation)
- [Contributing](#contributing)
- [Known Issues & Remaining Work](#known-issues--remaining-work)
- [License](#license)

---

## Overview

OIV is a custom Frappe app designed for ONERC to digitize and streamline the management of interns and volunteers. It provides:

- **Intern onboarding** — profile creation with personal, academic, emergency, and document details
- **Weekly activity logging** — interns log daily/weekly activities, which supervisors review and rate
- **Mission reporting** — structured field mission reports with findings, challenges, and recommendations
- **Timesheets** — weekly hour tracking linked to weekly reports, with supervisor and HR review workflows
- **Programme postings** — linking internship openings to ERPNext Job Openings

The app integrates with ERPNext/Frappe's built-in modules for Departments, Employees, and Job Openings.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | [Frappe Framework](https://frappeframework.com/) v15+ |
| Backend | Python 3.10+ |
| Frontend | JavaScript (Frappe desk UI), Vue.js (available via Frappe) |
| Database | MariaDB (InnoDB engine) |
| Linting | Ruff (Python), ESLint + Prettier (JS/Vue) |
| Pre-commit hooks | ruff, eslint, prettier, pyupgrade |
| Build | flit_core |

---

## Project Structure

```
oiv/
├── oiv/                          # Main app Python package
│   ├── hooks.py                  # App hooks and configuration
│   ├── modules.txt               # Registered Frappe modules
│   ├── patches.txt               # Database migration patches
│   ├── patches/                  # Patch scripts
│   ├── public/                   # Static assets (JS, CSS, icons)
│   ├── templates/                # Jinja web templates
│   │   └── pages/
│   ├── config/                   # App config (desk icons, etc.)
│   └── oiv/                      # "Oiv" module
│       └── doctype/
│           ├── user_profiles/         # Intern/volunteer profile
│           ├── weekly_reports/        # Weekly report submission
│           ├── weekly_activities/     # Child table for activities
│           ├── mission_reports/       # Field mission reports
│           ├── onerc_oiv_timesheet/   # Weekly timesheets
│           └── programme_posting/     # Programme/opening postings
├── pyproject.toml                # Python project metadata & Ruff config
├── .eslintrc                     # ESLint config for JS
├── .editorconfig                 # Editor formatting rules
├── .pre-commit-config.yaml       # Pre-commit hooks config
├── .gitignore
├── license.txt                   # MIT License
└── README.md
```

---

## DocTypes (Data Models)

### 1. User Profiles

**DocType name:** `user profiles`
**Purpose:** Stores the complete profile for each intern or volunteer.

#### Sections & Fields

**Personal Details**
| Field | Type | Notes |
|---|---|---|
| First Name | Data | |
| Last Name | Data | |
| Full Name | Data | Read-only (auto-computed) |
| Gender | Select | Male / Female |
| Date of Birth | Date | |
| Age | Int | Read-only (auto-computed) |
| Phone Number | Phone | |
| Email | Data | |
| Nationality | Select | Kenyan / Foreigner |
| County | Select | 47 Kenya counties (shown if Kenyan) |
| Country | Link → Country | Shown if Foreigner |
| City | Data | Shown if Foreigner |
| Area of Residency | Data | |
| Profile Photo | Attach Image | |

**Emergency Contacts**
| Field | Type | Notes |
|---|---|---|
| Full Name | Data | |
| Occupation | Data | |
| Phone Number | Phone | |
| Relationship Type | Select | Father / Mother / Sibling / Spouse / Cousin / Neighbor / Other |

**Skills and Interests**
| Field | Type |
|---|---|
| Skill Set | Long Text |
| Interests | Long Text |

**School Details**
| Field | Type | Notes |
|---|---|---|
| Academic Level | Select | Certificate / Diploma / Degree |
| Course | Data | |
| Institution Name | Data | |
| Year of Study | Data | |
| Campus | Data | |
| Lecturer's Name | Data | |
| Lecturer's Email | Data | |
| Lecturer's Contact | Phone | |

**Attachment/Internship Details**
| Field | Type | Notes |
|---|---|---|
| Type | Select | Industrial Attachment / Internship / Volunteer |
| Department | Link → Department | |
| Supervisor | Link → Employee | |
| Work Station | Select | HQ + all 47 Kenya counties + IOMe stations |
| Duration | Duration | |
| Project Title | Data | |

**Documents**
| Field | Type | Notes |
|---|---|---|
| School Letter | Attach | |
| Insurance | Attach | |
| School Certificates | Attach | |
| Copy of National ID | Attach | |
| CV | Attach | |
| Human Resource Letter | Attach | Read-only (issued by HR) |

**Intern Activity** *(Admin/System Manager only)*
| Field | Type |
|---|---|
| Date of Activity | Date |
| Activity | Data |
| Description of Activity | Text Editor |
| Skills Acquired | Text Editor |
| Challenges | Text Editor |
| Next Steps | Data |
| Support Needed | Data |

#### Permissions
| Role | Create | Read | Write | Delete |
|---|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ | ✅ |
| Intern | ✅ | ✅ | ✅ | ❌ |
| Supervisor | ❌ | ✅ | ❌ | ❌ |
| HR Manager | ❌ | ✅ | ✅ | ❌ |

---

### 2. Weekly Reports

**DocType name:** `weekly reports`
**Purpose:** Interns submit weekly summaries of their activities for supervisor review.
**Is Submittable:** Yes (supports Draft → Submit → Cancel workflow)

#### Fields
| Field | Type | Notes |
|---|---|---|
| Intern Name | Link → user profiles | |
| Department | Link → Department | |
| Supervisor | Link → Employee | |
| Status | Select | Draft / Submitted / Reviewed / Approved / Returned |
| Activity | Table → Weekly Activities | Child table of detailed daily entries |
| Amended From | Link → weekly reports | Standard amendment tracking |

#### Permissions
| Role | Create | Read | Write | Submit |
|---|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ | ✅ |
| Intern | ✅ (own) | ✅ (own) | ✅ | ✅ |
| Supervisor | ❌ | ✅ | ✅ | ❌ |

---

### 3. Weekly Activities (Child Table)

**DocType name:** `Weekly Activities`
**Purpose:** Detailed per-entry rows inside a Weekly Report. `istable: 1`

#### Fields

**Activities Section**
| Field | Type |
|---|---|
| Date | Date |
| Title | Data |
| Activity Description | Text |
| Skills Applied | Small Text |
| Hours Spent | Float |

**Reflections Section**
| Field | Type |
|---|---|
| Challenges Faced | Text Editor |
| Key Learnings | Text Editor |
| Support Needed | Text Editor |

**Supervisor Section** *(editable after submit)*
| Field | Type |
|---|---|
| Comments | Text Editor |
| Rating | Rating |
| Reviewed On | Date |

---

### 4. Mission Reports

**DocType name:** `mission reports`
**Purpose:** Formal reports submitted by interns/staff after field missions or deployments.

#### Fields
| Field | Type | Notes |
|---|---|---|
| Intern | Data | |
| Mission Title | Data | |
| Deployment | Link → Personnel Deployment Request | |
| Project | Link → Personnel Deployment Request | |
| Mission Start Date | Date | |
| Mission End Date | Date | |
| Location | Link → Administrative Location | |
| Status | Select | Draft / Submitted / Approved |
| Report | Text Editor | General narrative |
| Activities Undertaken | Text Editor | |
| Findings and Observations | Text Editor | |
| Challenges | Text Editor | |
| Recommendations | Text Editor | |
| Lessons Learned | Text Editor | |
| Submitted To | Link → Employee | |
| Comments | Text Editor | Reviewer comments |
| Approved On | Date | |

#### Permissions
| Role | Create | Read | Write | Delete |
|---|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ | ✅ |
| Intern | ✅ | ✅ | ✅ | ✅ |
| Supervisor | ❌ | ✅ | ✅ | ❌ |

---

### 5. ONERC OIV Timesheet

**DocType name:** `onerc oiv timesheet`
**Purpose:** Tracks total hours worked per week, linked to a weekly report. Reviewed by supervisors and HR.

#### Fields
| Field | Type | Notes |
|---|---|---|
| Intern | Link → user profiles | |
| Department | Link → Department | Read-only |
| Week Start Date | Date | |
| Week End Date | Date | |
| Linked Weekly Reports | Link → weekly reports | |
| Total Hours | Float | |
| Status | Select | Draft / Submitted / Approved / Rejected / Flagged for HR — Read-only |
| Supervisor | Link → Employee | |
| Supervisor Comments | Long Text | Read-only |
| HR Notes | Long Text | Read-only |

#### Permissions
| Role | Create | Read | Write |
|---|---|---|---|
| System Manager | ✅ | ✅ | ✅ |
| HR Manager | ❌ | ✅ | ✅ |
| Supervisor | ❌ | ✅ | ✅ |
| Intern | ✅ | ✅ | ❌ |

---

### 6. Programme Posting

**DocType name:** `Programme Posting`
**Purpose:** Links an internship/volunteer programme opening to an ERPNext Job Opening record.

#### Fields
| Field | Type |
|---|---|
| Opening | Link → Job Opening |

#### Permissions
System Manager only (create, read, write, delete).

---

## Roles & Permissions

The app defines four custom roles:

| Role | Description |
|---|---|
| **Intern** | Can create and manage their own profile, weekly reports, and mission reports |
| **Supervisor** | Read-only on profiles; can review and write on weekly reports and timesheets |
| **HR Manager** | Can read and write profiles; read and manage timesheets |
| **System Manager** | Full access to all doctypes |

> ⚠️ The `Intern` role on `Weekly Reports` uses `if_owner: 1`, meaning interns can only see and edit their own records.

---

## Installation

### Prerequisites

- [Frappe Bench](https://github.com/frappe/bench) installed
- ERPNext v15+ installed in your bench (for Department, Employee, Job Opening links)
- Python 3.10+
- Node.js (for frontend assets)

### Steps

```bash
# Navigate to your bench directory
cd /path/to/your/bench

# Get the app
bench get-app https://github.com/your-org/oiv --branch develop

# Install the app on your site
bench --site your-site.localhost install-app oiv

# Run migrations
bench --site your-site.localhost migrate
```

### Setting Up Pre-commit (for contributors)

```bash
cd apps/oiv

# Install pre-commit
pip install pre-commit

# Enable hooks for this repo
pre-commit install
```

Pre-commit will run the following checks on every commit:
- **ruff** — Python import sorting and linting
- **ruff-format** — Python code formatting
- **eslint** — JavaScript linting
- **prettier** — JavaScript/Vue/SCSS formatting
- **trailing-whitespace**, **check-merge-conflict**, **check-ast**, **check-json**, **check-yaml**, **check-toml**, **debug-statements** — general hygiene checks

---

## Known Issues & Remaining Work

### 🔴 Critical / Blockers

- [ ] **`Intern` field in Mission Reports is `Data` type** — should be `Link → user profiles` for relational integrity and filtering
- [ ] **`project` field in Mission Reports links to `Personnel Deployment Request`** — this appears to be a copy-paste error; it likely should link to a `Project` doctype
- [ ] **`Personnel Deployment Request` and `Administrative Location` doctypes are referenced but not defined** in this app — they must either be created here or confirmed as existing in a dependent app
- [ ] **No server-side logic** — all `.py` controller files are empty (`pass`). Business logic (auto-fill, validation, status transitions) is entirely missing

### 🟡 High Priority

- [ ] **Workflow automation** — Status fields on all doctypes are manual `Select` fields. Proper Frappe Workflows should be configured so status transitions are gated by role (e.g., only a Supervisor can set "Approved")
- [ ] **`full_name` and `age` are read-only but not auto-computed** — the `user_profiles.py` controller needs `before_save` logic to concatenate `first_name + last_name` and compute `age` from `date_of_birth`
- [ ] **Timesheet `total_hours` is not auto-computed** — should sum `hours_spent` from linked `Weekly Activities` rows
- [ ] **Timesheet `department` and `status` are read-only** — need server-side logic to auto-populate these from the linked intern profile and submission action
- [ ] **No `amended_from` handling** in `weekly_reports.py` — amendment logic should be implemented if the submittable workflow is used
- [ ] **`Programme Posting` doctype is very sparse** — needs additional fields (description, eligibility criteria, dates, capacity) to be usable as a public-facing posting

### 🟢 Nice to Have / Enhancements

- [ ] **Dashboard** — A summary dashboard for HR/Supervisors showing active interns, pending approvals, overdue reports
- [ ] **Notifications** — Email/in-app alerts when a report is submitted, approved, or returned
- [ ] **Web forms** — Public-facing application form so candidates can apply without a Frappe account
- [ ] **Reports & Analytics** — Custom Frappe reports for intern hours by department, mission count by location, etc.
- [ ] **Document generation** — Auto-generate completion/experience letters as PDF using the `human_resource_letter` attachment field
- [ ] **`Weekly Activities` child table** — Add an `idx` (day number) or enforce date range validation against the parent `Weekly Report` week dates
- [ ] **Kenya county → workstation alignment** — The `work_station` select options and the `county` select options are currently separate lists; consider linking them
- [ ] **Volunteer-specific fields** — The `type` field supports "Volunteer" but the profile has no volunteer-specific fields (e.g., volunteer hours cap, volunteering category)
- [ ] **Tests** — All test files (`Testmissionreports`, `Testuserprofiles`, etc.) are empty stubs; unit and integration tests need to be written
- [ ] **`hooks.py` cleanup** — Many hooks entries are commented out boilerplate; document which ones are intentionally unused vs. planned

---