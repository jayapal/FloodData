from analyse.models import GeoUSA
from FloodData.custom import CustomLayerMapping


mapping = {'name' :'FLD_ZONE', # The 'name' model field maps to the 'str' layer field.
               'poly' : 'POLYGON', # For geometry fields use OGC name.
               }


def flood_zone_mapping(path, county):
    lm = CustomLayerMapping(GeoUSA, path, mapping, custom={"county": county})
    lm.save()

