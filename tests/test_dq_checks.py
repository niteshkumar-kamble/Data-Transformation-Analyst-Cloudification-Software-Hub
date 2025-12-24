
from src.quality.dq_checks import check_catalog_completeness

def test_catalog_completeness_minimal():
    rows = [{"component": "OpenSSL", "catalog_item": "SN-CAT-443"}]
    assert check_catalog_completeness(rows) == []

def test_catalog_completeness_missing():
    rows = [{"component": "Log4j", "catalog_item": None}]
    errs = check_catalog_completeness(rows)
    assert len(errs) == 1 and "Log4j" in errs[0]
