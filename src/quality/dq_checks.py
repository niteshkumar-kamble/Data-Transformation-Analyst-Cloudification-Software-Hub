
from typing import List, Dict

def check_catalog_completeness(rows: List[Dict]) -> List[str]:
    errors = []
    for i, r in enumerate(rows):
        if not r.get("catalog_item"):
            errors.append(f"Row {i}: missing catalog_item for component {r.get('component')}")
    return errors

def check_avl_consistency(avl_rows: List[Dict]) -> List[str]:
    errors = []
    for r in avl_rows:
        if not r.get("sap_material_id"):
            errors.append(f"AVL {r.get('windchill_avl_id')} missing SAP mapping")
    return errors
