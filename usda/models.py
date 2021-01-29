from django.contrib.gis.db import models

# Create your models here.

class GeoUSDA(models.Model):
    state = models.CharField(max_length=250, blank=True, null=True)
    poly = models.PolygonField(srid=4269) # we want our model in a different SRID

    def __str__(self):
        return "{} - {}".format(self.id, self.state)

