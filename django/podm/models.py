from __future__ import unicode_literals
from django.contrib.gis.db import models as gmodels
from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

class ahhs_dust_data(models.Model):
    id = models.AutoField(primary_key=True)
    sample = models.CharField(max_length=14,null=True)
    pfna_concentration = models.FloatField()
    pfna_mrl = models.FloatField()
    pfna_dl = models.FloatField()
    pfna_flags = models.CharField(max_length=6,null=True)
    pfds_concentration = models.FloatField()
    pfds_mrl = models.FloatField()
    pfds_dl = models.FloatField()
    pfds_flags = models.CharField(max_length=6,null=True)
    pfhxa_concentration = models.FloatField()
    pfhxa_mrl = models.FloatField()
    pfhxa_dl = models.FloatField()
    pfhxa_flags = models.CharField(max_length=6,null=True)
    pfoa_concentration = models.FloatField()
    pfoa_mrl = models.FloatField()
    pfoa_dl = models.FloatField()
    pfoa_flags = models.CharField(max_length=6,null=True)
    pfos_concentration = models.FloatField()
    pfos_mrl = models.FloatField()
    pfos_dl = models.FloatField()
    pfos_flags = models.CharField(max_length=6,null=True)
    pfba_concentration = models.FloatField()
    pfba_mrl = models.FloatField()
    pfba_dl = models.FloatField()
    pfba_flags = models.CharField(max_length=6,null=True)
    pfdoa_concentration = models.FloatField()
    pfdoa_mrl = models.FloatField()
    pfdoa_dl = models.FloatField()
    pfdoa_flags = models.CharField(max_length=6,null=True)
    pfpea_concentration = models.FloatField()
    pfpea_mrl = models.FloatField()
    pfpea_dl = models.FloatField()
    pfpea_flags = models.CharField(max_length=6,null=True)
    pfhps_concentration = models.FloatField()
    pfhps_mrl = models.FloatField()
    pfhps_dl = models.FloatField()
    pfhps_flags = models.CharField(max_length=6,null=True)
    pfunda_concentration = models.FloatField()
    pfunda_mrl = models.FloatField()
    pfunda_dl = models.FloatField()
    pfunda_flags = models.CharField(max_length=6,null=True)
    pfbs_concentration = models.FloatField()
    pfbs_mrl = models.FloatField()
    pfbs_dl = models.FloatField()
    pfbs_flags = models.CharField(max_length=6,null=True)
    pfpes_concentration = models.FloatField()
    pfpes_mrl = models.FloatField()
    pfpes_dl = models.FloatField()
    pfpes_flags = models.CharField(max_length=6,null=True)
    pfns_concentration = models.FloatField()
    pfns_mrl = models.FloatField()
    pfns_dl = models.FloatField()
    pfns_flags = models.CharField(max_length=6,null=True)
    pfhpa_concentration = models.FloatField()
    pfhpa_mrl = models.FloatField()
    pfhpa_dl = models.FloatField()
    pfhpa_flags = models.CharField(max_length=6,null=True)
    pfhxs_concentration = models.FloatField()
    pfhxs_mrl = models.FloatField()
    pfhxs_dl = models.FloatField()
    pfhxs_flags = models.CharField(max_length=6,null=True)
    pfda_concentration = models.FloatField()
    pfda_mrl = models.FloatField()
    pfda_dl = models.FloatField()
    pfda_flags = models.CharField(max_length=6,null=True)

