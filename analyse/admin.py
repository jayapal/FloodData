from django.contrib import admin

# Register your models here.

from analyse.models import *

class GeoUSAAdmin(admin.ModelAdmin):
    list_filter = ('county',)

admin.site.register(GeoUSA, GeoUSAAdmin)
