from django.contrib.gis.db import models

# Create your models here.

class GeoOpportunityZone(models.Model):
    state = models.CharField(max_length=250)
    county = models.CharField(max_length=250)
    poly = models.MultiPolygonField(srid=4269) # we want our model in a different SRID

    def __str__(self):
        return "{} - {}".format(self.id, self.state, self.county)

