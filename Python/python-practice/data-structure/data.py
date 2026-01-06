# save as overpass_extract.py
import requests
import time
import csv
import pandas as pd
from urllib.parse import quote_plus

# -------------- CONFIG --------------
OVERPASS_URL = "https://overpass-api.de/api/interpreter"  # public instance
# Change this query: area name "Nagpur" is an example — replace as needed.
OVERPASS_QUERY = """
[out:json][timeout:600];
area["name"="Nagpur"]["boundary"="administrative"]->.searchArea;
(
  node["amenity"~"school|college|university|kindergarten"](area.searchArea);
  way["amenity"~"school|college|university|kindergarten"](area.searchArea);
  relation["amenity"~"school|college|university|kindergarten"](area.searchArea);
);
out center tags;
"""
OUTPUT_CSV = "osm_institutions_nagpur.csv"
# ------------------------------------

def run_query(query):
    r = requests.get(OVERPASS_URL, params={'data': query}, timeout=180)
    r.raise_for_status()
    return r.json()

def element_latlon(el):
    # Nodes have lat/lon, ways/relations return center
    if el.get('type') == 'node':
        return el.get('lat'), el.get('lon')
    # 'center' key for way/relation when using 'out center'
    c = el.get('center')
    if c:
        return c.get('lat'), c.get('lon')
    return None, None

def build_address(tags):
    # combine addr:* tags into a single address string if present
    parts = []
    for key in ['addr:housenumber','addr:street','addr:suburb','addr:city','addr:postcode','addr:state','addr:country']:
        v = tags.get(key)
        if v:
            parts.append(v)
    return ", ".join(parts) if parts else tags.get('address') or ""

def extract_tags(tags):
    return {
        'name': tags.get('name'),
        'type': tags.get('amenity') or tags.get('office') or tags.get('building'),
        'address': build_address(tags),
        'street': tags.get('addr:street'),
        'city': tags.get('addr:city'),
        'state': tags.get('addr:state'),
        'postcode': tags.get('addr:postcode'),
        'phone': tags.get('contact:phone') or tags.get('phone') or tags.get('telephone'),
        'email': tags.get('contact:email') or tags.get('email'),
        'website': tags.get('contact:website') or tags.get('website'),
        'management': tags.get('operator') or tags.get('operator:type'),
        'osm_tags': ";".join([f"{k}={v}" for k,v in tags.items()])  # for debugging/enrichment
    }

def google_maps_link(lat, lon):
    if lat and lon:
        return f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    return ""

def main():
    print("Running Overpass query...")
    resp = run_query(OVERPASS_QUERY)
    elements = resp.get('elements', [])
    print(f"Got {len(elements)} elements")

    rows = []
    for el in elements:
        tags = el.get('tags', {}) or {}
        lat, lon = element_latlon(el)
        info = extract_tags(tags)
        info.update({
            'osm_id': f"{el.get('type')}/{el.get('id')}",
            'lat': lat,
            'lon': lon,
            'google_maps_link': google_maps_link(lat, lon),
            'source': 'overpass-api.de'
        })
        rows.append(info)

    # Save to CSV using pandas
    df = pd.DataFrame(rows)
    cols = ['osm_id','name','type','address','street','city','state','postcode',
            'phone','email','website','management','lat','lon','google_maps_link','osm_tags','source']
    df = df.reindex(columns=cols)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Wrote {len(df)} rows to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
