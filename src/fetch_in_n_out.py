#!/usr/bin/env python3
"""Fetch In-N-Out Burger locations in California using OpenStreetMap."""

import json
import requests
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

# Overpass API query for In-N-Out locations in California
# Includes nodes, ways, and relations with center coordinates
OVERPASS_QUERY = """
[out:json];
area["ISO3166-2"="US-CA"]->.ca;
(
  node["brand"="In-N-Out Burger"](area.ca);
  way["brand"="In-N-Out Burger"](area.ca);
  rel["brand"="In-N-Out Burger"](area.ca);
);
out center;
"""


def fetch_in_n_out_locations():
    """Fetch In-N-Out locations from OpenStreetMap via Overpass API."""
    url = "https://overpass-api.de/api/interpreter"

    response = requests.post(url, data=OVERPASS_QUERY, timeout=60)
    response.raise_for_status()

    data = response.json()
    elements = data.get("elements", [])

    stores = []
    for elem in elements:
        tags = elem.get("tags", {})

        # Get coordinates - nodes have lat/lon directly, ways/relations have center
        if elem.get("type") == "node":
            lat = elem.get("lat")
            lng = elem.get("lon")
        else:
            center = elem.get("center", {})
            lat = center.get("lat")
            lng = center.get("lon")

        if lat is None or lng is None:
            continue

        stores.append({
            "name": f"In-N-Out #{tags.get('ref', tags.get('store_number', 'Unknown'))}",
            "address": f"{tags.get('addr:housenumber', '')} {tags.get('addr:street', '')}".strip(),
            "city": tags.get("addr:city", ""),
            "lat": lat,
            "lng": lng,
        })

    return stores


def main():
    DATA_DIR.mkdir(exist_ok=True)

    print("Fetching In-N-Out locations in California from OpenStreetMap...")
    stores = fetch_in_n_out_locations()

    output_file = DATA_DIR / "in_n_out.json"
    with open(output_file, "w") as f:
        json.dump(stores, f, indent=2)

    print(f"Found {len(stores)} In-N-Out locations in California")
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    main()
