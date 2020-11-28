from django.conf import settings
import requests
import ipaddress

def get_ip_geolocalization(ip):
    ipaddress.ip_address(ip)
    url = '{}test/{}?access_key={}'.format(settings.GEOIP_URL,ip,settings.GEOIP_TOKEN)
    try:
        res = requests.post(url)
    except:
        raise Exception("Service temporarily unavailable")
    return res.json()