class ahhs_water_data(models.Model):
    id = models.AutoField(primary_key=True)
    sample = models.CharField(max_length=20,null=True)
    pfhps_concentration = models.FloatField()
    pfhps_mrl = models.FloatField()
    pfhps_dl = models.FloatField()
    pfhps_flags = models.CharField(max_length=6,null=True)
    pfhxs_concentration = models.FloatField()
    pfhxs_mrl = models.FloatField()
    pfhxs_dl = models.FloatField()
    pfhxs_flags = models.CharField(max_length=6,null=True)
    pfda_concentration = models.FloatField()
    pfda_mrl = models.FloatField()
    pfda_dl = models.FloatField()
    pfda_flags = models.CharField(max_length=6,null=True)
    pfba_concentration = models.FloatField()
    pfba_mrl = models.FloatField()
    pfba_dl = models.FloatField()
    pfba_flags = models.CharField(max_length=6,null=True)
    pfpea_concentration = models.FloatField()
    pfpea_mrl = models.FloatField()
    pfpea_dl = models.FloatField()
    pfpea_flags = models.CharField(max_length=6,null=True)
    pfpes_concentration = models.FloatField()
    pfpes_mrl = models.FloatField()
    pfpes_dl = models.FloatField()
    pfpes_flags = models.CharField(max_length=6,null=True)
    pfna_concentration = models.FloatField()
    pfna_mrl = models.FloatField()
    pfna_dl = models.FloatField()
    pfna_flags = models.CharField(max_length=6,null=True)
    pfhxa_concentration = models.FloatField()
    pfhxa_mrl = models.FloatField()
    pfhxa_dl = models.FloatField()
    pfhxa_flags = models.CharField(max_length=6,null=True)
    pfbs_concentration = models.FloatField()
    pfbs_mrl = models.FloatField()
    pfbs_dl = models.FloatField()
    pfbs_flags = models.CharField(max_length=6,null=True)
    pfos_concentration = models.FloatField()
    pfos_mrl = models.FloatField()
    pfos_dl = models.FloatField()
    pfos_flags = models.CharField(max_length=6,null=True)
    pfhpa_concentration = models.FloatField()
    pfhpa_mrl = models.FloatField()
    pfhpa_dl = models.FloatField()
    pfhpa_flags = models.CharField(max_length=6,null=True)
    pfoa_concentration = models.FloatField()
    pfoa_mrl = models.FloatField()
    pfoa_dl = models.FloatField()
    pfoa_flags = models.CharField(max_length=6,null=True)
    pfns_concentration = models.FloatField()
    pfns_mrl = models.FloatField()
    pfns_dl = models.FloatField()
    pfns_flags = models.CharField(max_length=6,null=True)

class ncserum(models.Model):
    id = models.AutoField(primary_key=True)
    sample = models.CharField(max_length=15,null=True)
    pfba_concentration = models.FloatField()
    pfba_mrl = models.FloatField()
    pfba_dl = models.FloatField()
    pfba_flags = models.CharField(max_length=1,null=True)
    pfbs_concentration = models.FloatField()
    pfbs_mrl = models.FloatField()
    pfbs_dl = models.FloatField()
    pfbs_flags = models.CharField(max_length=1,null=True)
    pfda_concentration = models.FloatField()
    pfda_mrl = models.FloatField()
    pfda_dl = models.FloatField()
    pfda_flags = models.CharField(max_length=1,null=True)
    pfdoa_concentration = models.FloatField()
    pfdoa_mrl = models.FloatField()
    pfdoa_dl = models.FloatField()
    pfdoa_flags = models.CharField(max_length=1,null=True)
    pfds_concentration = models.FloatField()
    pfds_mrl = models.FloatField()
    pfds_dl = models.FloatField()
    pfds_flags = models.CharField(max_length=1,null=True)
    pfhpa_concentration = models.FloatField()
    pfhpa_mrl = models.FloatField()
    pfhpa_dl = models.FloatField()
    pfhpa_flags = models.CharField(max_length=1,null=True)
    pfhps_concentration = models.FloatField()
    pfhps_mrl = models.FloatField()
    pfhps_dl = models.FloatField()
    pfhps_flags = models.CharField(max_length=6,null=True)
    pfhxa_concentration = models.FloatField()
    pfhxa_mrl = models.FloatField()
    pfhxa_dl = models.FloatField()
    pfhxa_flags = models.CharField(max_length=1,null=True)
    pfhxs_concentration = models.FloatField()
    pfhxs_mrl = models.FloatField()
    pfhxs_dl = models.FloatField()
    pfhxs_flags = models.CharField(max_length=1,null=True)
    pfna_concentration = models.FloatField()
    pfna_mrl = models.FloatField()
    pfna_dl = models.FloatField()
    pfna_flags = models.CharField(max_length=6,null=True)
    pfns_concentration = models.FloatField()
    pfns_mrl = models.FloatField()
    pfns_dl = models.FloatField()
    pfns_flags = models.CharField(max_length=1,null=True)
    pfoa_concentration = models.FloatField()
    pfoa_mrl = models.FloatField()
    pfoa_dl = models.FloatField()
    pfoa_flags = models.CharField(max_length=1,null=True)
    pfos_concentration = models.FloatField()
    pfos_mrl = models.FloatField()
    pfos_dl = models.FloatField()
    pfos_flags = models.CharField(max_length=1,null=True)
    pfpea_concentration = models.FloatField()
    pfpea_mrl = models.FloatField()
    pfpea_dl = models.FloatField()
    pfpea_flags = models.CharField(max_length=1,null=True)
    pfpes_concentration = models.FloatField()
    pfpes_mrl = models.FloatField()
    pfpes_dl = models.FloatField()
    pfpes_flags = models.CharField(max_length=1,null=True)
    pfuda_concentration = models.FloatField()
    pfuda_mrl = models.FloatField()
    pfuda_dl = models.FloatField()
    pfuda_flags = models.CharField(max_length=1,null=True)

