from rest_framework import routers
from coreapi import views

router = routers.DefaultRouter()
router.register(r'ipgeoentries', views.IpGeoEntryViewset)
