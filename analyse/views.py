from django.contrib.gis.geos import GEOSGeometry

from rest_framework import response, status, views

from analyse.models import GeoUSA


class FloodDetectView(views.APIView):
    """
    API to flood data.
    """

    def post(self, request):
        data = request.data
        longitude = data.get('longitude', None)
        latitude = data.get('latitude', None)
        lookup_type = data.get('lookup_type')
        geom = None
        try:
            geom = GEOSGeometry("Point({} {})".format(longitude, latitude), srid=4269)
        except:
            return response.Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
        if lookup_type == "contains":
            geo_usa_obj = GeoUSA.objects.filter(poly__contains=geom)
        elif lookup_type == "intersects":
            geo_usa_obj = GeoUSA.objects.filter(poly__intersects=geom)
        else:
            geo_usa_obj = GeoUSA.objects.filter(poly__contains=geom)
        print("Geo USA objs", geo_usa_obj)
        if geo_usa_obj:
            return response.Response({"message": "Address is under flood Zone"})            
        return response.Response({"message": "Address is not under flood Zone"})

