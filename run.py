#!/usr/bin/env python3
"""Main script to run the full pipeline."""

import subprocess
import sys


def run_script(script_name):
    """Run a Python script and check for errors."""
    print(f"\n{'='*60}")
    print(f"Running {script_name}...")
    print('='*60)

    result = subprocess.run(
        [sys.executable, f"src/{script_name}"],
        capture_output=False,
    )

    if result.returncode != 0:
        print(f"Error running {script_name}")
        sys.exit(1)


def main():
    print("Tesla Superchargers Near In-N-Out Finder")
    print("========================================")

    # Step 1: Fetch Supercharger locations
    run_script("fetch_superchargers.py")

    # Step 2: Fetch In-N-Out locations
    run_script("fetch_in_n_out.py")

    # Step 3: Find nearby pairs
    run_script("find_nearby.py")

    # Step 4: Export to Google Maps formats
    run_script("export_to_google_maps.py")

    print("\n" + "="*60)
    print("Done! Check the data/ folder for output files.")
    print("="*60)


if __name__ == "__main__":
    main()
