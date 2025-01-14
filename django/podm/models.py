from __future__ import unicode_literals
from django.contrib.gis.db import models as gmodels
from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

class pfas_name_classification_info(models.Model):
    id = models.AutoField(primary_key=True)
    abbreviation = models.CharField(max_length=13,null=False)
    chemical_name = models.CharField(max_length=74,null=False)
    casrn = models.CharField(max_length=12,null=False)
    dtxsid = models.CharField(max_length=15,null=False)
    nhanes = models.CharField(max_length=1,null=True)
    carbon_atoms = models.IntegerField()
    formula = models.CharField(max_length=13,null=False)
    pfaa = models.CharField(max_length=1,null=True)
    pfca = models.CharField(max_length=1,null=True)
    pfsa = models.CharField(max_length=1,null=True)
    precursor = models.CharField(max_length=1,null=True)
    ftbs = models.CharField(max_length=1,null=True)
    dipap = models.CharField(max_length=1,null=True)
    ftoh = models.CharField(max_length=1,null=True)
    acid_ftca = models.CharField(max_length=1,null=True)
    acid_fts = models.CharField(max_length=1,null=True)
    substances_pasf = models.CharField(max_length=1,null=True)
    sulfonamides_fasa = models.CharField(max_length=1,null=True)
    ethanols_fase = models.CharField(max_length=1,null=True)
    pfeca = models.CharField(max_length=1,null=True)
    pfesa = models.CharField(max_length=1,null=True)
    cl_pfesa = models.CharField(max_length=1,null=True)
    carboxylic_acid = models.CharField(max_length=1,null=True)
    sulfonic_acid = models.CharField(max_length=1,null=True)

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

class pfas_sample_data(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.IntegerField()
    sample_id = models.CharField(max_length=30,null=False)
    study = models.CharField(max_length=100,null=True)
    pi = models.CharField(max_length=50,null=False)
    units = models.CharField(max_length=20,null=True)
    medium = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=2,null=True)
    zipcode = models.CharField(max_length=7,null=True)
    station = models.CharField(max_length=80,null=True)
    site_type = models.CharField(max_length=20,null=True)
    sample_detects = models.IntegerField()
    sample_sum = models.FloatField()
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

    class Meta:
        managed = False
        db_table = "podm_pfas_sample_data"

class ntar_sample_data(models.Model):
    id = models.AutoField(primary_key=True)
    sample_id = models.CharField(max_length=30,null=False)
    study = models.CharField(max_length=100,null=True)
    pi = models.CharField(max_length=50,null=False)
    units = models.CharField(max_length=20,null=True)
    medium = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=2,null=True)
    zipcode = models.CharField(max_length=7,null=True)
    station = models.CharField(max_length=80,null=True)
    site_type = models.CharField(max_length=20,null=True)
    sample_detects = models.IntegerField()
    sample_sum = models.FloatField()
    pfas_short_name = models.CharField(max_length=25,null=False)
    pfas_long_name = models.CharField(max_length=120,null=False)
    flags = models.CharField(max_length=15,null=False)
    measurement = models.FloatField()

    class Meta:
        managed = False
        db_table = "podm_ntar_sample_data"
