from __future__ import unicode_literals
from rest_framework import viewsets, status
#from rest_framework.generics import ListAPIView
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.gis.db.models.functions import Distance
#from django.contrib.gis.geos import GEOSGeometry,Point
from django.contrib.gis.geos import Point
from rest_framework_gis.filters import InBBoxFilter, DistanceToPointFilter, DistanceToPointOrderingFilter
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import pfas_name_classification_info_Serializer, pfas_in_tapwater_usgs_Serializer, pfas_sample_data_Serializer, pfas_sample_data2_Serializer, ntar_sample_data_Serializer, pfas_sites_distance_from_npl_Serializer
from .models import pfas_name_classification_info, pfas_in_tapwater_usgs, pfas_sample_data, pfas_sample_data2, ntar_sample_data, pfas_sites_distance_from_npl
from rest_framework.pagination import PageNumberPagination
from rest_framework_gis.pagination import GeoJsonPagination
from django.db import connection

# Change page size dynamically by by using the psize variable in the URL
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'psize'

class podm_pfas_name_classification_info_View(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = CustomPageNumberPagination
    queryset = pfas_name_classification_info.objects.all()
    serializer_class = pfas_name_classification_info_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['abbreviation','chemical_name','casrn','dtxsid','nhanes','carbon_atoms','formula','pfaa','pfca','pfsa','precursor','ftbs','dipap','ftoh','acid_ftca','acid_fts','substances_pasf','sulfonamides_fasa','ethanols_fase','pfeca','pfesa','cl_pfesa','carboxylic_acid','sulfonic_acid']
    ordering_fields = ['abbreviation','chemical_name','casrn','dtxsid','nhanes','carbon_atoms','formula','pfaa','pfca','pfsa,precursor','ftbs','dipap','ftoh','acid_ftca','acid_fts','substances_pasf','sulfonamides_fasa','ethanols_fase','pfeca','pfesa','cl_pfesa','carboxylic_acid','sulfonic_acid']

class podm_pfas_in_tapwater_usgs_View(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = CustomPageNumberPagination
    queryset = pfas_sample_data.objects.all()
    serializer_class = pfas_sample_data_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['sample_id', 'group_id', 'study', 'date', 'year', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfna_concentration','pfna_mrl','pfna_dl','pfna_flags','pfds_concentration','pfds_mrl','pfds_dl','pfds_flags','pfhxa_concentration','pfhxa_mrl','pfhxa_dl','pfhxa_flags','pfoa_concentration','pfoa_mrl','pfoa_dl','pfoa_flags','pfos_concentration','pfos_mrl','pfos_dl','pfos_flags','pfba_concentration','pfba_mrl','pfba_dl','pfba_flags','pfdoa_concentration','pfdoa_mrl','pfdoa_dl','pfdoa_flags','pfpea_concentration','pfpea_mrl','pfpea_dl','pfpea_flags','pfhps_concentration','pfhps_mrl','pfhps_dl','pfhps_flags','pfunda_concentration','pfunda_mrl','pfunda_dl','pfunda_flags','pfbs_concentration','pfbs_mrl','pfbs_dl','pfbs_flags','pfpes_concentration','pfpes_mrl','pfpes_dl','pfpes_flags','pfns_concentration','pfns_mrl','pfns_dl','pfns_flags','pfhpa_concentration','pfhpa_mrl','pfhpa_dl','pfhpa_flags','pfhxs_concentration','pfhxs_mrl','pfhxs_dl','pfhxs_flags','pfda_concentration','pfda_mrl','pfda_dl','pfda_flags']
    ordering_fields = ['sample_id', 'group_id', 'study', 'pi', 'date', 'year', 'units', 'medium', 'city', 'state', 'zipcode', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfna_concentration','pfna_mrl','pfna_dl','pfna_flags','pfds_concentration','pfds_mrl','pfds_dl','pfds_flags','pfhxa_concentration','pfhxa_mrl','pfhxa_dl','pfhxa_flags','pfoa_concentration','pfoa_mrl','pfoa_dl','pfoa_flags','pfos_concentration','pfos_mrl','pfos_dl','pfos_flags','pfba_concentration','pfba_mrl','pfba_dl','pfba_flags','pfdoa_concentration','pfdoa_mrl','pfdoa_dl','pfdoa_flags','pfpea_concentration','pfpea_mrl','pfpea_dl','pfpea_flags','pfhps_concentration','pfhps_mrl','pfhps_dl','pfhps_flags','pfunda_concentration','pfunda_mrl','pfunda_dl','pfunda_flags','pfbs_concentration','pfbs_mrl','pfbs_dl','pfbs_flags','pfpes_concentration','pfpes_mrl','pfpes_dl','pfpes_flags','pfns_concentration','pfns_mrl','pfns_dl','pfns_flags','pfhpa_concentration','pfhpa_mrl','pfhpa_dl','pfhpa_flags','pfhxs_concentration','pfhxs_mrl','pfhxs_dl','pfhxs_flags','pfda_concentration','pfda_mrl','pfda_dl','pfda_flags']

class podm_pfas_sample_data2_View(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = CustomPageNumberPagination
    queryset = pfas_sample_data2.objects.all()
    serializer_class = pfas_sample_data2_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['sample_id', 'study', 'date', 'year', 'pi', 'units', 'medium', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfmpa_concentration', 'pfmpa_mrl', 'pfmba_concentration', 'pfmba_mrl', 'pfta_concentration', 'pfta_mrl', 'netfosaa_concentration', 'netfosaa_mrl', 'x82fts_concentration', 'x82fts_mrl', 'hfpoda_concentration', 'hfpoda_mrl', 'x62fts_concentration', 'x62fts_mrl', 'nfdha_concentration', 'nfdha_mrl', 'pfuna_concentration', 'pfuna_mrl', 'pfeesa_concentration', 'pfeesa_mrl', 'nmefosaa_concentration', 'nmefosaa_mrl', 'x9clpf3ons_concentration', 'x9clpf3ons_mrl', 'x11clpf3ouds_concentration', 'x11clpf3ouds_mrl', 'adona_concentration', 'adona_mrl', 'x42fts_concentration', 'x42fts_mrl', 'pftrda_concentration', 'pftrda_mrl', 'genx_concentration', 'fosa_concentration', 'f6_2fts_concentration', 'pfprs_concentration']
    ordering_fields = ['sample_id', 'study', 'date', 'year', 'pi', 'units', 'medium', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfmpa_concentration', 'pfmpa_mrl', 'pfmba_concentration', 'pfmba_mrl', 'pfta_concentration', 'pfta_mrl', 'netfosaa_concentration', 'netfosaa_mrl', 'x82fts_concentration', 'x82fts_mrl', 'hfpoda_concentration', 'hfpoda_mrl', 'x62fts_concentration', 'x62fts_mrl', 'nfdha_concentration', 'nfdha_mrl', 'pfuna_concentration', 'pfuna_mrl', 'pfeesa_concentration', 'pfeesa_mrl', 'nmefosaa_concentration', 'nmefosaa_mrl', 'x9clpf3ons_concentration', 'x9clpf3ons_mrl', 'x11clpf3ouds_concentration', 'x11clpf3ouds_mrl', 'adona_concentration', 'adona_mrl', 'x42fts_concentration', 'x42fts_mrl', 'pftrda_concentration', 'pftrda_mrl', 'genx_concentration', 'fosa_concentration', 'f6_2fts_concentration', 'pfprs_concentration']

class podm_ntar_sample_data_View(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = CustomPageNumberPagination
    queryset = ntar_sample_data.objects.all() 
    serializer_class = ntar_sample_data_Serializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['sample_id', 'study', 'date', 'year', 'pi', 'medium', 'city', 'state', 'zipcode', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfas_short_name', 'pfas_long_name', 'flags', 'measurement']
    ordering_fields = ['city', 'state', 'site_id', 'site_type', 'latitude', 'longitude']

class pfas_sites_distance_from_npl_View(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = pfas_sites_distance_from_npl.objects.all()
    serializer_class = pfas_sites_distance_from_npl_Serializer

    @action(detail=True, methods=['get'], url_path='get-distance')
    def get_distance(self, request, pk=None):
        # 'pk' will contain the value of the path parameter (e.g., the object's ID)
        # if the action is detail=True.
        # For other path parameters defined in url_path, they will be in self.kwargs.

        # Example: Accessing a path parameter (e.g., 'pk' for a detail action)
        variables = self.kwargs.get('pk').split('&')
        miles = int(variables[0].split('=')[1])
        pi = variables[1].split('=')[1]

        # Custom Query
        sql_query = "SELECT sample_id AS pfas_sample_id, %s AS miles, study, pi, units, medium, pfas_samples.latitude AS pfas_latitude, pfas_samples.longitude AS pfas_longitude, " \
                            "npl.ogc_fid AS ogc_fid, npl.site_name as npl_site_name, npl.site_score AS npl_site_score, npl.latitude AS npd_latitude, npl.longitude AS npl_longitude " \
                    "FROM opal_pfas_sample_data_albers pfas_samples " \
                    "JOIN superfund_albers_national_priorities_list npl ON ST_DWithin(pfas_samples.geom::geometry, npl.wkb_geometry::geometry, %s * 1609.34) " \
                    "WHERE pi = %s AND geom IS NOT NULL"

        # Constructing and executing a raw SQL query
        if miles is not None:
            with connection.cursor() as cursor:
                # Use a parameterized query to prevent SQL injection
                cursor.execute(sql_query, [miles, miles, pi])
                columns = [col[0] for col in cursor.description]
                results = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]
            return Response(results, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Object ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
