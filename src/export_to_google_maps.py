#!/usr/bin/env python3
"""Export nearby pairs to formats suitable for Google Maps."""

import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_pairs():
    with open(DATA_DIR / "nearby_pairs.json") as f:
        return json.load(f)


def export_csv():
    """Export to CSV format that can be imported to Google My Maps."""
    pairs = load_pairs()

    output_file = DATA_DIR / "superchargers_with_in_n_out.csv"

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        # Header for Google My Maps import
        writer.writerow([
            "Name",
            "Description",
            "Latitude",
            "Longitude",
        ])

        for pair in pairs:
            sc = pair["supercharger"]
            ino = pair["in_n_out"]

            name = f"Tesla SC + In-N-Out: {sc['city']}"
            description = (
                f"Supercharger: {sc['name']} ({sc['stalls']} stalls)\\n"
                f"In-N-Out: {ino['address']}\\n"
                f"Walking distance: {pair['distance_meters']}m (~{pair['walking_minutes']} min)"
            )

            writer.writerow([
                name,
                description,
                sc["lat"],
                sc["lng"],
            ])

    print(f"Exported {len(pairs)} locations to {output_file}")
    print("\nTo import to Google Maps:")
    print("1. Go to https://www.google.com/mymaps")
    print("2. Create a new map")
    print("3. Click 'Import' and select the CSV file")
    print("4. Choose 'Latitude' and 'Longitude' as position columns")
    print("5. Choose 'Name' as title column")


def export_kml():
    """Export to KML format for Google Earth/Maps."""
    pairs = load_pairs()

    kml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Tesla Superchargers near In-N-Out</name>
    <description>Tesla Superchargers within walking distance of In-N-Out Burger in California</description>
'''

    for pair in pairs:
        sc = pair["supercharger"]
        ino = pair["in_n_out"]

        kml_content += f'''
    <Placemark>
      <name>Tesla SC + In-N-Out: {sc['city']}</name>
      <description><![CDATA[
        <b>Supercharger:</b> {sc['name']} ({sc['stalls']} stalls)<br>
        <b>In-N-Out:</b> {ino['address']}<br>
        <b>Walking distance:</b> {pair['distance_meters']}m (~{pair['walking_minutes']} min)
      ]]></description>
      <Point>
        <coordinates>{sc['lng']},{sc['lat']},0</coordinates>
      </Point>
    </Placemark>
'''

    kml_content += '''
  </Document>
</kml>'''

    output_file = DATA_DIR / "superchargers_with_in_n_out.kml"
    with open(output_file, "w") as f:
        f.write(kml_content)

    print(f"Exported KML to {output_file}")


def main():
    print("Exporting to Google Maps formats...\n")
    export_csv()
    print()
    export_kml()


if __name__ == "__main__":
    main()
