from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import datetime

geolocator = Nominatim(user_agent="http")


def calculate_distance(city1, city2):
    c1 = geolocator.geocode(city1 + ',' + 'India')
    c1_cordinates = (c1.latitude, c1.longitude)

    c2 = geolocator.geocode(city2 + ',' + 'India')
    c2_cordinates = (c2.latitude, c2.longitude)

    distance = geodesic(c1_cordinates, c2_cordinates).km
    print(distance)

print(datetime.today().strftime('%Y-%m-%d'))

