# Geocoder as a Service

Flask microservice for the Cook County Juvenile Probation Department that
geocodes an address, resolves it to a Chicago police district, and returns the
SPO supervisor responsible for that district. Supervisor assignments are
currently tracked in `units/list_of_units.json`; the long-term intent is to
back this with [CFive Supervisor](https://www.cfive.com/products/supervisor/).

## Stack

- **Web:** Flask + Flask-RESTful
- **GIS:** [ArcGIS API for Python](https://developers.arcgis.com/python/) (`arcgis`)
  - Geocoding via a published locator reached through a `GIS` connection
    (ArcGIS Online or Enterprise). The legacy local `.loc`/`.loz` files are
    kept in `ArcGIS Files/` for reference but are not read directly — they
    would need to be published to AGOL/Enterprise first.
  - Point-in-polygon via `pandas.DataFrame.spatial.from_featureclass`
    (reads the local shapefile) and `Geometry.contains()`.

## Install

```
pip install -r requirements.txt
```

## Run

```
python geocoder_service.py
```

The service starts on `http://127.0.0.1:5000`.

### GIS credentials

`geocoder.Geocoder()` instantiates an anonymous `GIS()` by default, which is
fine for the World Geocoder's free tier but will not store results. For a
specific locator, pass its URL and a `GIS` with credentials:

```python
from arcgis.gis import GIS
from geocoder import Geocoder

gis = GIS("https://your.portal/arcgis", "user", "password")
gc = Geocoder(locator_url="https://your.portal/.../GeocodeServer", gis=gis)
```

## Endpoints

| Method | Path         | Query       | Returns |
| ------ | ------------ | ----------- | ------- |
| GET    | `/units`     | —           | All supervisor units |
| GET    | `/districts` | `address`   | `{"Police District": <num \| message>}` |
| GET    | `/geocode/`  | `address`   | `{"address": <point \| message>}` |
| GET    | `/assign/`   | `address`   | `{"supervisor": <lname \| null>, "reason"?: str}` |

## Modules

### `geocoder.py` — `Geocoder`
- `geocode_address(address, min_score=90)` — returns an `arcgis.geometry.Geometry` point or `None`.
- `return_district(point, verbose=False)` — point-in-polygon against the
  police-district shapefile; returns the `dist_num`, `None`, or a
  diagnostic string when `verbose`.
- `geocode_to_district(address)` — chains the two.
- `get_shape_file()` / `set_shape_file(path)` — inspect/replace the district
  shapefile (cached layer is invalidated on set).

### `unit_structure.py`
- `UnitStructure(spo_lname, division=4, spo_fname="Officer")` — base model.
- `FieldUnit(..., court_date, police_district, calendar)` — adds roster
  data; `get_supervisor(district)` returns `"First, Last"` if the district
  is covered, else `None`.
- `load_units_to_class(path)` — reads NDJSON into `FieldUnit` instances.

### `address_parser.py`
Thin wrapper around `flask_restful.reqparse` that enforces a required
`address` query parameter.
