import os
from pathlib import Path
from typing import Optional, Union

from arcgis.features import GeoAccessor  # noqa: F401  registers the .spatial pandas accessor
from arcgis.geocoding import Geocoder as AGOLGeocoder, geocode
from arcgis.geometry import Geometry, Point
from arcgis.gis import GIS
import pandas as pd

"""
Geocoder backed by the ArcGIS Python API (arcgis).

This replaces the earlier arcpy implementation so the module can run outside
ArcGIS Pro / Windows. Two differences worth noting:

1. Geocoding: arcpy consumed a local .loc/.loz locator file directly. The
   ArcGIS Python API geocodes against a published locator reached through a
   `GIS` connection (ArcGIS Online or Enterprise). Pass a `locator_url` (a
   published GeocodeServer) or rely on the authenticated GIS's default
   geocoders. The legacy .loz file would need to be published first.

2. Point-in-polygon: the local shapefile is still read from disk via the
   spatial pandas accessor (`pd.DataFrame.spatial.from_featureclass`). Each
   row's SHAPE is an arcgis Geometry whose .contains() performs the test
   locally via shapely.
"""

ARC_FILES = Path(__file__).resolve().parent / "ArcGIS Files"
DEFAULT_SHAPEFILE = ARC_FILES / "shapefiles" / "geo_export_245fc99a-723b-4ad0-ab19-164d6ea290d2.shp"
DEFAULT_ADDRESS = "1100 South Hamilton Ave, Chicago, IL 60612"


class Geocoder:
    def __init__(
        self,
        address: str = DEFAULT_ADDRESS,
        shape_file: Union[str, os.PathLike, None] = None,
        locator_url: Optional[str] = None,
        gis: Optional[GIS] = None,
    ):
        self.address = address
        self.shape_file = Path(shape_file) if shape_file else DEFAULT_SHAPEFILE
        self.gis = gis or GIS()  # anonymous AGOL by default
        self.locator = AGOLGeocoder(locator_url, gis=self.gis) if locator_url else None
        self._districts_sdf: Optional[pd.DataFrame] = None

    def __str__(self) -> str:
        return (
            f"Geocoder(shape_file={self.shape_file.name}, "
            f"locator={'custom' if self.locator else 'default AGOL'}, "
            f"address={self.address!r})"
        )

    def get_shape_file(self) -> str:
        return str(self.shape_file)

    def set_shape_file(self, shape_file: Union[str, os.PathLike]) -> str:
        self.shape_file = Path(shape_file)
        self._districts_sdf = None  # invalidate cached layer
        return f"shape file set to {self.shape_file}"

    def _districts(self) -> pd.DataFrame:
        if self._districts_sdf is None:
            self._districts_sdf = pd.DataFrame.spatial.from_featureclass(str(self.shape_file))
        return self._districts_sdf

    def geocode_address(self, address: str, min_score: int = 90) -> Optional[Geometry]:
        """Return the highest-scoring candidate Geometry, or None if none pass min_score."""
        results = (
            self.locator.geocode(address) if self.locator else geocode(address, gis=self.gis)
        )
        if not results:
            return None
        best = max(results, key=lambda r: r.get("score", 0))
        if best.get("score", 0) < min_score:
            return None
        loc = best["location"]
        sr = best.get("attributes", {}).get("SpatialReference") or {"wkid": 4326}
        return Geometry({"x": loc["x"], "y": loc["y"], "spatialReference": sr})

    def return_district(self, point: Optional[Geometry], verbose: bool = False) -> Union[int, str, None]:
        if point is None:
            return "Calculated address does not appear to be in Cook County"

        sdf = self._districts()
        for _, row in sdf.iterrows():
            polygon: Geometry = row["SHAPE"]
            if polygon.contains(point):
                return row["dist_num"]

        if verbose:
            return "This address appears to be in Cook County, but not in Chicago."
        return None

    def geocode_to_district(self, address: str) -> Union[int, str, None]:
        return self.return_district(self.geocode_address(address))
