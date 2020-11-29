from django.db import models

class IpGeoEntry(models.Model):
    """IP entry with geolocation data"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    host = models.CharField(max_length=100,verbose_name="Host", unique=True)
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    class Meta:
        verbose_name = "IP Geolocation"
