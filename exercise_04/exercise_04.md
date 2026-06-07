# Exercise 4 - Cost / Time Estimation
**Sensor Data Collector - Mobile Application**  
Medical Software Development, FHNW 2026

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

- **Widget Point Analysis** (H. Krasemann): counts UI elements
- **Function Point Analysis** (IFPUG): counts external I/O, files, and interface interactions

The averaged Function Point count is then converted to Lines of Code (Java), and **COCOMO (organic)** is used to derive person-months, duration, team size, and costs.

---

## 3  Widget Point Analysis

All widgets visible in the UI mockup (Slide 2/3) are classified and counted:

| Widget / UI Element | Widget Type | Category |
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

> Formula from slides_05, Slide 18 (H. Krasemann): `functionpoints = 2 × widgetpoints`

---

## 4  Function Point Analysis (IFPUG)

The five standard categories are evaluated using **average values** from the FP table (slides_05, Slide 14):

| Category | Elements | Count | Value (avg) | Subtotal |
|---|---|:---:|:---:|:---:|
| External Inputs (EI) | Sensor select, Add, Remove, Start/Stop | 4 | 4 | 16 |
| External Outputs (EO) | Sensor list display, backend confirmation | 2 | 5 | 10 |
| External Inquiries (EQ) | none | 0 | 4 | 0 |
| Internal Logical Files (ILF) | Sensor list (in-memory) | 1 | 10 | 10 |
| External Interface Files (EIF) | Backend service API | 1 | 7 | 7 |
| **Total** | | | | **43 FP** |

$$\text{Function Points (IFPUG)} = 16 + 10 + 0 + 10 + 7 = \mathbf{43\ FP}$$

> Average values used per slides_05, Slide 14: EI=4, EO=5, EQ=4, ILF=10, EIF=7.

### Averaging both methods

| Method | Function Points |
|---|:---:|
| Widget Point Analysis | 16 FP |
| IFPUG Function Point Analysis | 43 FP |
| **Average (used for estimation)** | **29.5 ≈ 30 FP** |

> To reduce estimation uncertainty, both methods were applied and the arithmetic mean was used as approximation. Each method captures a different aspect of the system: Widget Points reflect UI complexity, while IFPUG captures functional interactions including backend communication.

---

## 5  LOC Estimation & COCOMO

### 5.1  Lines of Code (Java)

Programming language: **Java/Android**, 53 LOC per Function Point (slides_05, Slide 17)

$$\text{LOC} = 30\ \text{FP} \times 53\ \frac{\text{LOC}}{\text{FP}} = \mathbf{1'590\ \text{LOC}} \quad (= 1.590\ \text{KDLOC})$$

> Note: This figure does not account for re-use of Android SDK components; actual new code may be less (slides_05, Slide 17).

### 5.2  COCOMO - Organic (Simple)

The app is classified as **organic (simple)**: small team, well-understood domain, straightforward UI, no safety-critical constraints. (slides_05, Slide 21)

| Parameter | Symbol | Value | Source |
|---|:---:|:---:|---|
| Constant | a | 3.2 | Organic, slides_05 Slide 21 |
| Exponent | b | 1.05 | Organic, slides_05 Slide 21 |
| Duration exponent | c | 0.38 | Organic, slides_05 Slide 21 |
| Kilo delivered lines | KDL | 1.590 | Calculated above |
| Effort Adjustment Factor | EAF | 1.00 | No adjustments applied |

$$E_i = a \cdot \text{KDL}^b = 3.2 \times 1.590^{1.05} \approx \mathbf{5.24\ \text{person-months}}$$

$$E = \text{EAF} \times E_i = 1.00 \times 5.24 \approx \mathbf{5.24\ \text{person-months}}$$

$$D = 2.5 \times E^{0.38} = 2.5 \times 5.24^{0.38} \approx \mathbf{4.4\ \text{months}}$$

$$P = \frac{E}{D} = \frac{5.24}{4.4} \approx \mathbf{1.2\ \text{persons (average)}}$$

---

## 6  Phase Distribution

For small software (~2 KDL), the effort distribution is taken from slides_05, Slide 29:
**Design 19 %, Implementation 63 %, Integration & Tests 18 %**

Working time basis: 19 working days × 8 h = **152 h per person-month**

Total effort: 5.24 PM × 152 h/PM = **797 hours**

| Phase | Share | Hours | Activities |
|---|:---:|:---:|---|
| Design | 19 % | 151 h | Architecture, UI design, API contract |
| Implementation | 63 % | 502 h | Android coding, sensor integration, backend communication |
| Integration & Tests | 18 % | 144 h | Unit tests, device testing, bug fixing |
| **Total** | **100 %** | **797 h** | |

---

## 7  Cost Estimation

Hourly rate: **CHF 120.00 / h** (average market rate for a mid-level Android developer in Switzerland, based on typical Swiss software engineering salary levels)

| Cost Category | Amount | Basis / Notes |
|---|---:|---|
| Personal Cost (salary) | CHF 95'640 | 797 h × CHF 120/h |
| Software / Licenses | CHF 500 | Tools, misc. (Android Studio is free) |
| Hardware / Infrastructure | CHF 300 | Test devices, CI/CD server share |
| Risk / Contingency (15 %) | CHF 14'346 | 15 % of personal costs |
| **TOTAL PROJECT COST** | **CHF 110'786** | |

---

## 8  Summary

| Metric | Value |
|---|---:|
| Function Points (Widget Analysis) | 16 FP |
| Function Points (IFPUG) | 43 FP |
| **Function Points (average, used)** | **30 FP** |
| Lines of Code (Java) | 1'590 LOC (1.590 KDLOC) |
| **Effort (COCOMO)** | **5.24 person-months** |
| Total Working Hours | 797 h |
| **Project Duration** | **4.4 months** |
| Average Team Size | 1.2 persons |
| **TOTAL COST** | **CHF 110'786** |

> **Estimation accuracy:** At the specification phase, typical uncertainty is +/-2x (slides_05, Slide 9). This estimate should be revisited after detailed design.

---

## 9  Assumptions & Risks

### Assumptions

- Project type: organic (simple), small team, straightforward requirements
- Programming language: Java (Android), 53 LOC/FP (slides_05, Slide 17)
- COCOMO EAF = 1.00, no adjustment factors applied
- Hourly rate: CHF 120/h, mid-level developer, Switzerland
- Working time: 152 h per person-month (19 working days × 8 h)
- Backend service API is pre-existing; only client-side integration is in scope

### Risks

- Sensor API variability across Android device manufacturers
- Network reliability for data transmission to backend
- Requirement changes (e.g. additional sensor types, data formats)
- Testing on physical devices, limited device availability

> A 15 % contingency has been included in the cost estimate to mitigate the above risks.

---

## References

- R. Tanner, D. Herzig: *Medical Software Development*, FHNW, 2025 - [slides_05_medicalsoftwaredevelopment.pdf](slides_05_medicalsoftwaredevelopment.pdf)
- B. Boehm: COCOMO (COnstructive COst MOdel), organic model parameters
- H. Krasemann: Widget Point Analysis, UI-based function point estimation