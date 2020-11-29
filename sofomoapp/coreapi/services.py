from django.conf import settings
import requests
import ipaddress

def geolocate_ip(ip):
    #ipaddress.ip_address(ip)
    url = '{}/{}?access_key={}'.format(settings.GEOIP_URL,ip,settings.GEOIP_TOKEN)
    res = requests.post(url)
    return res.json()