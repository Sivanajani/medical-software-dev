# Exercise 5 – Software Requirements Specification
Medical Software Development · FHNW · 2025

**Sources:** [`SRS TMS`](SRS_TMS.pdf)

---

## 1. Who created the final version?

Version 1.0 (the final version) was created by Osamah Yacoub and Ahmad Arrabi from AlliedSoft, finalized on December 31, 2002. The document was prepared by AlliedSoft in collaboration with Chemonics International Inc. for the AMIR Program in Jordan.

---

## 2. What is the intended use?

Based on the Introduction and Scope sections of the SRS:

The TMS is intended to acquire and track training and testing sessions for Government of Jordan (GoJ) employees.

More specifically, the system is meant to:

- **Automate** the process of acquiring training and testing
- **Support a bidding process** for training/testing offers
- **Track** employee nomination, registration, and results
- **Collect** course feedback from trainees
- **Generate** relevant reports and views
- **Provide visibility** to management about training needs

The document also states a broader goal: to serve as a basis for software design, development, and testing, meaning the SRS itself is intended as a contract between the client and the development team, capturing agreed scope before implementation begins.

---

## 3. Who are the intended users?

Based on Section 4.2 (Actors) of the SRS, five user groups are defined:

| Actor | Role |
|---|---|
| **System Administrator** | Full system access; sets up the system for all other user groups (entities, users, locations, TPs, TCs, PMUs) |
| **PMU Administrator** | Manages the entire training/testing workflow, including maintaining TPs, administering requests, selecting TPs, and registering employees |
| **TP Administrator** | Manages their own training/testing center information, submits offers, reports attendance and results |
| **Training Coordinator (TC)** | Tracks employee training/testing status and nominates employees for training/testing |
| **GoJ Employee** | Views their own training/testing history and submits course evaluations |

The users can broadly be grouped into two categories:

- **Administrative users** (System Admin, PMU, TP Admin, TC): who manage the system and its workflows
- **End users** (GoJ Employees): who interact with the system in a limited, read/submit capacity

It is worth noting that the SRS states (Assumption 11) that for administrative groups (PMU, TP, TC), there is no business need for different login IDs per individual within those groups, meaning these roles are shared accounts rather than personal ones.

---

## 4. What is the standard environment?

Based on Section 2 (Assumptions and Dependencies) and Section 5.1 (System Requirements) of the SRS, the standard environment is defined as follows:

| Aspect | Specification |
|---|---|
| **Application Type** | Web-based (Internet or Intranet) |
| **Browser** | Microsoft Internet Explorer 5.0 or above |
| **Languages** | English or Arabic |
| **Screen Resolution** | 800×600 (optimal) |
| **Excel Export** | Microsoft Excel 2000 or above |
| **Architecture** | 3-tier software architecture with XML support |
| **Runtime** | Hardware, software, and networking supplied and maintained by the client |

A few important notes:

- AlliedSoft is explicitly not responsible for the purchase, setup, or configuration of the runtime hardware, software, or networking environment. This is the client's responsibility
- The environment is notably narrow and dated even by 2003 standards, specifying only Internet Explorer 5.0+ means no cross-browser compatibility is required
- No reporting technology is mandated as a standard. AlliedSoft is free to choose any reporting technique that meets the requirements
- There is no mention of server-side requirements such as operating system, database, or server software, which could be considered a gap in the SRS

---

## 5. Functional Requirement Analysis FR03 – Users Maintenance

> *"Add, update, and delete system administrators and GoJ trainees; trainee information should include gender"*

### Complete
The requirement is incomplete in several ways:
- It only mentions add, update, and delete. There is no mention of read/view, even though all other similar requirements in the use cases include it
- It does not specify what information should be stored for system administrators beyond gender for trainees
- Password management, account activation/deactivation, and login ID assignment are not mentioned
- No mention of mandatory vs. optional fields
- No mention of what happens to dependent data when a user is deleted (e.g., training history)

### Accurate
The requirement is partially accurate but contains a notable inconsistency:
- The title says "Users Maintenance" but the description only mentions system administrators and GoJ trainees. It omits TP Administrators and Training Coordinators, who are also system users
- This is contradicted by Section 4.2, where five distinct actor types are defined
- The mention of gender is accurate and consistent with the broader context of gender-based reporting (FR20.16 requires pass rate reports by gender)

### Unambiguous
The requirement is ambiguous in multiple ways:
- GoJ trainees is used here, but elsewhere the document uses GoJ Employees. It is unclear whether these refer to the same group
- Trainee information should include gender. the word "should" is weak and non-committal; it is unclear whether this is mandatory or optional
- It is unclear whether administrators and trainees are managed in the same interface or separately
- No definition of what constitutes valid/invalid user information

