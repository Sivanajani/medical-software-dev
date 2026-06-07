# Exercise 5 – Software Requirements Specification
Medical Software Development, FHNW 2026

**Sources:** [`SRS_TMS.pdf`](SRS_TMS.pdf) – E-Government Training Management System, AlliedSoft / AMIR Program, January 2003  
[`slides_09_medicalsoftwaredevelopment.pdf`](slides_09_medicalsoftwaredevelopment.pdf) – Requirements Engineering, MSD Course, FHNW, March 2025

---

## 1. Who created the final version?

Version 1.0 was created by Osamah Yacoub and Ahmad Arrabi from AlliedSoft, finalized on December 31, 2002. The document was prepared by AlliedSoft in collaboration with Chemonics International Inc. for the AMIR Program in Jordan.

---

## 2. What is the intended use?

The SRS captures the complete software requirements for the E-Government Training Management System (TMS). According to Section 1 (Introduction), the document serves two purposes: it is intended to be approved by the client as a representation of agreed scope, and it is used by the development team as the basis for software design, development, and testing.

Functionally, the TMS is intended to:

- Acquire and track training and testing sessions for Government of Jordan (GoJ) employees
- Support a bidding process for training and testing offers
- Track employee nomination, registration, and results
- Collect course feedback from trainees
- Generate reports and views for management visibility
- Automate (to an extent) the process of acquiring training and testing

---

## 3. Who are the intended users?

Based on Section 4.2 (Actors), five user groups are defined:

| Actor | Role |
|---|---|
| **System Administrator** | Full system access; sets up the system for all other user groups (entities, users, locations, TPs, TCs, PMUs) |
| **PMU Administrator** | Manages the entire training/testing workflow: maintains TPs, administers requests, selects TPs, registers employees |
| **TP Administrator** | Maintains own training/testing center information, submits offers, reports attendance and results |
| **Training Coordinator (TC)** | Tracks employee training/testing status, nominates employees for training/testing |
| **GoJ Employee** | Views own training/testing history, submits course evaluations |

Users can be grouped into two categories: administrative users (System Admin, PMU, TP Admin, TC) who manage the system and its workflows, and end users (GoJ Employees) who interact with the system in a limited, read/submit capacity.

Note: Assumption 11 states that for administrative groups (PMU, TP, TC) there is no business need for individual login IDs within those groups. These roles are shared accounts, not personal ones.

---

## 4. What is the standard environment?

Based on Section 2 (Assumptions and Dependencies) and Section 5.1 (System Requirements):

| Aspect | Specification |
|---|---|
| **Application Type** | Web-based (Internet or Intranet) |
| **Browser** | Microsoft Internet Explorer 5.0 or above |
| **Languages** | English or Arabic |
| **Screen Resolution** | 800×600 (optimal) |
| **Excel Export** | Microsoft Excel 2000 or above |
| **Architecture** | 3-tier software architecture with XML support |
| **Runtime Environment** | Hardware, software, and networking supplied and maintained by the client |

Key notes:

- AlliedSoft is explicitly not responsible for the purchase, setup, or configuration of the runtime hardware, software, or networking environment (Assumption 4).
- No specific reporting technology is designated as an e-Government standard; AlliedSoft is free to choose any technique that meets the requirements (Assumption 6).
- Server-side requirements (operating system, database, server software) are not mentioned in the SRS, which is a notable gap.

---

## 5. Functional Requirement Analysis: FR03 – Users Maintenance

> *"Add, update, and delete system administrators and GoJ trainees; trainee information should include gender."*

### Complete

According to the MSD course definition of functional requirements (Slides 09, slide 11), a complete functional requirement must specify: inputs/triggers, outputs/responses, preconditions, actions, postconditions, and side effects. FR03 addresses none of these dimensions. It consists of a single sentence with no trigger event, no expected system output, no preconditions, no postconditions, and no side effects defined. This alone makes it fundamentally incomplete as a functional requirement.

Beyond that structural gap, the requirement is also incomplete in the following ways:

- Only add, update, and delete are mentioned. There is no read/view operation, even though all comparable use cases in the document (e.g., 4.3.1–4.3.31) include it explicitly.
- The data to be stored for system administrators is not specified at all. Only trainee gender is mentioned.
- Password management, account activation/deactivation, and login ID assignment are not mentioned.
- Mandatory vs. optional fields are not distinguished.
- No specification of what happens to dependent data (e.g., training history) when a user is deleted.

### Accurate

The requirement is partially accurate but contains a notable inconsistency:

- The title "Users Maintenance" implies all system users, but the description only covers system administrators and GoJ trainees. TP Administrators and Training Coordinators are system users (defined in Section 4.2) but are absent from this requirement.
- The mention of gender is consistent with the reporting requirements: FR20.16 requires pass rate reports broken down by gender, which provides justification for storing this attribute.
- However, the corresponding use case 4.3.27 (Administrator Maintenance) covers TP Administrators and TCs, not System Administrators. System Administrators have no dedicated use case in the SRS. FR03 therefore does not accurately map to the use cases that are documented.

### Unambiguous

The requirement is ambiguous in multiple ways:

- The term "GoJ trainees" is used here, while "GoJ Employees" is used elsewhere in the document (Section 4.2, use case 4.3.28). It is not stated whether these refer to the same group.
- The word "should" in "trainee information should include gender" is non-committal. It is unclear whether gender is a mandatory field or an optional one.
- It is not specified whether system administrators and trainees are managed in the same interface or through separate screens.
- No definition is given of what constitutes valid user information for either group.

