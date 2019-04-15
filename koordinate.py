#from googlemaps import GoogleMaps
#
# gmaps = GoogleMaps('AIzaSyCCOz-swFmieBTBm6HvvrSRnss-8euo2WA')
# lat, lng = gmaps.address_to_latlng("Italy - Sicily & Sardinia")
# print("lat: "+str(lat))
# print("lng: "+str(lng))
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Italy, Sicily & Sardinia")
print(location)