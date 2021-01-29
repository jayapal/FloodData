from django.contrib.gis.geos import GEOSGeometry

from rest_framework import response, status, views

from usda.models import GeoUSDA


class UsdaEligibilityView(views.APIView):
    """
    API for usda eligibilty.
    """

    def post(self, request):
        data = request.data
        response_list = []
        geo_usda_objs_all = GeoUSDA.objects.filter(state='New Jersey')
        for each in data:
            longitude = each.get('longitude', None)
            latitude = each.get('latitude', None)
            lookup_type = each.get('lookup_type')
            geom = None
            zones_list = []
            try:
                geom = GEOSGeometry("Point({} {})".format(longitude, latitude), srid=4269)
            except:
                pass
            if geom:
                if lookup_type == "contains":
                    geo_usda_objs = geo_usda_objs_all.filter(poly__contains=geom)
                else:
                    geo_usda_objs = geo_usda_objs_all.filter(poly__intersects=geom)
                if geo_usda_objs:
                    each.update({"status": "ineligible"})
                else:
                    each.update({"status": "eligible"})
            response_list.append(each)
        return response.Response(response_list)
