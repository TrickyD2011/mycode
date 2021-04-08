#!/usr/bin/env python3
import random
import requests

# api goes here
api0 = "https://www.dnd5eapi.co/api/classes"

# sent HTTP GET and create resp, a response object
resp0 = requests.get(api0)
# respdata is the JSON attached to our 200+JSON response
# converted to pythonic list and dictionaries
respdata0 = resp0.json()
# Create reference variables
num = [0,1,2,3,4,5,6,7,8,9,10,11]
ranint = random.choice(num)

def main():
    """Describing a Class"""
    answer = input('Enter your name and see which Class you belong to\n')
    # Take the name and do nothing with it
    if answer.lower() == "":
        print('The nameless are a dangerous type. I cannot help you')
    else:
        print(respdata0.get('results')+random.choice(num) ['name'])

main()
