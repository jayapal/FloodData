from django.contrib import admin

# Register your models here.

from usda.models import *

class GeoUSDAAdmin(admin.ModelAdmin):
    list_filter = ('state',)

admin.site.register(GeoUSDA, GeoUSDAAdmin)