class pfas_in_tapwater_usgs(gmodels.Model):
    id = models.AutoField(primary_key=True)
    study = models.CharField(max_length=13,null=True)
    station_na = models.CharField(max_length=50,null=True)
    site_type = models.CharField(max_length=14,null=True)
    sampleyear = models.IntegerField()
    detects = models.IntegerField()
    sum_pfas = models.FloatField()
    pfprs = models.FloatField()
    pfpes = models.FloatField()
    pfpea = models.FloatField()
    pfos = models.FloatField()
    pfoa = models.FloatField()
    pfhxs = models.FloatField()
    pfhxa = models.FloatField()
    pfhps = models.FloatField()
    pfhpa = models.FloatField()
    pfds_num = models.FloatField()
    pfda_num = models.FloatField()
    pfbs = models.FloatField()
    pfba = models.FloatField()
    pf = models.FloatField()
    genx_num = models.FloatField()
    fosa = models.FloatField()
    f6_2fts = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = gmodels.PointField(null=True)

class pfas_data(models.Model):
    data_id = models.AutoField(primary_key=True)
    sample = models.CharField(max_length=30,null=False)
    pfna_concentration = models.FloatField()
    pfna_mrl = models.FloatField()
    pfna_dl = models.FloatField()
    pfna_flags = models.CharField(max_length=6,null=True)
    pfds_concentration = models.FloatField()
    pfds_mrl = models.FloatField()
    pfds_dl = models.FloatField()
    pfds_flags = models.CharField(max_length=6,null=True)
    pfhxa_concentration = models.FloatField()
    pfhxa_mrl = models.FloatField()
    pfhxa_dl = models.FloatField()
    pfhxa_flags = models.CharField(max_length=6,null=True)
    pfoa_concentration = models.FloatField()
    pfoa_mrl = models.FloatField()
    pfoa_dl = models.FloatField()
    pfoa_flags = models.CharField(max_length=6,null=True)
    pfos_concentration = models.FloatField()
    pfos_mrl = models.FloatField()
    pfos_dl = models.FloatField()
    pfos_flags = models.CharField(max_length=6,null=True)
    pfba_concentration = models.FloatField()
    pfba_mrl = models.FloatField()
    pfba_dl = models.FloatField()
    pfba_flags = models.CharField(max_length=6,null=True)
    pfdoa_concentration = models.FloatField()
    pfdoa_mrl = models.FloatField()
    pfdoa_dl = models.FloatField()
    pfdoa_flags = models.CharField(max_length=6,null=True)
    pfpea_concentration = models.FloatField()
    pfpea_mrl = models.FloatField()
    pfpea_dl = models.FloatField()
    pfpea_flags = models.CharField(max_length=6,null=True)
    pfhps_concentration = models.FloatField()
    pfhps_mrl = models.FloatField()
    pfhps_dl = models.FloatField()
    pfhps_flags = models.CharField(max_length=6,null=True)
    pfunda_concentration = models.FloatField()
    pfunda_mrl = models.FloatField()
    pfunda_dl = models.FloatField()
    pfunda_flags = models.CharField(max_length=6,null=True)
    pfbs_concentration = models.FloatField()
    pfbs_mrl = models.FloatField()
    pfbs_dl = models.FloatField()
    pfbs_flags = models.CharField(max_length=6,null=True)
    pfpes_concentration = models.FloatField()
    pfpes_mrl = models.FloatField()
    pfpes_dl = models.FloatField()
    pfpes_flags = models.CharField(max_length=6,null=True)
    pfns_concentration = models.FloatField()
    pfns_mrl = models.FloatField()
    pfns_dl = models.FloatField()
    pfns_flags = models.CharField(max_length=6,null=True)
    pfhpa_concentration = models.FloatField()
    pfhpa_mrl = models.FloatField()
    pfhpa_dl = models.FloatField()
    pfhpa_flags = models.CharField(max_length=6,null=True)
    pfhxs_concentration = models.FloatField()
    pfhxs_mrl = models.FloatField()
    pfhxs_dl = models.FloatField()
    pfhxs_flags = models.CharField(max_length=6,null=True)
    pfda_concentration = models.FloatField()
    pfda_mrl = models.FloatField()
    pfda_dl = models.FloatField()
    pfda_flags = models.CharField(max_length=6,null=True)
    pfuda_concentration = models.FloatField()
    pfuda_mrl = models.FloatField()
    pfuda_dl = models.FloatField()
    pfuda_flags = models.CharField(max_length=6,null=True)

    class Meta:
        managed = False
        db_table = "podm_pfas_data"

