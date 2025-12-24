
# ServiceNow (SHUB) Catalog Controls — Examples

> Pseudo-scripts and patterns for catalog completeness, AVL validation, and entitlement binding.

## 1. Catalog Completeness (Business Rule)
- Trigger: On insert/update of BOM component record
- Rule: Ensure `catalog_item` field is populated; otherwise, flag `catalog_complete=false`

## 2. AVL Consistency (Scheduled Job)
- Validate Windchill AVL entries have matching SAP materials; create incident/task if mismatch.

## 3. Entitlement Binding (Flow Designer)
- On request submission, check entitlement linkage; block approval until present.

*Note: Replace with actual GlideRecord queries / Script Includes according to your schema.*
