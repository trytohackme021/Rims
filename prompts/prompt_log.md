# Prompt Evolution & Methodological Log
## Institutional Library Realignment Project (RIMS Academic Commons)

**Consultancy Organization:** Apex Higher Education Advisory Partners (Apex HEAP)  
**Scope:** Systematic documentation of prompt engineering progression, technical enhancements, and analytical constraints across core deliverables.

---

### Phase 1: Curated Census Dataset & Metadata Schema

#### Initial Baseline Prompt:
```text
Create a 300-line CSV dataset of library books and journals for a management college with 
departments, circulation, downloads, cost, and satisfaction scores, plus a data dictionary.
```

#### Production-Grade Refined Prompt:
```text
Act as a Senior Academic Data Architect conducting an institutional collection census for 
Rajasthan Institute of Management & Sciences (RIMS).
Generate a statistically coherent, realistic audit sample of exactly 300 records reflecting an 
annual expenditure of ₹18.00 Lakh facing a mandated 30% reduction (ceiling: ₹12.60 Lakh).
Required Specifications:
1. record_id: Discrete alphanumeric format ('ACAD-LIB-1001' to 'ACAD-LIB-1300')
2. department: Distribution across ['School of Business', 'School of Technology & Computing', 
   'School of Commerce & Finance', 'Department of Social Sciences', 'Department of Pure & Applied Sciences']
3. resource_type: ['book', 'journal', 'e-resource'] with ~58% monographs, 27% serials, 15% digital bundles
4. subject_category: Realistic accredited course domains per school
5. publication_year: Monographs spanning 1997–2024; serials 2016–2024
6. times_issued_last_year: Explicitly model the vintage threshold (pre-2015 titles circulate <1.4 times; 
   2021-2024 editions circulate 38-64 times)
7. downloads_last_year: Reflect serial dormancy (57% of journals must log <10 downloads/yr)
8. annual_cost: INR figures reflecting academic procurement (Books: ₹520–₹3,450; Journals: ₹28,500–₹89,000; 
   E-resources: ₹14,500–₹46,000)
9. visit_time_slot: Four operational intervals ['Slot A: 09:00 - 11:30', 'Slot B: 11:30 - 13:30', 
   'Slot C: 13:30 - 15:30', 'Slot D: 15:30 - 17:00'], capturing the late afternoon lab conflict
10. student_year: ['Year 1 (Freshman UG)' through 'Master Level (PG-2)']
11. satisfaction_score: Integer Likert 1-5 correlated with material currency and cohort seniority

Also construct a comprehensive markdown Data Dictionary detailing field domains, constraints, and audit notes.
```

#### Analytical Adjustments & Rationale:
- **School-Level Operational Grounding:** Replaced generic departments with distinct Schools and introduced explicit correlations linking edition vintage to circulation velocity.
- **Seeded Determinism:** Utilized deterministic pseudo-random seeding (Seed: 888) to guarantee reproducible audit metrics that strictly reconcile with institutional budget totals.

---

### Phase 2: Empirical Holdings Diagnostics & Visual Analytics

#### Initial Baseline Prompt:
```text
Write a python script to plot 5 graphs from the library data: departments, publication years, 
costs, visit times, and student satisfaction.
```

#### Production-Grade Refined Prompt:
```text
Act as a Principal Statistical Visualization Consultant using Python, Matplotlib, and Seaborn to 
generate 5 publication-grade 300 DPI analytical charts for the RIMS Academic Council:
1. Figure 1 (School Utilization): Horizontal grouped bar chart contrasting physical checkouts vs 
   electronic downloads across all 5 schools, formatted in an emerald and terracotta palette.
2. Figure 2 (Vintage vs Circulation): Dual-shaded regression scatter plot highlighting the pre-2015 
   vintage threshold against modern syllabus textbook velocity.
3. Figure 3 (Portfolio Cost Efficiency): Strategic four-quadrant scatter matrix isolating dormant 
   serial subscriptions (>₹50k cost / <10 downloads) from high-utility course texts.
4. Figure 4 (Diurnal Flow): Bar chart illustrating the operating slot profile and the 74% collapse 
   after 15:30 caused by laboratory practicals.
5. Figure 5 (Seniority Sentiment Decay): Boxplot distribution tracking satisfaction decline from 
   Freshman UG to Master Level PG-2 scholars.

For every chart, provide exactly 1–2 lines of crisp executive diagnostic insight linking the 
empirical finding directly to the portfolio restructuring decision.
```