class nta_data(models.Model):
    data_id = models.AutoField(primary_key=True)
    sample = models.CharField(max_length=30,null=False)
    pfas_name = models.CharField(max_length=20,null=False)
    measurement = models.FloatField()

    class Meta:
        managed = False
        db_table = "podm_nta_data"

class sample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    study_id = models.IntegerField()
    medium_id = models.IntegerField()
    location_id = models.IntegerField()
    technique_id = models.IntegerField()
    sample = models.CharField(max_length=30,null=False)

    class Meta:
        managed = False
        db_table = "podm_sample"

class study(models.Model):
    study_id = models.AutoField(primary_key=True)
    study = models.CharField(max_length=100,null=True)
    station = models.CharField(max_length=200,null=True) 
    site_type = models.CharField(max_length=50,null=True)
    year = models.IntegerField()
    detects = models.IntegerField()
    sum = models.IntegerField()
    pi = models.CharField(max_length=50,null=False)

    class Meta:
        managed = False
        db_table = "podm_study"
 
class technique(models.Model):
    technique_id = models.AutoField(primary_key=True)
    measurement = models.CharField(max_length=200,null=True)
    units = models.CharField(max_length=20,null=True)

    class Meta:
        managed = False
        db_table = "podm_technique"

class medium(models.Model):
    medium_id = models.AutoField(primary_key=True)
    medium = models.CharField(max_length=20,null=True) 
    description = models.CharField(max_length=300,null=True)
    comments = models.CharField(max_length=500,null=True)
    creation_date = models.DateField(null=True)
    modified_date = models.DateField(null=True)

    class Meta:
        managed = False
        db_table = "podm_medium"

