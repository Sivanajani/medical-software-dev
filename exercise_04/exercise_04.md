# Exercise 4 – Cost / Time Estimation
**Sensor Data Collector – Mobile Application**  
Medical Software Development · FHNW · 2025

---

## 1  Project Overview

A mobile application is to be developed that allows users to collect sensor data from a smartphone. The key functional requirements are:

- Select a sensor from a dropdown (Sensor Select Box)
- Add selected sensors to a list (Add Sensor button); duplicates are ignored
- Remove a marked sensor from the list (Remove Sensor button)
- Start / Stop data collection (toggle button); during collection, list modifications are locked
- Upon stopping, the collected data is transmitted to a backend service

The application has a single-screen UI (see mockup, Slide 2/3) and communicates with an external backend.

---

## 2  Estimation Method

Two complementary algorithmic methods from the lecture (slides_05) are applied and their results averaged:

- **Widget Point Analysis** (H. Krasemann) — counts UI elements
- **Function Point Analysis** (IFPUG) — counts external I/O, files, and interface interactions

The averaged Function Point count is then converted to Lines of Code (Java), and **COCOMO (organic)** is used to derive person-months, duration, team size, and costs.

---

## 3  Widget Point Analysis

All widgets in the UI mockup (Slide 2/3) are classified and counted:

| Widget / UI Element | Type | Category |
|---|---|---|
| Sensor Select Box (Combobox) | Input widget | Input |
| Add Sensor (Pushbutton) | Input widget | Input |
| Remove Sensor (Pushbutton) | Input widget | Input |
| Start/Stop Collecting Data (Pushbutton) | Input widget | Input |
| Selected Sensors (List) | Composite widget | Composite |
| "Sensor Data Collector" (Label) | Describing widget | Describing |
| "Selected Sensors" (Label) | Describing widget | Describing |
| App Window | Describing widget | Describing |

| Category | Count |
|---|:---:|
| Input widgets | 4 |
| Describing widgets | 3 |
| Composite widgets | 1 |
| Menu widgets | 0 |
| **Total Widget Points** | **8** |

$$\text{Function Points (Widget)} = 8 \times 2 = \mathbf{16\ FP}$$

> Formula from slides_05, Slide 18: `functionpoints = 2 × widgetpoints`

---

## 4  Function Point Analysis (IFPUG)

The five standard categories are evaluated using **average values** (slides_05, Slide 14):

| Category | Elements | Count | Value (avg) | Subtotal |
|---|---|:---:|:---:|:---:|
| External Inputs (EI) | Sensor select, Add, Remove, Start/Stop | 4 | 4 | 16 |
| External Outputs (EO) | Sensor list display, backend confirmation | 2 | 5 | 10 |
| External Inquiries (EQ) | — | 0 | 4 | 0 |
| Internal Logical Files (ILF) | Sensor list (in-memory) | 1 | 7 | 7 |
| External Interface Files (EIF) | Backend service API | 1 | 5 | 5 |
| **Total** | | | | **38 FP** |

$$\text{Function Points (IFPUG)} = 16 + 10 + 0 + 7 + 5 = \mathbf{38\ FP}$$

### Averaging both methods

| Method | Function Points |
|---|:---:|
| Widget Point Analysis | 16 FP |
| IFPUG Function Point Analysis | 38 FP |
| **Average (used for estimation)** | **27 FP** |

> Both methods serve as a cross-check; their average provides a balanced basis for the LOC and COCOMO calculation.

---

## 5  LOC Estimation & COCOMO

### 5.1  Lines of Code (Java)

Programming language: **Java/Android** → **53 LOC per Function Point** (slides_05, Slide 17)

$$\text{LOC} = 27\ \text{FP} \times 53\ \frac{\text{LOC}}{\text{FP}} = \mathbf{1{,}431\ \text{LOC}} \quad (= 1.431\ \text{KDLOC})$$

> Note: This figure does not account for re-use of Android SDK components; actual new code may be less.

### 5.2  COCOMO – Organic (Simple)

The app is classified as **organic (simple)**: small team, well-understood domain, straightforward UI, no safety-critical constraints.

