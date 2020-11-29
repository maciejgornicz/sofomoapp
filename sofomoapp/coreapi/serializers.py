from rest_framework import serializers
from rest_framework.exceptions import APIException
from coreapi import models
from coreapi import services

class IPGeoEntrySerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        host = data.get('host')
        if not host:
            raise APIException("No host")
        try:
            ipdata = services.geolocate_ip(host)
            latitude = ipdata['latitude']
            longitude = ipdata['longitude']
        except Exception as e:
            raise APIException(e)
        if latitude and longitude:
            data['latitude'] = latitude
            data['longitude'] = longitude
        else:
            raise APIException("Can't find host data")
        return data
    
    class Meta:
        model = models.IpGeoEntry
        fields = ['id','host', 'latitude', 'longitude']