class location(models.Model):
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=2,null=True)
    zipcode = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = False
        db_table = "podm_location"

class pfas_sample_data(models.Model):
    sample_id = models.AutoField(primary_key=True)
    sample = models.CharField(max_length=30,null=False)
    study = models.CharField(max_length=100,null=True)
    pi = models.CharField(max_length=50,null=False)
    units = models.CharField(max_length=20,null=True)
    medium = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=2,null=True)
    zipcode = models.IntegerField()
    pfna_concentration = models.FloatField()
    pfna_mrl = models.FloatField()
    pfna_dl = models.FloatField()
    pfna_flags = models.CharField(max_length=6,null=True)
    pfds_concentration = models.FloatField()
    pfds_mrl = models.FloatField()
    pfds_dl = models.FloatField()
    pfds_flags = models.CharField(max_length=6,null=True)
    pfhxa_concentration = models.FloatField()
    pfhxa_mrl = models.FloatField()
    pfhxa_dl = models.FloatField()
    pfhxa_flags = models.CharField(max_length=6,null=True)
    pfoa_concentration = models.FloatField()
    pfoa_mrl = models.FloatField()
    pfoa_dl = models.FloatField()
    pfoa_flags = models.CharField(max_length=6,null=True)
    pfos_concentration = models.FloatField()
    pfos_mrl = models.FloatField()
    pfos_dl = models.FloatField()
    pfos_flags = models.CharField(max_length=6,null=True)
    pfba_concentration = models.FloatField()
    pfba_mrl = models.FloatField()
    pfba_dl = models.FloatField()
    pfba_flags = models.CharField(max_length=6,null=True)
    pfdoa_concentration = models.FloatField()
    pfdoa_mrl = models.FloatField()
    pfdoa_dl = models.FloatField()
    pfdoa_flags = models.CharField(max_length=6,null=True)
    pfpea_concentration = models.FloatField()
    pfpea_mrl = models.FloatField()
    pfpea_dl = models.FloatField()
    pfpea_flags = models.CharField(max_length=6,null=True)
    pfhps_concentration = models.FloatField()
    pfhps_mrl = models.FloatField()
    pfhps_dl = models.FloatField()
    pfhps_flags = models.CharField(max_length=6,null=True)
    pfunda_concentration = models.FloatField()
    pfunda_mrl = models.FloatField()
    pfunda_dl = models.FloatField()
    pfunda_flags = models.CharField(max_length=6,null=True)
    pfbs_concentration = models.FloatField()
    pfbs_mrl = models.FloatField()
    pfbs_dl = models.FloatField()
    pfbs_flags = models.CharField(max_length=6,null=True)
    pfpes_concentration = models.FloatField()
    pfpes_mrl = models.FloatField()
    pfpes_dl = models.FloatField()
    pfpes_flags = models.CharField(max_length=6,null=True)
    pfns_concentration = models.FloatField()
    pfns_mrl = models.FloatField()
    pfns_dl = models.FloatField()
    pfns_flags = models.CharField(max_length=6,null=True)
    pfhpa_concentration = models.FloatField()
    pfhpa_mrl = models.FloatField()
    pfhpa_dl = models.FloatField()
    pfhpa_flags = models.CharField(max_length=6,null=True)
    pfhxs_concentration = models.FloatField()
    pfhxs_mrl = models.FloatField()
    pfhxs_dl = models.FloatField()
    pfhxs_flags = models.CharField(max_length=6,null=True)
    pfda_concentration = models.FloatField()
    pfda_mrl = models.FloatField()
    pfda_dl = models.FloatField()
    pfda_flags = models.CharField(max_length=6,null=True)
    pfuda_concentration = models.FloatField()
    pfuda_mrl = models.FloatField()
    pfuda_dl = models.FloatField()
    pfuda_flags = models.CharField(max_length=6,null=True)

    class Meta:
        managed = False
        db_table = "podm_pfas_sample_data"

