# **DIRECTORY ARCHIVED** ON 2023-04-18

**THIS DIRECTORY IS ARCHIVED, IT IS KEPT TO UNDERSTAND THE HISTORY OF THE PROJECT.**

## Description

This directory contains :

- All the original map features registered in *MapWize*, in the GeoJSON format `mapwize/mapwize_*.json`.
- A JSON file specifying an icon and a style for each place type `icons.json`.
- A python script to generate new GeoJSON files that are compatible with *Leaflet* and the search box `cs_*.json`, and CSV files for *Géode* and *AppScho* `cs_*_features.csv`.

## Structure

```TXT
data/
├── generated/               -> (output directory for data.py)  # ignored by git
├── mapwize/                 -> Original mapwize data
├── .gitignore
├── data.py                  -> Data processing script          # WARNING: IT IS REALLY UGLY
├── icons.json               -> Icons and style for each place type
└── README.md
```

## Usage

Run the python script, a directory `generated` will be created containing the GeoJSON files and the CSV file.

```bash
python data.py
```
