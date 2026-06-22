# 🌍 Geographic Catalogue - Morocco

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![LXML](https://img.shields.io/badge/lxml-4.9+-orange.svg)](https://lxml.de)
[![Leaflet](https://img.shields.io/badge/Leaflet-1.9+-yellow.svg)](https://leafletjs.com)

##  Description

This project provides a complete ETL (Extract-Transform-Load) pipeline for geographic data, transforming raw CSV files into a validated XML catalogue and generating an interactive map visualization for Moroccan locations.

### Key Features
-  **Data Cleaning**: Automatic correction of common errors (invalid IDs, out-of-range coordinates)
-  **XML Generation**: Creates structured XML from CSV data
-  **XSD Validation**: Ensures data integrity with a custom XML schema
-  **Geographic Constraints**: Latitude (20.0-37.0) and Longitude (-18.0-0.0) for Morocco
-  **Interactive Map**: Leaflet.js visualization with custom markers
-  **Error Logging**: Detailed reports of all corrections and validation errors


## 🗂️ Project Structure
```
catalogue-geographique/
│
├── data/
│ ├── locations.csv # Raw data with realistic errors
│ └── catalogue.xml # Cleaned and structured XML output
│
├── scripts/
│ ├── 01_csv_to_xml.py 
│ ├── 04_export_geojson.py 
│ └── carte_interactive.html 
├── schema/
│ └── lieux.xsd # XML Schema D
│
├── carte.png # resultat finale 
│
├── README.md # Project documentation
├── .gitignore # Git ignore rules
└── requirements.txt # Python dependencies

```

---

## 🚀 Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)

### Required Python Libraries
- `lxml` - XML processing and XSD validation
- `pandas` - CSV data manipulation

---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/catalogue-geographique.git
cd catalogue-geographique
```
### 2-install dependencies
```bash
pip install lxml pandas
```
## Usage Guide
### step 1: Generate XML from CSV
``` bash 
python scripts/01_csv_to_xml.py
```
### Step 2: Validate XML against XSD
``` bash 
python scripts/02_validate_xsd.py
```
### Step 3: Generate Interactive Map
``` bash
python scripts/03_generate_html.py
```

