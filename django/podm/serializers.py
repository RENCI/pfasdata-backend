from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import ahhs_dust_data, ahhs_water_data, ncserum, pfas_in_tapwater_usgs, pfas_sample_data
from drf_queryfields import QueryFieldsMixin

# Serializer, with GeoFeatureModelSerializer, for tables for the gauge_station_source_data model view.
# GeoFeatureModelSerializer enables spatial searches.
class ahhs_dust_data_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = ahhs_dust_data
        id_field = 'id'
        fields = ('id', 'sample', 'pfna_concentration', 'pfna_mrl', 'pfna_dl', 'pfna_flags', 'pfds_concentration', 'pfds_mrl', 
                  'pfds_dl', 'pfds_flags', 'pfhxa_concentration', 'pfhxa_mrl', 'pfhxa_dl', 'pfhxa_flags', 'pfoa_concentration', 
                  'pfoa_mrl', 'pfoa_dl', 'pfoa_flags', 'pfos_concentration', 'pfos_mrl', 'pfos_dl', 'pfos_flags', 
                  'pfba_concentration', 'pfba_mrl', 'pfba_dl', 'pfba_flags', 'pfdoa_concentration', 'pfdoa_mrl', 'pfdoa_dl', 
                  'pfdoa_flags', 'pfpea_concentration', 'pfpea_mrl', 'pfpea_dl', 'pfpea_flags', 'pfhps_concentration', 'pfhps_mrl', 
                  'pfhps_dl', 'pfhps_flags', 'pfunda_concentration', 'pfunda_mrl', 'pfunda_dl', 'pfunda_flags', 
                  'pfbs_concentration', 'pfbs_mrl', 'pfbs_dl', 'pfbs_flags', 'pfpes_concentration', 'pfpes_mrl', 'pfpes_dl', 
                  'pfpes_flags', 'pfns_concentration', 'pfns_mrl', 'pfns_dl', 'pfns_flags', 'pfhpa_concentration', 'pfhpa_mrl', 
                  'pfhpa_dl', 'pfhpa_flags', 'pfhxs_concentration', 'pfhxs_mrl', 'pfhxs_dl', 'pfhxs_flags', 'pfda_concentration', 
                  'pfda_mrl', 'pfda_dl', 'pfda_flags')

class ahhs_water_data_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = ahhs_water_data
        id_field = 'id'
        fields = ('id', 'sample', 'pfhps_concentration', 'pfhps_mrl', 'pfhps_dl', 'pfhps_flags', 'pfhxs_concentration', 'pfhxs_mrl', 
                  'pfhxs_dl', 'pfhxs_flags', 'pfda_concentration', 'pfda_mrl', 'pfda_dl', 'pfda_flags', 'pfba_concentration', 
                  'pfba_mrl', 'pfba_dl', 'pfba_flags', 'pfpea_concentration', 'pfpea_mrl', 'pfpea_dl', 'pfpea_flags', 
                  'pfpes_concentration', 'pfpes_mrl', 'pfpes_dl', 'pfpes_flags', 'pfna_concentration', 'pfna_mrl', 'pfna_dl', 
                  'pfna_flags', 'pfhxa_concentration', 'pfhxa_mrl', 'pfhxa_dl', 'pfhxa_flags', 'pfbs_concentration', 'pfbs_mrl', 
                  'pfbs_dl', 'pfbs_flags', 'pfos_concentration', 'pfos_mrl', 'pfos_dl', 'pfos_flags', 'pfhpa_concentration', 
                  'pfhpa_mrl', 'pfhpa_dl', 'pfhpa_flags', 'pfoa_concentration', 'pfoa_mrl', 'pfoa_dl', 'pfoa_flags', 
                  'pfns_concentration', 'pfns_mrl', 'pfns_dl', 'pfns_flags')

