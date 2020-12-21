from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class GeoUSA(models.Model):
    name = models.CharField(max_length=2500) # corresponds to the 'str' field
    poly = models.PolygonField(srid=4269) # we want our model in a different SRID

    def __str__(self):
        return 'Name: %s' % self.name
