
# Cloudification & Software Hub — Hands-on Projects

> A practical, end-to-end portfolio for the **Data & Transformation Analyst** role focusing on **3rd-party BOM software & cloud products**: KPIs, compliance, lineage, BI dashboards, ServiceNow controls, and Azure Data Lake pipelines.

!Status
!Tech Stack
!License

---

## 📁 Repository Structure
.
├── data/
│   ├── raw/
│   │   ├── bom_products.csv
│   │   ├── licenses.csv
│   │   ├── vendors.csv
│   │   ├── sap_materials.csv
│   │   └── windchill_avl.csv
│   └── processed/
├── notebooks/
│   ├── 01_kpi_modeling.ipynb
│   ├── 02_data_quality_rules.ipynb
│   ├── 03_lineage_mapping.ipynb
│   └── 04_renewal_risk_scoring.ipynb
├── src/
│   ├── pipelines/
│   │   ├── adls_ingest.py
│   │   └── transform_kpis.py
│   ├── quality/
│   │   └── dq_checks.py
│   ├── lineage/
│   │   └── lineage_builder.py
│   ├── servicenow/
│   │   └── catalog_controls_example.md
│   └── utils.py
├── dashboards/
│   ├── powerbi/
│   │   └── BOM_Software_Compliance.pbix
│   └── tableau/
│       └── BOM_Software_Compliance.twb
├── docs/
│   ├── architecture.md
│   ├── kpi_definitions.md
│   └── change_management.md
├── tests/
│   ├── test_dq_checks.py
│   └── test_lineage.py
├── .env.example
├── requirements.txt
├── LICENSE
└── README.md
