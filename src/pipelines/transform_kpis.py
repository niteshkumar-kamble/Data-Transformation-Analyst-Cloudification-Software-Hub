
import argparse
import os
import pandas as pd

def compute_kpis(raw_dir: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    bom = pd.read_csv(os.path.join(raw_dir, "bom_products.csv"))
    lic = pd.read_csv(os.path.join(raw_dir, "licenses.csv"))
    ven = pd.read_csv(os.path.join(raw_dir, "vendors.csv"))

    usage = bom.groupby(["product_id", "component"]).size().reset_index(name="usage_count")
    cov = usage.merge(lic[["component", "quantity"]], on="component", how="left")
    cov["license_coverage"] = (cov["quantity"].fillna(0) >= cov["usage_count"]).astype(int)

    vendor_map = lic[["component", "vendor"]].merge(ven, on="vendor", how="left")
    cov = cov.merge(vendor_map[["component", "vendor", "tier"]], on="component", how="left")

    # renewal risk simple heuristic (demo only)
    cov["renewal_risk_score"] = (cov["usage_count"] / cov["usage_count"].max()).fillna(0)                                      * (cov["tier"].map({1: 0.7, 2: 0.5, 3: 0.3}).fillna(0.4))
    cov.to_csv(os.path.join(out_dir, "kpi_coverage.csv"), index=False)
    print("Wrote:", os.path.join(out_dir, "kpi_coverage.csv"))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="raw directory")
    ap.add_argument("--output", required=True, help="output directory")
    args = ap.parse_args()
    compute_kpis(args.input, args.output)