| Parameter | Symbol | Value | Source |
|---|:---:|:---:|---|
| Constant a | a | 3.2 | Organic (COCOMO table, slides_05) |
| Exponent b | b | 1.05 | Organic (COCOMO table, slides_05) |
| Duration exponent c | c | 0.38 | Organic (COCOMO table, slides_05) |
| Kilo delivered lines | KDL | 1.431 | Calculated above |
| Effort Adjustment Factor | EAF | 1.00 | Conservative (no adjustments) |

$$E_i = 3.2 \times 1.431^{1.05} \approx \mathbf{4.67\ \text{person-months}}$$

$$E = \text{EAF} \times E_i = 1.00 \times 4.67 \approx \mathbf{4.67\ \text{person-months}}$$

$$D = 2.5 \times E^{0.38} = 2.5 \times 4.67^{0.38} \approx \mathbf{4.2\ \text{months}}$$

$$P = \frac{E}{D} = \frac{4.67}{4.2} \approx \mathbf{1.1\ \text{persons (average)}}$$

---

## 6  Phase Distribution

For small software (<2 KDLOC), slides_05 Slide 29: **Design 19%, Implementation 63%, Integration & Tests 18%**

Total effort: 4.67 PM × 152 h/PM = **710 hours**

| Phase | Share | Hours | Activities |
|---|:---:|:---:|---|
| Design | 19 % | 135 h | Architecture, UI design, API contract |
| Implementation | 63 % | 447 h | Android coding, sensor integration, backend communication |
| Integration & Tests | 18 % | 128 h | Unit tests, device testing, bug fixing |
| **Total** | **100 %** | **710 h** | |

> Working time basis: 19 working days × 8 h = 152 h per person-month

---

## 7  Cost Estimation

Hourly rate: **CHF 120.– / h** (mid-level Android developer, Switzerland)

| Cost Category | Amount | Basis / Notes |
|---|---:|---|
| Personal Cost (salary) | CHF 85,200 | 710 h × CHF 120/h |
| Software / Licenses | CHF 500 | Tools, misc. (Android Studio is free) |
| Hardware / Infrastructure | CHF 300 | Test devices, CI/CD server share |
| Risk / Contingency (15 %) | CHF 12,780 | 15% of personal costs |
| **TOTAL PROJECT COST** | **CHF 98,780** | |

---

## 8  Summary

| Metric | Value |
|---|---:|
| Function Points (Widget Analysis) | 16 FP |
| Function Points (IFPUG) | 38 FP |
| **Function Points (average, used)** | **27 FP** |
| Lines of Code (Java) | 1,431 LOC (1.431 KDLOC) |
| **Effort (COCOMO)** | **4.67 person-months** |
| Total Working Hours | 710 h |
| **Project Duration** | **4.2 months** |
| Average Team Size | 1.1 persons |
| **TOTAL COST** | **CHF 98,780** |

> **Estimation accuracy:** At the specification phase, typical uncertainty is ±2× (slides_05, Slide 9). This estimate should be revisited after detailed design.

---

## 9  Assumptions & Risks

### Assumptions
- Project type: organic (simple) — small team, straightforward requirements
- Programming language: Java (Android) → 53 LOC/FP
- COCOMO EAF = 1.00 (no adjustment factors — conservative)
- Hourly rate: CHF 120/h (mid-level developer, Switzerland)
- Working time: 152 h per person-month (19 working days × 8 h)
- Backend service API is pre-existing; only client-side integration is in scope

### Risks
- Sensor API variability across Android device manufacturers
- Network reliability for data transmission to backend
- Requirement changes (e.g. additional sensor types, data formats)
- Testing on physical devices — limited device availability

> A 15% contingency has been included in the cost estimate to mitigate the above risks.

---

## References

- R. Tanner, D. Herzig: *Medical Software Development*, FHNW, 2025 — `slides_05_medicalsoftwaredevelopment.pdf`
- B. Boehm: COCOMO (COnstructive COst MOdel) — organic model parameters
- H. Krasemann: Widget Point Analysis — UI-based function point estimation
- IFPUG: Function Point Analysis standard — www.ifpug.org