# Tesla Superchargers Near In-N-Out

Find Tesla Superchargers within walking distance of In-N-Out Burger locations in California. Perfect for road trips when you want to grab a burger while your car charges.

**[View the map](https://www.google.com/maps/d/edit?mid=1na82zQDa9YaKaYCwGt67Lfdvvblt19E&usp=sharing)** (generated February 2, 2026)

## Quick Start

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python run.py
```

## What It Does

1. Fetches all Tesla Supercharger locations in California (630+ locations)
2. Fetches all In-N-Out Burger locations in California (270+ locations)
3. Finds pairs within 400m walking distance (~5 minute walk)
4. Exports results for Google Maps import

**Current results: 55 Supercharger + In-N-Out combinations**

## Project Structure

```
├── run.py                       # Run the full pipeline
├── src/
│   ├── fetch_superchargers.py   # Fetch Tesla Supercharger locations
│   ├── fetch_in_n_out.py        # Fetch In-N-Out locations
│   ├── find_nearby.py           # Find pairs within walking distance
│   └── export_to_google_maps.py # Export to CSV/KML
├── data/                        # Generated output (gitignored)
└── requirements.txt
```

## Configuration

Edit `MAX_DISTANCE_METERS` in `src/find_nearby.py` to change the walking distance threshold (default: 400m).

## Importing to Google Maps

1. Go to [Google My Maps](https://www.google.com/mymaps)
2. Create a new map
3. Click **Import** and select `data/superchargers_with_in_n_out.csv`
4. Choose "Latitude" and "Longitude" as position columns
5. Choose "Name" as title column

Alternatively, import the KML file (`data/superchargers_with_in_n_out.kml`) for richer formatting.

## Data Sources

- **Tesla Superchargers**: [supercharge.info](https://supercharge.info) API
- **In-N-Out locations**: [OpenStreetMap](https://www.openstreetmap.org) via Overpass API

## Sample Results

| Location | Walking Distance |
|----------|------------------|
| Beaumont, CA | 16m (~0 min) |
| Ukiah, CA | 55m (~1 min) |
| Glendale, CA (Harvey Dr) | 66m (~1 min) |
| Fairfield, CA | 68m (~1 min) |
| Pleasanton, CA | 72m (~1 min) |
| Gilroy, CA | 114m (~1 min) |
