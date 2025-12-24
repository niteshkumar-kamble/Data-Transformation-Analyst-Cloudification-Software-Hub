
# Cloudification & Software Hub — Hands-on Projects

> A practical, end-to-end portfolio for the **Data & Transformation Analyst** role focusing on **3rd-party BOM software & cloud products**: KPIs, compliance, lineage, BI dashboards, ServiceNow controls, and Azure Data Lake pipelines.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Tech Stack](https://img.shields.io/badge/stack-SQL%20%7C%20Python%20%7C%20Power%20BI%20%7C%20Tableau%20%7C%20Azure%20Data%20Lake%20%7C%20ServiceNow-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📁 Repository Structure

```
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
│   │   └── BOM_Software_Compliance.pbix (placeholder)
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
```

---

## 🎯 Objectives

1. **KPIs for 3rd-party BOM software**: usage (by product/BOM), license/entitlement status, renewal risk, vendor spend, savings pipeline, standardization/adoption.
2. **ServiceNow (SHUB) controls**: catalog completeness, AVL checks (Windchill ↔ SAP), compliance signals tied to BOM lineage.
3. **Data lineage** across **Windchill, SAP, Azure Data Lake, ServiceNow** with traceability.
4. **Digital transformation artifacts**: integrations, features, dashboards, UAT/demos.
5. **Adoption & change enablement**: materials, developer/buyer coaching.

---

## 🧪 Projects Overview

### 1) KPI Modeling & Analytics
- **Goal**: Build KPI layer for BOM-scoped third-party software.
- **Input**: `bom_products.csv`, `licenses.csv`, `vendors.csv`
- **Output**: KPI parquet/csv in `data/processed/` + interactive dashboard.
- **Notebook**: `notebooks/01_kpi_modeling.ipynb`

**Example metrics:**
- `UsageByProduct`: count of software components per BOM/product
- `LicenseCoverage`: % mapped entitlements vs. usage
- `RenewalRiskScore`: weighted risk (expiry proximity × usage criticality × vendor tier)
- `SavingsPipeline`: sum of potential savings from standardization

---

### 2) Data Quality Rules & Compliance Signals
- **Goal**: Implement data quality checks aligned to BOM lineage & SHUB controls.
- **Input**: `sap_materials.csv`, `windchill_avl.csv`
- **Output**: DQ report (`data/processed/dq_report.csv`)
- **Notebook**: `notebooks/02_data_quality_rules.ipynb`
- **Script**: `src/quality/dq_checks.py`

**Checks include:**
- Missing/invalid AVL mapping (Windchill ↔ SAP)
- Catalog completeness (ServiceNow item present)
- Entitlement mismatch (license > usage or missing)
- Vendor tier policy exceptions
- Orphaned components (no BOM linkage)

---

### 3) Lineage & Traceability Mapping
- **Goal**: Construct lineage graph linking BOM → Component → License → Vendor → Catalog → Entitlement.
- **Input**: combined datasets; optional graph store
- **Output**: lineage JSON & visualization
- **Notebook**: `notebooks/03_lineage_mapping.ipynb`
- **Script**: `src/lineage/lineage_builder.py`

**Example lineage record:**
```json
{
  "bom_id": "BOM-10293",
  "product_id": "PRD-ALPHA",
  "component": "OpenSSL",
  "version": "3.0.7",
  "license": "Apache-2.0",
  "entitlement_id": "LIC-8732",
  "vendor": "VendorX",
  "catalog_item": "SN-CAT-443",
  "sap_material_id": "MAT-99821",
  "windchill_avl_id": "AVL-771",
  "signals": {
    "renewal_risk": 0.67,
    "compliance_ok": true,
    "catalog_complete": true
  }
}
```

---

### 4) Azure Data Lake (ADLS) Ingest & Transform
- **Goal**: Simulate/implement ingestion to ADLS + transforms for KPI tables.
- **Scripts**: `src/pipelines/adls_ingest.py`, `src/pipelines/transform_kpis.py`
- **Docs**: `docs/architecture.md`

**CLI example:**
```bash
python src/pipelines/adls_ingest.py --source data/raw --container bom-analytics --prefix raw/
python src/pipelines/transform_kpis.py --input raw/ --output curated/
```

---

### 5) ServiceNow (SHUB) Catalog Controls
- **Goal**: Define SHUB control patterns & pseudo-scripts for catalog completeness and entitlement linkage.
- **Doc**: `src/servicenow/catalog_controls_example.md`

**Control examples:**
- **Catalog Completeness**: Ensure each BOM component has a SHUB catalog item.
- **AVL Consistency**: Validate AVL entries match SAP materials.
- **Entitlement Binding**: Require entitlement link before approval workflow.

---

### 6) BI Dashboards (Power BI / Tableau)
- **Goal**: Publish BOM KPIs + compliance signals for stakeholders.
- **Artifacts**: `dashboards/powerbi/` and `dashboards/tableau/`
- **Docs**: `docs/kpi_definitions.md`

**Recommended visuals:**
- Renewal Risk by Vendor/Product (heatmap)
- License Coverage Trend (line)
- Savings Pipeline (bar)
- Catalog Completeness (donut)
- AVL Exceptions (table)

---

## ⚙️ Setup

### Prerequisites
- Python 3.10+
- Power BI Desktop or Tableau Public
- (Optional) Azure CLI for ADLS simulation
- (Optional) ServiceNow Dev Instance (for sandbox testing)

### Install
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # fill in ADLS/account keys if applicable
```

---

## 🧪 Testing

Run unit tests for DQ & lineage:
```bash
pytest -q
```

---

## 🧭 Roadmap

- [ ] Integrate real ADLS Gen2 with SAS credentials
- [ ] Add Power BI dataflows for curated tables
- [ ] ServiceNow API automation (catalog completeness, entitlement validation)
- [ ] Renewal risk model v2 (time-to-expiry + usage criticality + vendor risk)
- [ ] Windchill/SAP connectors (mock → connector abstraction)

---

## 📜 License

This project is licensed under the **MIT License** — see `LICENSE` for details.
