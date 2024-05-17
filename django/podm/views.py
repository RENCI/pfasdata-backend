from __future__ import unicode_literals
from rest_framework import viewsets, status
#from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
#from django.contrib.gis.geos import GEOSGeometry,Point
from django.contrib.gis.geos import Point
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter, DistanceToPointOrderingFilter
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import pfas_in_tapwater_usgs_Serializer, pfas_sample_data_Serializer, ntar_sample_data_Serializer
from .models import pfas_in_tapwater_usgs, pfas_sample_data, ntar_sample_data
from rest_framework.pagination import PageNumberPagination
from rest_framework_gis.pagination import GeoJsonPagination

# Change page size dynamically by by using the psize variable in the URL
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'psize'

class podm_pfas_in_tapwater_usgs_View(viewsets.ModelViewSet):
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

class podm_pfas_sample_data_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = pfas_sample_data.objects.all()
    serializer_class = pfas_sample_data_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['sample_id', 'group_id', 'study', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'pfna_concentration','pfna_mrl','pfna_dl','pfna_flags','pfds_concentration','pfds_mrl','pfds_dl','pfds_flags','pfhxa_concentration','pfhxa_mrl','pfhxa_dl','pfhxa_flags','pfoa_concentration','pfoa_mrl','pfoa_dl','pfoa_flags','pfos_concentration','pfos_mrl','pfos_dl','pfos_flags','pfba_concentration','pfba_mrl','pfba_dl','pfba_flags','pfdoa_concentration','pfdoa_mrl','pfdoa_dl','pfdoa_flags','pfpea_concentration','pfpea_mrl','pfpea_dl','pfpea_flags','pfhps_concentration','pfhps_mrl','pfhps_dl','pfhps_flags','pfunda_concentration','pfunda_mrl','pfunda_dl','pfunda_flags','pfbs_concentration','pfbs_mrl','pfbs_dl','pfbs_flags','pfpes_concentration','pfpes_mrl','pfpes_dl','pfpes_flags','pfns_concentration','pfns_mrl','pfns_dl','pfns_flags','pfhpa_concentration','pfhpa_mrl','pfhpa_dl','pfhpa_flags','pfhxs_concentration','pfhxs_mrl','pfhxs_dl','pfhxs_flags','pfda_concentration','pfda_mrl','pfda_dl','pfda_flags','pfuda_concentration','pfuda_mrl','pfuda_dl','pfuda_flags']
    ordering_fields = ['city', 'state']

class podm_ntar_sample_data_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = ntar_sample_data.objects.all() 
    serializer_class = ntar_sample_data_Serializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['sample_id', 'study', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'pfas_short_name', 'pfas_long_name', 'flags', 'measurement']
    ordering_fields = ['city', 'state']