class ncserum_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = ncserum
        id_field = 'id'
        fields = ('id', 'sample', 'pfba_concentration', 'pfba_mrl', 'pfba_dl', 'pfba_flags', 'pfbs_concentration', 'pfbs_mrl', 
                  'pfbs_dl', 'pfbs_flags', 'pfda_concentration', 'pfda_mrl', 'pfda_dl', 'pfda_flags', 'pfdoa_concentration', 
                  'pfdoa_mrl', 'pfdoa_dl', 'pfdoa_flags', 'pfds_concentration', 'pfds_mrl', 'pfds_dl', 'pfds_flags', 
                  'pfhpa_concentration', 'pfhpa_mrl', 'pfhpa_dl', 'pfhpa_flags', 'pfhps_concentration', 'pfhps_mrl', 'pfhps_dl', 
                  'pfhps_flags', 'pfhxa_concentration', 'pfhxa_mrl', 'pfhxa_dl', 'pfhxa_flags', 'pfhxs_concentration', 'pfhxs_mrl', 
                  'pfhxs_dl', 'pfhxs_flags', 'pfna_concentration', 'pfna_mrl', 'pfna_dl', 'pfna_flags', 'pfns_concentration', 
                  'pfns_mrl', 'pfns_dl', 'pfns_flags', 'pfoa_concentration', 'pfoa_mrl', 'pfoa_dl', 'pfoa_flags', 
                  'pfos_concentration', 'pfos_mrl', 'pfos_dl', 'pfos_flags', 'pfpea_concentration', 'pfpea_mrl', 'pfpea_dl', 
                  'pfpea_flags', 'pfpes_concentration', 'pfpes_mrl', 'pfpes_dl', 'pfpes_flags', 'pfuda_concentration', 'pfuda_mrl', 
                  'pfuda_dl', 'pfuda_flags')

class pfas_in_tapwater_usgs_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = pfas_in_tapwater_usgs
        id_field = 'id'
        geo_field = 'geom'
        fields = ('id', 'study', 'station_na', 'site_type', 'sampleyear', 'detects', 'sum_pfas', 'pfprs', 'pfpes', 'pfpea', 'pfos', 
                  'pfoa', 'pfhxs', 'pfhxa', 'pfhps', 'pfhpa', 'pfds_num', 'pfda_num', 'pfbs', 'pfba', 'pf', 'genx_num', 'fosa', 
                  'f6_2fts', 'latitude', 'longitude')

class pfas_sample_data_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = pfas_sample_data
        id_field = 'sample_id'
        fields = ('sample_id', 'sample', 'study', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'pfna_concentration','pfna_mrl','pfna_dl','pfna_flags','pfds_concentration','pfds_mrl','pfds_dl','pfds_flags','pfhxa_concentration','pfhxa_mrl','pfhxa_dl','pfhxa_flags','pfoa_concentration','pfoa_mrl','pfoa_dl','pfoa_flags','pfos_concentration','pfos_mrl','pfos_dl','pfos_flags','pfba_concentration','pfba_mrl','pfba_dl','pfba_flags','pfdoa_concentration','pfdoa_mrl','pfdoa_dl','pfdoa_flags','pfpea_concentration','pfpea_mrl','pfpea_dl','pfpea_flags','pfhps_concentration','pfhps_mrl','pfhps_dl','pfhps_flags','pfunda_concentration','pfunda_mrl','pfunda_dl','pfunda_flags','pfbs_concentration','pfbs_mrl','pfbs_dl','pfbs_flags','pfpes_concentration','pfpes_mrl','pfpes_dl','pfpes_flags','pfns_concentration','pfns_mrl','pfns_dl','pfns_flags','pfhpa_concentration','pfhpa_mrl','pfhpa_dl','pfhpa_flags','pfhxs_concentration','pfhxs_mrl','pfhxs_dl','pfhxs_flags','pfda_concentration','pfda_mrl','pfda_dl','pfda_flags','pfuda_concentration','pfuda_mrl','pfuda_dl','pfuda_flags')

