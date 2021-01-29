from django.contrib.gis.geos import GEOSGeometry

from rest_framework import response, status, views

from analyse.models import GeoUSA, COUNTY_LIST


class FloodZoneView(views.APIView):
    """
    API to get flood zone.
    """

    def post(self, request):
        data = request.data
        response_list = []
        filter_by = self.request.query_params.get('filter_by')
        geo_usa_objs_all = GeoUSA.objects.exclude(name='AREA NOT INCLUDED')
        if filter_by:
            if filter_by in COUNTY_LIST:
                geo_usa_objs_all = geo_usa_objs_all.filter(county=filter_by)
            else:
                return response.Response({"error": "Invalid Filter"}, status=status.HTTP_400_BAD_REQUEST)
        for each in data:
            longitude = each.get('longitude', None)
            latitude = each.get('latitude', None)
            lookup_type = each.get('lookup_type')
            filter_by = each.get('filter_by', None)
            geom = None
            zones_list = []
            try:
                geom = GEOSGeometry("Point({} {})".format(longitude, latitude), srid=4269)
            except:
                pass
            geo_usa_objs = geo_usa_objs_all.filter(county=filter_by) if filter_by in COUNTY_LIST else geo_usa_objs_all
            if geom:
                if lookup_type == "contains":
                    geo_usa_objs = geo_usa_objs.filter(poly__contains=geom)
                else:
                    geo_usa_objs = geo_usa_objs.filter(poly__intersects=geom)
                print("Geo USA objs", geo_usa_objs)
                if geo_usa_objs:
                    zones_list =list(geo_usa_objs.distinct('name').values_list('name', flat=True))
                    print(zones_list)
            each.update({"zones": zones_list})
            response_list.append(each)
        return response.Response(response_list)


class CountyListView(views.APIView):
    """
    API to get county list.
    """

    def get(self, request):
        return response.Response(COUNTY_LIST)

