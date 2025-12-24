
from src.lineage.lineage_builder import build_lineage

def test_lineage_basic():
    recs = [{
        "bom_id": "BOM-1001", "product_id": "PRD-ALPHA", "component": "OpenSSL", "version": "3.0.7",
        "license": "Apache-2.0", "entitlement_id": "LIC-2001", "vendor": "VendorX",
        "catalog_item": "SN-CAT-443", "sap_material_id": "MAT-9001", "windchill_avl_id": "AVL-7001"
    }]
    result = build_lineage(recs)
    assert result[0]["signals"]["catalog_complete"] is True
