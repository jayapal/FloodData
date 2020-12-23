from django.contrib.gis.geos import GEOSGeometry

from rest_framework import response, status, views

from analyse.models import GeoUSA


class FloodZoneView(views.APIView):
    """
    API to get flood zone.
    """

    def post(self, request):
        data = request.data
        response_list = []
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
                    geo_usa_obj = GeoUSA.objects.filter(poly__contains=geom).exclude(name='AREA NOT INCLUDED')
                geo_usa_obj = GeoUSA.objects.filter(poly__intersects=geom).exclude(name='AREA NOT INCLUDED')
                print("Geo USA objs", geo_usa_obj)
                if geo_usa_obj:
                    zones_list =list(geo_usa_obj.distinct('name').values_list('name', flat=True))
                    print(zones_list)
            each.update({"zones": zones_list})
            response_list.append(each)
        return response.Response(response_list)

