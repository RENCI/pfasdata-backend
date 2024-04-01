from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
#from django.contrib.gis.geos import GEOSGeometry,Point
from django.contrib.gis.geos import Point
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter, DistanceToPointOrderingFilter
from rest_framework.decorators import action
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import pfas_hot_spot_Serializer, pfas_dust_water_Serializer, ahhs_dust_data_Serializer, ahhs_water_data_Serializer, ncserum_Serializer, pfas_in_tapwater_usgs_Serializer
from .models import pfas_hot_spot, pfas_dust_water, ahhs_dust_data, ahhs_water_data, ncserum, pfas_in_tapwater_usgs
from rest_framework.pagination import PageNumberPagination
from rest_framework_gis.pagination import GeoJsonPagination

# Change page size dynamically by by using the psize variable in the URL
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'psize'

class drf_pfas_hot_spot_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = pfas_hot_spot.objects.all() #.order_by('time')
    serializer_class = pfas_hot_spot_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['id','dust_sample','dust_compound','dust_concentration_ng_per_g','city','state','longitude','latitude','geom']

    # Function to enable search by distance from lon/lat point
    @action(detail=False, methods=['get'])
    def get_nearest_samples(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords),srid=4326)
            nearest_five_samples = pfas_hot_spot.objects.annotate(distance=Distance('geom',user_location)).order_by('distance')[:10]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_five_samples, many = True)
            print(nearest_five_samples)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class drf_pfas_dust_water_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = pfas_dust_water.objects.all() #.order_by('time')
    serializer_class = pfas_dust_water_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['id','sample','compound','concentration_ng_per_g','city','state','medium','longitude','latitude','geom']

    # Function to enable search by distance from lon/lat point
    @action(detail=False, methods=['get'])
    def get_nearest_samples(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords),srid=4326)
            nearest_five_samples = pfas_dust_water.objects.annotate(distance=Distance('geom',user_location)).order_by('distance')[:10]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_five_samples, many = True)
            print(nearest_five_samples)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class drf_ahhs_dust_data_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = ahhs_dust_data.objects.all()
    serializer_class = ahhs_dust_data_Serializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'sample', 'pfna_concentration', 'pfna_mrl', 'pfna_dl', 'pfna_flags', 'pfds_concentration', 'pfds_mrl', 
                     'pfds_dl', 'pfds_flags', 'pfhxa_concentration', 'pfhxa_mrl', 'pfhxa_dl', 'pfhxa_flags', 'pfoa_concentration', 
                     'pfoa_mrl', 'pfoa_dl', 'pfoa_flags', 'pfos_concentration', 'pfos_mrl', 'pfos_dl', 'pfos_flags', 
                     'pfba_concentration', 'pfba_mrl', 'pfba_dl', 'pfba_flags', 'pfdoa_concentration', 'pfdoa_mrl', 'pfdoa_dl', 
                     'pfdoa_flags', 'pfpea_concentration', 'pfpea_mrl', 'pfpea_dl', 'pfpea_flags', 'pfhps_concentration', 
                     'pfhps_mrl', 'pfhps_dl', 'pfhps_flags', 'pfunda_concentration', 'pfunda_mrl', 'pfunda_dl', 'pfunda_flags', 
                     'pfbs_concentration', 'pfbs_mrl', 'pfbs_dl', 'pfbs_flags', 'pfpes_concentration', 'pfpes_mrl', 'pfpes_dl', 
                     'pfpes_flags', 'pfns_concentration', 'pfns_mrl', 'pfns_dl', 'pfns_flags', 'pfhpa_concentration', 'pfhpa_mrl', 
                     'pfhpa_dl', 'pfhpa_flags', 'pfhxs_concentration', 'pfhxs_mrl', 'pfhxs_dl', 'pfhxs_flags', 'pfda_concentration', 
                     'pfda_mrl', 'pfda_dl', 'pfda_flags']

