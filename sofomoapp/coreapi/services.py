from django.conf import settings
import requests
import ipaddress

def geolocate_ip(ip):
    ipaddress.ip_address(ip)
    url = '{}/{}?access_key={}'.format(settings.GEOIP_URL,ip,settings.GEOIP_TOKEN)
    try:
        res = requests.post(url)
    except:
        raise Exception("Service temporarily unavailable")
    return res.json()