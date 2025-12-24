
import json
from typing import List, Dict

def build_lineage(records: List[Dict]) -> List[Dict]:
    # Pass-through demo: ensure required keys exist and build signals
    result = []
    for r in records:
        lineage = {
            "bom_id": r.get("bom_id"),
            "product_id": r.get("product_id"),
            "component": r.get("component"),
            "version": r.get("version"),
            "license": r.get("license"),
            "entitlement_id": r.get("entitlement_id"),
            "vendor": r.get("vendor"),
            "catalog_item": r.get("catalog_item"),
            "sap_material_id": r.get("sap_material_id"),
            "windchill_avl_id": r.get("windchill_avl_id"),
            "signals": {
                "renewal_risk": float(r.get("renewal_risk", 0.5)),
                "compliance_ok": bool(r.get("compliance_ok", True)),
                "catalog_complete": bool(r.get("catalog_item") is not None),
            },
        }
        result.append(lineage)
    return result

if __name__ == "__main__":
    sample = [{
        "bom_id": "BOM-1001", "product_id": "PRD-ALPHA", "component": "OpenSSL", "version": "3.0.7",
        "license": "Apache-2.0", "entitlement_id": "LIC-2001", "vendor": "VendorX", "catalog_item": "SN-CAT-443",
        "sap_material_id": "MAT-9001", "windchill_avl_id": "AVL-7001", "renewal_risk": 0.67, "compliance_ok": True
    }]
    print(json.dumps(build_lineage(sample), indent=2))
