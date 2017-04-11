import os
from geopy import geocoders


def geocode(address):
    g = geocoders.Nominatim()
    place, (lat, lng) = g.geocode(address)
    print(place, lat, lng)
    return place, lat, lng

geocode('5 Braemor Drive, Churchtown, Co.Dublin')