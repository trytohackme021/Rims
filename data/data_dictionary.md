# RIMS Central Library: Academic Holdings & Utilization Audit
## Comprehensive Data Dictionary & Schema Documentation

**Institutional Context:** Rajasthan Institute of Management & Sciences (RIMS)  
**Dataset Artifact:** `rims_collection_audit_2026.csv`  
**Sample Dimension:** 300 Representative Audit Units (Physical Monographs, Serial Subscriptions, and Digital Knowledge Bases)  
**Currency Standard:** Indian Rupee (INR / ₹)  
**Analytical Auditor:** Apex Higher Education Advisory Partners (Apex HEAP)

---

### Field Specifications & Metadata Schema

| Field Identifier | Storage Type | Technical Description | Permitted Values & Domain Boundaries | Typical Sample Record |
| :--- | :--- | :--- | :--- | :--- |
| `record_id` | String | Unique catalog audit identifier assigned during physical/digital census. | `ACAD-LIB-1001` through `ACAD-LIB-1300` | `ACAD-LIB-1142` |
| `department` | Categorical | Academic School or administrative department governing the curriculum. | `School of Business`, `School of Technology & Computing`, `School of Commerce & Finance`, `Department of Social Sciences`, `Department of Pure & Applied Sciences` | `School of Business` |
| `resource_type` | Categorical | Structural classification of library acquisition. | `book` (Printed textbook/monograph), `journal` (Periodic academic serial), `e-resource` (Digital aggregated bundle / database) | `journal` |
| `subject_category` | Categorical | Course-aligned academic syllabus topic (25 distinct curricular domains). | Domain topics including *Fintech Innovations*, *Machine Learning & Neural Nets*, *Direct & Indirect Taxation*, *Developmental Sociology*, *Computational Solid State Physics* | `Fintech Innovations` |
| `publication_year` | Integer | Imprint edition year for print items, or current subscription activation year. | Discrete range: `1997` – `2024` | `2011` |
| `times_issued_last_year` | Integer | Total automated circulatory checkouts recorded on the Koha ILS system during the past academic session. | Integer: `0` to `64` (Physical print items only; `0` for digital) | `32` |
| `downloads_last_year` | Integer | Aggregated full-text article and chapter retrieval events logged via IP-authentication proxy. | Integer: `0` to `195` (Serials and e-resources only; `0` for physical books) | `4` |
| `annual_cost` | Integer | Net yearly recurring cost or procurement price in INR (₹). | Monographs: ₹520 – ₹3,450<br>Journals: ₹28,500 – ₹89,000<br>E-Resources: ₹14,500 – ₹46,000 | `₹64,200` |
| `visit_time_slot` | Categorical | Primary operational time band during which transactions or consultations occurred. | `Slot A: 09:00 - 11:30`, `Slot B: 11:30 - 13:30`, `Slot C: 13:30 - 15:30`, `Slot D: 15:30 - 17:00` | `Slot B: 11:30 - 13:30` |
| `student_year` | Categorical | Academic seniority level of the consulting student patron. | `Year 1 (Freshman UG)`, `Year 2 (Sophomore UG)`, `Year 3 (Final Year UG)`, `Master Level (PG-1)`, `Master Level (PG-2)` | `Year 2 (Sophomore UG)` |
| `satisfaction_score` | Integer | Exit-survey sentiment rating captured via digital kiosk on a standardized 5-point Likert scale. | `1` (Extremely Dissatisfied) to `5` (Highly Satisfied) | `2` |

---

### Analytical Integrity & Audit Observations
1. **The Obsolescence Pattern:** 42% of physical books were acquired prior to 2015; these titles exhibit an annual circulation rate of less than 1.4 checkouts per copy. Syllabus-updated editions (2021–2024) circulate at an average rate of 42.6 checkouts annually.
2. **Serial Cost Inefficiency:** 57% of journal subscriptions recorded fewer than 10 downloads across 12 months, creating an unsustainable cost-per-use burden on institutional finances.
3. **Operational Chokepoint:** 72% of recorded footfall is concentrated prior to 13:30, with a steep 67% decline in the late afternoon window due to laboratory and tutorial scheduling conflicts.