class drf_ahhs_water_data_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = ahhs_water_data.objects.all()
    serializer_class = ahhs_water_data_Serializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'sample', 'pfhps_concentration', 'pfhps_mrl', 'pfhps_dl', 'pfhps_flags', 'pfhxs_concentration', 
                     'pfhxs_mrl', 'pfhxs_dl', 'pfhxs_flags', 'pfda_concentration', 'pfda_mrl', 'pfda_dl', 'pfda_flags', 
                     'pfba_concentration', 'pfba_mrl', 'pfba_dl', 'pfba_flags', 'pfpea_concentration', 'pfpea_mrl', 'pfpea_dl', 
                     'pfpea_flags', 'pfpes_concentration', 'pfpes_mrl', 'pfpes_dl', 'pfpes_flags', 'pfna_concentration', 'pfna_mrl', 
                     'pfna_dl', 'pfna_flags', 'pfhxa_concentration', 'pfhxa_mrl', 'pfhxa_dl', 'pfhxa_flags', 'pfbs_concentration', 
                     'pfbs_mrl', 'pfbs_dl', 'pfbs_flags', 'pfos_concentration', 'pfos_mrl', 'pfos_dl', 'pfos_flags', 
                     'pfhpa_concentration', 'pfhpa_mrl', 'pfhpa_dl', 'pfhpa_flags', 'pfoa_concentration', 'pfoa_mrl', 'pfoa_dl', 
                     'pfoa_flags', 'pfns_concentration', 'pfns_mrl', 'pfns_dl', 'pfns_flags']

class drf_ncserum_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = ncserum.objects.all()
    serializer_class = ncserum_Serializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id', 'sample', 'pfba_concentration', 'pfba_mrl', 'pfba_dl', 'pfba_flags', 'pfbs_concentration', 'pfbs_mrl', 
                     'pfbs_dl', 'pfbs_flags', 'pfda_concentration', 'pfda_mrl', 'pfda_dl', 'pfda_flags', 'pfdoa_concentration', 
                     'pfdoa_mrl', 'pfdoa_dl', 'pfdoa_flags', 'pfds_concentration', 'pfds_mrl', 'pfds_dl', 'pfds_flags', 
                     'pfhpa_concentration', 'pfhpa_mrl', 'pfhpa_dl', 'pfhpa_flags', 'pfhps_concentration', 'pfhps_mrl', 'pfhps_dl', 
                     'pfhps_flags', 'pfhxa_concentration', 'pfhxa_mrl', 'pfhxa_dl', 'pfhxa_flags', 'pfhxs_concentration', 
                     'pfhxs_mrl', 'pfhxs_dl', 'pfhxs_flags', 'pfna_concentration', 'pfna_mrl', 'pfna_dl', 'pfna_flags', 
                     'pfns_concentration', 'pfns_mrl', 'pfns_dl', 'pfns_flags', 'pfoa_concentration', 'pfoa_mrl', 'pfoa_dl', 
                     'pfoa_flags', 'pfos_concentration', 'pfos_mrl', 'pfos_dl', 'pfos_flags', 'pfpea_concentration', 'pfpea_mrl', 
                     'pfpea_dl', 'pfpea_flags', 'pfpes_concentration', 'pfpes_mrl', 'pfpes_dl', 'pfpes_flags', 
                     'pfuda_concentration', 'pfuda_mrl', 'pfuda_dl', 'pfuda_flags']

class drf_pfas_in_tapwater_usgs_View(viewsets.ModelViewSet):
    pagination_class = GeoJsonPagination
    queryset = pfas_in_tapwater_usgs.objects.all()
    serializer_class = pfas_in_tapwater_usgs_Serializer
    filter_backends = (InBBoxFilter,DistanceToPointFilter,DistanceToPointOrderingFilter,DjangoFilterBackend)
    bbox_filter_include_overlapping = True
    distance_filter_field = 'geom'
    distance_ordering_filter_field = 'geom'
    distance_filter_convert_meters = True
    filter_fields = ['id', 'study', 'station_na', 'site_type', 'sampleyear', 'detects', 'sum_pfas', 'pfprs', 'pfpes', 'pfpea', 'pfos',
                     'pfoa', 'pfhxs', 'pfhxa', 'pfhps', 'pfhpa', 'pfds_num', 'pfda_num', 'pfbs', 'pfba', 'pf', 'genx_num', 'fosa',
                     'f6_2fts', 'latitude', 'longitude']
