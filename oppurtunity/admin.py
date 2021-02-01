from django.contrib import admin

# Register your models here.

from oppurtunity.models import GeoOppurtunityZone


class GeoOppurtunityZoneAdmin(admin.ModelAdmin):
    list_filter = ('state', 'county')

admin.site.register(GeoOppurtunityZone, GeoOppurtunityZoneAdmin)
