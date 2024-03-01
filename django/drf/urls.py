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
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from . import views
#from .models import pfas_hot_spot, pfas_dust_water, ncserum, ahhs_water_data

# Set URL for gauge geometry Django views
router = routers.DefaultRouter()

router.register(r'pfas_hot_spot', views.drf_pfas_hot_spot_View, 'pfast_hot_spot')
router.register(r'pfas_dust_water', views.drf_pfas_dust_water_View, 'pfast_dust_water')
router.register(r'ahhs_dust_data', views.drf_ahhs_dust_data_View, 'ahhs_dust_data')
router.register(r'ahhs_water_data', views.drf_ahhs_water_data_View, 'ahhs_water_data')
router.register(r'ncserum', views.drf_ncserum_View, 'ncserum')
router.register(r'pfas_in_tapwater_usgs', views.drf_pfas_in_tapwater_usgs_View, 'pfas_in_tapwater_usgs')

urlpatterns = [
    path("api/", include(router.urls)),
]

