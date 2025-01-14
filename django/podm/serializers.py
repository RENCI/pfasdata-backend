from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import pfas_name_classification_info, pfas_in_tapwater_usgs, pfas_sample_data, ntar_sample_data
from drf_queryfields import QueryFieldsMixin

# Serializer, with GeoFeatureModelSerializer, for tables for the gauge_station_source_data model view.
# GeoFeatureModelSerializer enables spatial searches.

class pfas_name_classification_info_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta: 
        model = pfas_name_classification_info
        id_field = 'id'
        fields = ('abbreviation','chemical_name','casrn','dtxsid','nhanes','carbon_atoms','formula','pfaa','pfca','pfsa','precursor','ftbs','dipap','ftoh','acid_ftca','acid_fts','substances_pasf','sulfonamides_fasa','ethanols_fase','pfeca','pfesa','cl_pfesa','carboxylic_acid','sulfonic_acid')

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
        id_field = 'id'
        fields = ('id', 'sample_id', 'group_id', 'study', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'station', 'site_type', 'sample_detects', 'sample_sum', 'pfna_concentration','pfna_mrl','pfna_dl','pfna_flags','pfds_concentration','pfds_mrl','pfds_dl','pfds_flags','pfhxa_concentration','pfhxa_mrl','pfhxa_dl','pfhxa_flags','pfoa_concentration','pfoa_mrl','pfoa_dl','pfoa_flags','pfos_concentration','pfos_mrl','pfos_dl','pfos_flags','pfba_concentration','pfba_mrl','pfba_dl','pfba_flags','pfdoa_concentration','pfdoa_mrl','pfdoa_dl','pfdoa_flags','pfpea_concentration','pfpea_mrl','pfpea_dl','pfpea_flags','pfhps_concentration','pfhps_mrl','pfhps_dl','pfhps_flags','pfunda_concentration','pfunda_mrl','pfunda_dl','pfunda_flags','pfbs_concentration','pfbs_mrl','pfbs_dl','pfbs_flags','pfpes_concentration','pfpes_mrl','pfpes_dl','pfpes_flags','pfns_concentration','pfns_mrl','pfns_dl','pfns_flags','pfhpa_concentration','pfhpa_mrl','pfhpa_dl','pfhpa_flags','pfhxs_concentration','pfhxs_mrl','pfhxs_dl','pfhxs_flags','pfda_concentration','pfda_mrl','pfda_dl','pfda_flags')

class ntar_sample_data_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = ntar_sample_data
        id_field = 'id'
        fields = ('id', 'sample_id', 'study', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'station', 'site_type', 'sample_detects', 'sample_sum', 'pfas_short_name', 'pfas_long_name', 'flags', 'measurement')

