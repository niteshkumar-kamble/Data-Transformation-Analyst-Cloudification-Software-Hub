
# Architecture — Data Flow & Layers

- **Raw**: CSV inputs (BOM, licenses, vendors, SAP, Windchill)
- **Curated**: KPI tables produced by transforms
- **Presentation**: BI dashboards (Power BI / Tableau)
- **Controls**: ServiceNow SHUB validations & workflows

Data movement simulated by local `.adls_sim/<container>/<layer>/` structure.
