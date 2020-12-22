from django.db import models

# Create your models here.

from django.contrib.gis.db import models

COUNTY_LIST = [
    'Atlantic County',
    'Bergen County',
    'Burlington County',
    'Camden County',
    'Cape May County',
    'Cumberland County',
    'Essex County',
    'Gloucestor County',
    'Hudson County',
    'Hunterdon County',
    'Mercer County',
    'Middlesex County',
    'Monmouth County',
    'Morris County',
    'Ocean County',
    'Passaic County',
    'Salem County',
    'Somerset County',
    'Sussex County',
    'Union County',
    'Warren County'
    
]

COUNTY_TYPES = [(county, county) for county in COUNTY_LIST]


class GeoUSA(models.Model):
    state = models.CharField(max_length=250, default="New Jersey")
    county = models.CharField(max_length=250, choices=COUNTY_TYPES)
    name = models.CharField(max_length=2500) # corresponds to the 'str' field
    poly = models.PolygonField(srid=4269) # we want our model in a different SRID

    def __str__(self):
        return 'Name: %s' % self.name
