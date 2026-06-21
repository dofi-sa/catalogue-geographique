# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
from lxml import etree
from collections import defaultdict

NS = {"geo": "http://exemple.com/geo"}
XML_FILE = "catalogue.xml"
GEOJSON_FILE = "export.geojson"
STATS_FILE = "rapport_statistiques.txt"

def export_geojson(xml_path, geojson_path, stats_path):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    lieux = root.findall("geo:lieu", NS)

    features = []
    villes_count = defaultdict(int)

    for lieu in lieux:
        lid     = lieu.get("id")
        cat     = lieu.get("categorie")
        nom     = lieu.findtext("geo:nom", default="", namespaces=NS)
        adresse = lieu.findtext("geo:adresse", default="", namespaces=NS)
        desc    = lieu.findtext("geo:description", default="", namespaces=NS)
        lat     = float(lieu.findtext("geo:coordonnees/geo:latitude", namespaces=NS))
        lon     = float(lieu.findtext("geo:coordonnees/geo:longitude", namespaces=NS))

        parts = [p.strip() for p in adresse.split(",")]
        ville = parts[-2] if len(parts) >= 2 else parts[0]
        villes_count[ville] += 1

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "properties": {
                "id": lid,
                "nom": nom,
                "categorie": cat,
                "adresse": adresse,
                "description": desc
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(geojson_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
    print(f"GeoJSON exporte : {geojson_path} ({len(features)} lieux)")

    # Statistiques XPath
    total = len(tree.xpath("//geo:lieu", namespaces=NS))

    cats_xpath = {}
    for lieu in lieux:
        cat = lieu.get("categorie")
        if cat not in cats_xpath:
            count = len(tree.xpath(f"//geo:lieu[@categorie='{cat}']", namespaces=NS))
            cats_xpath[cat] = count

    latitudes  = [float(v) for v in tree.xpath("//geo:latitude/text()", namespaces=NS)]
    longitudes = [float(v) for v in tree.xpath("//geo:longitude/text()", namespaces=NS)]
    moy_lat = sum(latitudes) / len(latitudes) if latitudes else 0
    moy_lon = sum(longitudes) / len(longitudes) if longitudes else 0

    with open(stats_path, "w", encoding="utf-8") as f:
        f.write("=== RAPPORT STATISTIQUES ===\n\n")
        f.write(f"Nombre total de lieux : {total}\n\n")
        f.write("Nombre de sites par categorie :\n")
        for cat, count in sorted(cats_xpath.items()):
            f.write(f"  - {cat} : {count}\n")
        f.write("\nNombre de sites par ville :\n")
        for ville, count in sorted(villes_count.items(), key=lambda x: -x[1]):
            f.write(f"  - {ville} : {count}\n")
        f.write(f"\nCentre geographique moyen (lat, lon) : ({moy_lat:.4f}, {moy_lon:.4f})\n")

    print(f"Statistiques generees : {stats_path}")
    print(f"\nTotal lieux : {total}")
    print("Par categorie :")
    for cat, count in sorted(cats_xpath.items()):
        print(f"   {cat} : {count}")

if __name__ == "__main__":
    export_geojson(XML_FILE, GEOJSON_FILE, STATS_FILE)