#!/usr/bin/env python3
"""Find In-N-Out locations within walking distance of Tesla Superchargers."""

import json
from pathlib import Path
from geopy.distance import geodesic

DATA_DIR = Path(__file__).parent.parent / "data"

# Maximum walking distance in meters (~5 minute walk)
MAX_DISTANCE_METERS = 400


def load_json(filename):
    with open(DATA_DIR / filename) as f:
        return json.load(f)


def calculate_distance(loc1, loc2):
    """Calculate distance between two locations in meters."""
    coords1 = (loc1["lat"], loc1["lng"])
    coords2 = (loc2["lat"], loc2["lng"])
    return geodesic(coords1, coords2).meters


def find_nearby_pairs():
    """Find In-N-Out locations near Tesla Superchargers."""
    superchargers = load_json("superchargers.json")
    in_n_outs = load_json("in_n_out.json")

    pairs = []

    for charger in superchargers:
        if charger["lat"] is None or charger["lng"] is None:
            continue

        for ino in in_n_outs:
            if ino["lat"] is None or ino["lng"] is None:
                continue

            distance = calculate_distance(charger, ino)

            if distance <= MAX_DISTANCE_METERS:
                pairs.append({
                    "supercharger": {
                        "name": charger["name"],
                        "address": charger["address"],
                        "city": charger["city"],
                        "lat": charger["lat"],
                        "lng": charger["lng"],
                        "stalls": charger["stalls"],
                    },
                    "in_n_out": {
                        "name": ino["name"],
                        "address": ino["address"],
                        "city": ino["city"],
                        "lat": ino["lat"],
                        "lng": ino["lng"],
                    },
                    "distance_meters": round(distance),
                    "walking_minutes": round(distance / 80),  # ~80m per minute walking
                })

    # Sort by distance
    pairs.sort(key=lambda x: x["distance_meters"])

    return pairs


def main():
    print(f"Finding In-N-Out locations within {MAX_DISTANCE_METERS}m of Superchargers...")
    pairs = find_nearby_pairs()

    output_file = DATA_DIR / "nearby_pairs.json"
    with open(output_file, "w") as f:
        json.dump(pairs, f, indent=2)

    print(f"\nFound {len(pairs)} Supercharger + In-N-Out combinations!\n")

    for pair in pairs:
        sc = pair["supercharger"]
        ino = pair["in_n_out"]
        print(f"📍 {sc['name']}, {sc['city']}")
        print(f"   🍔 {ino['address']}, {ino['city']}")
        print(f"   📏 {pair['distance_meters']}m (~{pair['walking_minutes']} min walk)")
        print()

    print(f"Saved to {output_file}")


if __name__ == "__main__":
    main()