### Traceable

This is the strongest aspect of FR03:

- It has a unique identifier (FR03).
- It can be linked to use case 4.3.28 (GoJ Employee Maintenance, initiated by TC) and partially to 4.3.27 (Administrator Maintenance, covering TP Admins and TCs, not System Admins).
- The gender field connects to FR20.16 (pass rate reports by entity, location, TP, and gender), establishing a cross-requirement dependency.
- The originating stakeholder (MoICT) is traceable through the document's scope section.

Note: Traceability to System Administrators specifically is incomplete because no corresponding use case exists for them.

### Testable

The requirement is partially testable:

| Test Case | Testable? |
|---|---|
| Can a user record be added? | Yes |
| Can a user record be updated? | Yes |
| Can a user record be deleted? | Yes |
| Does the trainee record contain a gender field? | Yes |
| Is gender a mandatory field? | No – not defined |
| What are the valid values for gender? | No – not defined |
| What happens to training history on user deletion? | No – not specified |
| Which fields are required vs. optional? | No – not defined |

### Summary

| Criterion | Assessment | Key Issue |
|---|---|---|
| **Complete** | Weak | No inputs, outputs, preconditions, postconditions, or side effects defined; missing read operation, field definitions, and deletion behavior |
| **Accurate** | Partial | Omits TP Administrators and TCs; System Administrator use case does not exist |
| **Unambiguous** | Weak | "Should", "trainees" vs. "employees", scope and interface unclear |
| **Traceable** | Adequate | Clear ID, partial use case links, gender justified by FR20.16 |
| **Testable** | Partial | Basic CRUD testable; validation rules and field definitions undefined |

Overall, FR03 is a weak requirement. It is partially traceable, which is its main strength, but it lacks the precision and completeness needed to reliably guide development and testing.

---

## 6. Is there a requirement regarding data security?

Yes. Section 5.2 (Security Requirements) defines four user security levels:

| Req. | Role | Access Rights |
|---|---|---|
| SEC01 | PMU | Full system control; ability to update lookup data; ability to generate all reports |
| SEC02 | TP Administrators | Limited to own center; can update attendance/absence and results; can submit offers |
| SEC03 | Training Coordinators | Can administer own employees; can nominate employees for training/testing |
| SEC04 | GoJ Employees | Can view own training/testing history; can submit evaluations only |

These requirements define role-based access control: different users have different levels of visibility and write access depending on their role.

However, the security section is limited in scope. It specifies who can access what, but says nothing about how the system should technically protect that data. The following aspects are absent:

| Missing Aspect | Implication |
|---|---|
| Encryption | No mention of HTTPS or encryption of data in transit or at rest |
| Password policies | No requirements for password strength, complexity, or expiry |
| Session management | No session timeout or session security requirements |
| Audit logging | No requirement to track changes or access events |
| Data backup and recovery | No mention of backup strategies |
| Input validation | No protection against injection attacks or malformed input |

The security section covers only access permissions (SEC01–SEC04). According to the MSD course definition of non-functional requirements (Slides 09, slide 13), security requirements should also address protection against damage and attacks. Neither is mentioned anywhere in the SRS. For a web-based government system handling employee records, this is a significant gap.

---

## 7. Is there a requirement on how the software should be designed?

Yes. Section 3 (High-Level System Architecture) and Section 5.1 (System Requirements) contain design-related requirements.

### Architecture Requirement – SYS03

The most explicit design requirement is:

> *"The application must be designed with a 3-tier software architecture with XML support for interoperability with future e-Government applications."*

The three tiers are defined as:

| Tier | Description |
|---|---|
| Tier 1 (Front-End) | Browser-based UI for visual programming, input specification, and visualization |
| Tier 2 (Middleware) | Distributed, object-based, scalable web server, object broker, and resource manager |
| Tier 3 (Back-End) | Back-end services and resources |

### Other Design-Related Requirements

| Req. | Description |
|---|---|
| SYS01 | Application must be web-based |
| SYS02 | User interface and data must support both English and Arabic |
| DOC02 | A Software Design Specification must be delivered, covering recommended hardware specifications and hardware/software security design |

### What is NOT defined

Despite these requirements, many design aspects are left unspecified:

| Missing Aspect | Implication |
|---|---|
| Database design | No database technology or schema requirements are given |
| Server-side technology | No programming language, framework, or runtime is mandated |
| Security architecture | Referenced in DOC02 but no details appear in the SRS itself |
| Performance requirements | No response times, load capacity, or scalability targets are defined |
| UI/UX guidelines | Beyond language support and browser compatibility, no design standards are specified |

### Assessment

According to the MSD course definition of non-functional requirements (Slides 09, slide 13), technical requirements should also cover performance, scalability, portability, compatibility, reliability, availability, and maintainability. None of these are addressed in the TMS SRS. SYS01 (web-based) and SYS02 (language support) are also present, but SYS03 is the only requirement that imposes an architectural constraint.

Furthermore, according to Slides 09 (slide 19), specific requirements should be defined using tools such as use cases, GUI mockups, UML diagrams, data flow diagrams, entity relationship diagrams, and communication protocols. The TMS SRS uses use cases extensively, but provides no GUI mockups, no UML diagrams, no data model, and no communication protocols, which further limits the completeness of its design-related content.