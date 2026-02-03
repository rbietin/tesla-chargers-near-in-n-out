#!/usr/bin/env python3
"""Fetch Tesla Supercharger locations in California."""

import json
import requests
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def fetch_superchargers():
    """Fetch Tesla Superchargers in California from supercharge.info API."""
    # supercharge.info provides a public API with all Tesla Supercharger data
    url = "https://supercharge.info/service/supercharge/allSites"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    all_sites = response.json()

    # Filter for California Superchargers that are open
    california_chargers = [
        site for site in all_sites
        if site.get("address", {}).get("state") == "CA"
        and site.get("status") == "OPEN"
    ]

    # Extract relevant fields
    chargers = []
    for site in california_chargers:
        chargers.append({
            "name": site.get("name"),
            "address": site.get("address", {}).get("street"),
            "city": site.get("address", {}).get("city"),
            "lat": site.get("gps", {}).get("latitude"),
            "lng": site.get("gps", {}).get("longitude"),
            "stalls": site.get("stallCount"),
        })

    return chargers


def main():
    DATA_DIR.mkdir(exist_ok=True)

    print("Fetching Tesla Superchargers in California...")
    chargers = fetch_superchargers()

    output_file = DATA_DIR / "superchargers.json"
    with open(output_file, "w") as f:
        json.dump(chargers, f, indent=2)

    print(f"Found {len(chargers)} Superchargers in California")
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    main()
