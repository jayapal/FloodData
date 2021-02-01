from django.contrib import admin

# Register your models here.

from oppurtunity.models import GeoOpportunityZone


class GeoOpportunityZoneAdmin(admin.ModelAdmin):
    list_filter = ('state', 'county')

admin.site.register(GeoOpportunityZone, GeoOpportunityZoneAdmin)
