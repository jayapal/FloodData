from analyse.models import GeoUSA
from FloodData.custom import CustomLayerMapping


states = {"NJ": "New Jersey", "MD": "Maryland"}

mapping = {'name' :'FLD_ZONE', # The 'name' model field maps to the 'str' layer field.
            'zone_info': 'ZONE_SUBTY',
            'fld_id': 'FLD_AR_ID',
            'poly' : 'POLYGON', # For geometry fields use OGC name.
               }


ZONE_X_SHADED  = "0.2 PCT ANNUAL CHANCE FLOOD HAZARD"
ZONE_X_UNSHADED  = "AREA OF MINIMAL FLOOD HAZARD"


def flood_zone_mapping(path, county, state):
    lm = CustomLayerMapping(GeoUSA, path, mapping, custom={"county": county, "state": state})
    lm.save(verbose=True, strict=True)

