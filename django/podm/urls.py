"""Map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.urls import path, include
from rest_framework import routers
from . import views

# Set URL for gauge geometry Django views
router = routers.DefaultRouter()

router.register(r'ahhs_dust_data', views.podm_ahhs_dust_data_View, 'ahhs_dust_data')
router.register(r'ahhs_water_data', views.podm_ahhs_water_data_View, 'ahhs_water_data')
router.register(r'ncserum', views.podm_ncserum_View, 'ncserum')
router.register(r'pfas_in_tapwater_usgs', views.podm_pfas_in_tapwater_usgs_View, 'pfas_in_tapwater_usgs')
router.register(r'pfas_sample_data', views.podm_pfas_sample_data_View, 'pfas_sample_data')

urlpatterns = [
    path("api/", include(router.urls)),
]

