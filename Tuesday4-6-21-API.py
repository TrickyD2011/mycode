#!/usr/bin/python3
"""RSFeeser | Good Morning Review
Given the data contained in issnow,
Write a program that displays the current

<timestamp> this iss is:
Longitude - <longitude>
Latitude - <latitude>
"""

#Library
import requests

#Source Code
def main():
    issnow = requests.get("http:api.open-notify.org/iss-now.json") # this returns an HTTP 200+json
    issnow = issnow.json()


    #Code Timestamp
    import datetime;
    ct = datetime.datetime.now()
    print("current time: -", ct)
    ts = ct.timestamp()
    print("timestamp: -", ts)

    #Code Long amd Lat
    #import urllib,urllib2
    #import googlemaps
    #import GoogleMaps
    #address = "5548 Normandy Dr SE, Olympia, Washington, USA 98501"
    #add = GoogleMaps().address_to_latlng(addresss)
    #print(add)

    longit = issnow.get("iss_position").get("longitude")
    print("Longitude:- ", longit)

    latit = issnow.get("iss_position").get("latitude")
    print("Latitude:_ ", latit)
main()
