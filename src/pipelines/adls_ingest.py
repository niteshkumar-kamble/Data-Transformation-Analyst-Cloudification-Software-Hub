
import argparse, os, shutil

def ingest_local_to_simulated_adls(source: str, container: str, prefix: str = "raw/"):
    # This simulates ADLS by copying to a local folder named after the container
    target_root = os.path.join(".adls_sim", container, prefix)
    os.makedirs(target_root, exist_ok=True)
    for root, _, files in os.walk(source):
        for fn in files:
            src_fp = os.path.join(root, fn)
            rel = os.path.relpath(src_fp, source)
            dst_fp = os.path.join(target_root, rel)
            os.makedirs(os.path.dirname(dst_fp), exist_ok=True)
            shutil.copy2(src_fp, dst_fp)
            print(f"Copied {src_fp} -> {dst_fp}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--container", required=True)
    ap.add_argument("--prefix", default="raw/")
    args = ap.parse_args()
    ingest_local_to_simulated_adls(args.source, args.container, args.prefix)