### Traceable
This is the strongest aspect of the requirement:
- It has a clear identifier (FR03)
- It links to use case 4.3.27 (Administrator Maintenance) and 4.3.28 (GoJ Employee Maintenance)
- It connects to reporting requirement FR20.16 (pass rate by gender), justifying why gender is needed
- It can be traced back to the client (MoICT) as the originating stakeholder

### Testable
The requirement is partially testable:

| Test | Testable? |
|---|---|
| Can a user be added? | Yes |
| Can a user be updated? | Yes |
| Can a user be deleted? | Yes |
| Does trainee record include a gender field? | Yes |
| Are all required fields validated? | No. Fields not specified |
| What are valid gender values? | No. Not defined |
| What happens to data on deletion? | No. Not specified |

### Summary

| Criterion | Rating | Key Issue |
|---|---|---|
| **Complete** | Poor | Missing read operation, field definitions, and deletion behavior |
| **Accurate** | Partial | Omits TP Administrators and TCs as users |
| **Unambiguous** | Poor | "Should", "trainees" vs "employees", unclear scope |
| **Traceable** | Good | Clear ID, links to use cases and reporting requirements |
| **Testable** | Partial | Basic CRUD testable, but validation rules undefined |

Overall, FR03 is a weak requirement, while traceable, it lacks the precision and completeness needed to guide development and testing reliably.

---

## 6. Is there a requirement regarding data security?

Yes, there are security requirements found in Section 5.2 (Security Requirements).

### What is defined: Role-Based Access Control (RBAC)

Four security levels are specified:

| Req. | Role | Access Rights |
|---|---|---|
| SEC01 | PMU | Full system control; update lookup data; generate all reports |
| SEC02 | TP Administrators | Limited to own center; update attendance/results; submit offers |
| SEC03 | Training Coordinators | Administer own employees; nominate for training/testing |
| SEC04 | GoJ Employees | View own training history; submit evaluations only |

### What is NOT defined

The security requirements are very limited in scope. The SRS notably lacks:

| Missing Aspect | Implication |
|---|---|
| Encryption | No mention of HTTPS or data encryption in transit or at rest |
| Password policies | No rules for password strength, expiry, or complexity |
| Session management | No timeout or session security rules defined |
| Audit logging | No requirement to track who changed what and when |
| Data backup | No mention of data recovery or backup strategies |
| Input validation | No mention of protection against injection attacks |

### Conclusion

The security section is superficial, it only defines *who can access what*, but says nothing about *how the system should technically protect that data*. For a web-based government system handling employee data, this represents a significant gap in the SRS.

---

## 7. Is there a requirement on how the software should be designed?

Yes, there are design-related requirements found in Section 3 (High-Level System Architecture) and Section 5.1 (System Requirements).

### Architecture Requirement — SYS03

The most explicit design requirement is:

> *"The application must be designed with a 3-tier software architecture with XML support for interoperability with future e-Government applications."*

The three tiers are defined as:

| Tier | Description |
|---|---|
| Tier 1 (Front-End) | Browser-based UI for visual programming, input, and visualization |
| Tier 2 (Middleware) | Distributed, object-based, scalable web server / object broker |
| Tier 3 (Back-End) | Back-end services and resources |

### Other Design-Related Requirements

| Req. | Description |
|---|---|
| SYS01 | Application must be web-based |
| SYS02 | UI must support both English and Arabic |
| DOC02 | A Software Design Specification document must be delivered, including hardware recommendations and security design |

### What is NOT defined

Despite these requirements, many design aspects are left open:

| Missing Aspect | Implication |
|---|---|
| Database design | No database technology or schema requirements specified |
| Server-side technology | No programming language or framework mandated |
| Security architecture | DOC02 mentions it but no details are given in the SRS itself |
| Performance requirements | No response times, load capacity, or scalability targets defined |
| UI/UX guidelines | Beyond language and browser support, no design standards are specified |

### Conclusion

The design requirements are minimal but present. The 3-tier architecture and XML support are clearly mandated, giving developers a structural framework. However, the SRS largely leaves technical implementation decisions open, which is appropriate for an SRS (which should define what the system does, not how it does it). Notably, SYS03 is an exception to this principle. By mandating a specific 3-tier architecture, the SRS crosses into design territory, likely driven by the need for interoperability with future e-Government applications. Despite this, many other important non-functional aspects remain underspecified.