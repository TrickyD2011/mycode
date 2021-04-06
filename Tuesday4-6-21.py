#!/usr/bin/python3
"""RSFeeser | Good Morning Review
Given the data contained in issnow,
Write a program that displays the current

<timestamp> this iss is:
Longitude - <longitude>
Latitude - <latitude>
"""
#Source Code
issnow = {"message": "success", "timestamp": 1617724195, "iss_position": {"longitude": "-90.8173", "latitude": "6.8474"}}

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