#### Analytical Adjustments & Rationale:
- **Decision-Support Framing:** Shifted from passive data displays to strategic quadrant matrices and threshold lines that visually justify the ₹7.35 Lakh serial cancellation.
- **Executive Conciseness:** Structured insights into 1–2 actionable sentences per figure for rapid leadership comprehension.

---

### Phase 3: Policy Advisory Memorandum (Executive Briefing)

#### Initial Baseline Prompt:
```text
Draft a memo summarizing which journals to cancel, which departments don't use the library, 
and three steps to improve library visits.
```

#### Production-Grade Refined Prompt:
```text
Draft a formal executive policy memorandum (exactly 2 pages) from Apex Higher Education Advisory 
Partners to Dr. Arvind Sharma, Principal of RIMS, and the Academic Council.
Systematically address the three mandatory consulting questions:
1. Low Usage Diagnostics: Quantify disengagement across schools, outdated computing/tax books, and 
   the Slot D (15:30–17:00) timetable conflict.
2. Portfolio Restructuring & -30% Budget Balance Sheet: Construct an itemized budget table reconciling 
   historical ₹18.00 Lakh spend down to exactly ₹12.60 Lakh (-₹5.40L savings), specifying the non-renewal 
   of 38 dormant serials and reinvestment into Course Reserve Textbooks (+₹25k) and E-Resources (+₹105k).
3. The SAAF 3-Pillar Turnaround Plan: (Pillar 1: 08:00–21:00 Extended Study Span; Pillar 2: Zero-Waitlist 
   Course Reserve Vault; Pillar 3: Collaborative Ideation Commons).
Conclude with a quantitative accountability verification scorecard for next semester.
```

#### Analytical Adjustments & Rationale:
- **Administrative Rigor:** Formatted as an official institutional advisory memorandum with a fully balanced, rupee-reconciled financial matrix meeting the Principal's exact -30% ceiling.
- **Structural Attribution:** Replaced faculty-student finger-pointing with operational root-cause analysis (class schedules and procurement vintage).

---

### Phase 4: Multi-Channel Bauhaus Campaign Collateral

#### Initial Baseline Prompt:
```text
Make social media and poster copy telling students that the library is open later.
```

#### Production-Grade Refined Prompt:
```text
Formulate an integrated promotional campaign pack for RIMS Central Library adhering to a 
modernist Swiss/Bauhaus editorial visual standard:
1. Deliverable A: Instagram Square Post (1080×1080 px).
   - Headline: 'YOUR SYLLABUS. FRESH OFF THE PRESS.'
   - Audit Benchmark: '42% of older holdings averaged <1.4 checkouts. Stocked 2024 syllabus editions 
     and open until 9:00 PM!'
   - CTA: 'Claim your study pod tonight • Weekdays 08:00 to 21:00.'
2. Deliverable B: Campus Concourse Noticeboard Poster (A3 Portrait).
   - Headline: 'RECLAIM YOUR STUDY SPAN.'
   - Audit Benchmark: 'Turnstile audit showed visits plunged 74% after 3:30 PM due to labs. Extended 
     to 9:00 PM!'
   - CTA: 'Check out your 2024 prescribed textbook from the Course Reserve Vault today.'

Deliver:
- Complete Canva AI generation prompts for editorial architectural imagery
- Clean, standalone SVG vector assets with zero XML errors
- Interactive preview interface
```

#### Analytical Adjustments & Rationale:
- **Rubric Compliance:** Guaranteed that each marketing asset features a clear message, explicit CTA, and verified analysis data point.
- **Vector Production Delivery:** Delivered verified SVG and HTML vector layouts ready for campus dissemination.
