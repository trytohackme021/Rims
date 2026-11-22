import pandas as pd
import numpy as np
import random

# Unique seed distinct from any previous generation
np.random.seed(888)
random.seed(888)

# Institutional Schools / Departments
dept_mapping = {
    "School of Business": [
        "Corporate Valuation", "Consumer Behavior Analytics", "Strategic Leadership", 
        "Supply Chain Modeling", "Fintech Innovations", "Human Resource Systems"
    ],
    "School of Technology & Computing": [
        "Distributed Systems", "Machine Learning & Neural Nets", "Full-Stack Software Architecture", 
        "Cryptography & Network Defense", "Quantum Algorithms", "Outdated System Architecture (PDP/VAX/Pascal)"
    ],
    "School of Commerce & Finance": [
        "Advanced Forensic Accounting", "Direct & Indirect Taxation", "International Trade Logistics", 
        "Equity Research & Portfolio Analysis", "Company Auditing Principles"
    ],
    "Department of Social Sciences": [
        "Developmental Sociology", "Comparative Indian Politics", "Contemporary History & Global Studies", 
        "Linguistic Anthropology", "Public Policy Analysis"
    ],
    "Department of Pure & Applied Sciences": [
        "Stochastic Differential Equations", "Computational Solid State Physics", 
        "Industrial Green Chemistry", "Bioinformatics & Genomic Analytics"
    ]
}

departments = list(dept_mapping.keys())
dept_probabilities = [0.34, 0.31, 0.16, 0.10, 0.09]

resource_types = ["book", "journal", "e-resource"]
resource_weights = [0.58, 0.27, 0.15]

# Unique time slots matching operational intervals
time_slots = [
    "Slot A: 09:00 - 11:30", 
    "Slot B: 11:30 - 13:30", 
    "Slot C: 13:30 - 15:30", 
    "Slot D: 15:30 - 17:00"
]
time_slot_weights = [0.33, 0.39, 0.18, 0.10]

student_cohorts = [
    "Year 1 (Freshman UG)", 
    "Year 2 (Sophomore UG)", 
    "Year 3 (Final Year UG)", 
    "Master Level (PG-1)", 
    "Master Level (PG-2)"
]
cohort_weights = [0.26, 0.24, 0.22, 0.14, 0.14]

records = []

for idx in range(1, 301):
    record_id = f"ACAD-LIB-{1000 + idx}"
    dept = np.random.choice(departments, p=dept_probabilities)
    res_type = np.random.choice(resource_types, p=resource_weights)
    subject = random.choice(dept_mapping[dept])
    
    if res_type == "book":
        # 42% older holdings (1997 - 2014), 58% newer (2015 - 2024)
        if random.random() < 0.42:
            pub_year = random.randint(1997, 2014)
            # Stagnant circulation for obsolete books
            times_issued = random.choices([0, 1, 2, 4], weights=[0.68, 0.18, 0.10, 0.04])[0]
        else:
            pub_year = random.randint(2015, 2024)
            if pub_year >= 2021:
                times_issued = random.randint(28, 64)
            else:
                times_issued = random.randint(6, 26)
        downloads = 0
        annual_cost = int(random.randint(520, 3450))
        
    elif res_type == "journal":
        pub_year = random.randint(2016, 2024)
        times_issued = 0
        # High dormancy in journal subscriptions (scenario fact: many <10 downloads)
        if random.random() < 0.62:
            downloads = random.randint(0, 9)
        else:
            downloads = random.randint(11, 48)
        annual_cost = int(random.randint(28500, 89000))
        
    else: # e-resource
        pub_year = random.randint(2019, 2024)
        times_issued = 0
        downloads = random.randint(22, 195)
        annual_cost = int(random.randint(14500, 46000))
        
    time_slot = np.random.choice(time_slots, p=time_slot_weights)
    cohort = np.random.choice(student_cohorts, p=cohort_weights)
    
    # Satisfaction score calculation based on utility
    if res_type == "book" and pub_year < 2015:
        sat_score = random.choices([1, 2, 3], weights=[0.58, 0.32, 0.10])[0]
    elif res_type == "journal" and downloads < 10:
        sat_score = random.choices([1, 2, 3], weights=[0.45, 0.38, 0.17])[0]
    elif pub_year >= 2021:
        sat_score = random.choices([3, 4, 5], weights=[0.12, 0.52, 0.36])[0]
    else:
        sat_score = random.choices([2, 3, 4], weights=[0.28, 0.54, 0.18])[0]
        
    records.append({
        "record_id": record_id,
        "department": dept,
        "resource_type": res_type,
        "subject_category": subject,
        "publication_year": pub_year,
        "times_issued_last_year": times_issued,
        "downloads_last_year": downloads,
        "annual_cost": annual_cost,
        "visit_time_slot": time_slot,
        "student_year": cohort,
        "satisfaction_score": sat_score
    })

df = pd.DataFrame(records)
out_csv = r"C:\Users\Asus\.gemini\antigravity\scratch\rims_library_consulting_taskforce\data\rims_collection_audit_2026.csv"
df.to_csv(out_csv, index=False)

print(f"Dataset successfully created at: {out_csv}")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print(f"Total Expenditure in Sample: INR {df['annual_cost'].sum():,}")
print(f"Books: {(df['resource_type']=='book').sum()}, Journals: {(df['resource_type']=='journal').sum()}, E-resources: {(df['resource_type']=='e-resource').sum()}")
print(f"Journals with <10 downloads: {((df['resource_type']=='journal') & (df['downloads_last_year'] < 10)).sum()}")
