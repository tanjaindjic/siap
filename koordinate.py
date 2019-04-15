# from googlemaps import GoogleMaps
#
# gmaps = GoogleMaps('AIzaSyBfAColFj5kqMuSa8WG7NJ2WJZte3O4x8Y')
# lat, lng = gmaps.address_to_latlng("Italy - Sicily & Sardinia")
# print("lat: "+str(lat))
# print("lng: "+str(lng))



# import requests
# url = 'https://maps.googleapis.com/maps/api/geocode/json?address=Italy+Sicily+Sardinia&key=AIzaSyBfAColFj5kqMuSa8WG7NJ2WJZte3O4x8Y'
# response = requests.post(url, data=None)
# print(response.text)

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("Sicily, Italy")
print(location.longitude)