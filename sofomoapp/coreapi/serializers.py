from rest_framework import serializers
from rest_framework.exceptions import APIException
from coreapi import models
from coreapi import services

class IPGeoEntrySerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        ip_address = data.get('ip_address')
        if not ip_address:
            raise APIException("No IP address")
        try:
            ipdata = services.geolocate_ip(ip_address)
            latitude = ipdata['latitude']
            longitude = ipdata['longitude']
        except Exception as e:
            raise APIException(e)
        if latitude and longitude:
            data['latitude'] = latitude
            data['longitude'] = longitude
        else:
            raise APIException("Can't find IP address data") #possible when checking valid but restricted ips like 192.168.1.1
        return data
    
    class Meta:
        model = models.IpGeoEntry
        fields = ['id','ip_address', 'latitude', 'longitude']