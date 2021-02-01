from django.contrib.gis.geos import GEOSGeometry

from rest_framework import response, status, views

from oppurtunity.models import GeoOpportunityZone


class OpportunityZoneView(views.APIView):
    """
    API for opportunity zone.
    """

    def post(self, request):
        data = request.data
        response_list = []
        geo_oppurtunity_objs_all = GeoOpportunityZone.objects.filter(state='New Jersey')
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
                    geo_oppurtunity_objs = geo_oppurtunity_objs_all.filter(poly__contains=geom)
                else:
                    geo_oppurtunity_objs = geo_oppurtunity_objs_all.filter(poly__intersects=geom)
                if geo_oppurtunity_objs:
                    each.update({"is_opportunity_zone": True})
                else:
                    each.update({"is_opportunity_zone": False})
            response_list.append(each)
        return response.Response(response_list)
