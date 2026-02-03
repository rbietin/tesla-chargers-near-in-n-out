# Tesla Chargers Near In-N-Out

Find Tesla Superchargers within walking distance of In-N-Out Burger locations in California.

## Project Structure

```
├── run.py                      # Main pipeline script
├── src/
│   ├── fetch_superchargers.py  # Fetch Tesla Supercharger locations
│   ├── fetch_in_n_out.py       # Fetch In-N-Out locations
│   ├── find_nearby.py          # Find pairs within walking distance
│   └── export_to_google_maps.py # Export to CSV/KML for Google Maps
├── data/                       # Generated data files (gitignored)
│   ├── superchargers.json
│   ├── in_n_out.json
│   ├── nearby_pairs.json
│   ├── superchargers_with_in_n_out.csv
│   └── superchargers_with_in_n_out.kml
└── requirements.txt
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the full pipeline:

```bash
python run.py
```

Or run individual steps:

```bash
python src/fetch_superchargers.py   # Fetch Supercharger data
python src/fetch_in_n_out.py        # Fetch In-N-Out data
python src/find_nearby.py           # Find nearby pairs
python src/export_to_google_maps.py # Export for Google Maps
```

## Configuration

- Walking distance threshold: 400m (~5 minute walk)
- Edit `MAX_DISTANCE_METERS` in `src/find_nearby.py` to adjust

## Data Sources

- **Tesla Superchargers**: [supercharge.info](https://supercharge.info) public API
- **In-N-Out locations**: In-N-Out website API

## Importing to Google Maps

1. Go to https://www.google.com/mymaps
2. Create a new map
3. Click "Import" and select `data/superchargers_with_in_n_out.csv`
4. Choose "Latitude" and "Longitude" as position columns
5. Choose "Name" as title column
