#!/usr/bin/env python3

import requests
# api goes here
api0 = "https://www.dnd5eapi.co/api/classes"
api1 = "https://www.dnd5eapi.co/api/proficiencies"

# sent HTTP GET and create resp, a response object
resp0 = requests.get(api0)
resp1 = requests.get(api1)
# respdata is the JSON attached to our 200+JSON response
# converted to pythonic list and dictionaries
respdata0 = resp0.json()
respdata1 = resp1.json()
# display ALL of the data we captured
# print(respdata1)
# Create reference variables
message = "Learn about a DND Class"
barbarian0 = respdata0.get('results')[0]["name"]
bard0 = respdata0.get('results')[1]["name"]
cleric0 = respdata0.get('results')[2]["name"]
druid0 = respdata0.get('results')[3]["name"]
fighter0 = respdata0.get('results')[4]["name"]
monk0 = respdata0.get('results')[5]["name"]
paladin0 = respdata0.get('results')[6]["name"]
ranger0 = respdata0.get('results')[7]["name"]
rogue0 = respdata0.get('results')[8]["name"]
sorcerer0 = respdata0.get('results')[9]["name"]
warlock0 = respdata0.get('results')[10]["name"]
wizard0 = respdata0.get('results')[11]["name"]


def main():
    """Describing a Class"""
    print(message)
    answer = input('Barbarian, Bard, Cleric, Druid, Fighter, Monk,\n'
                   'Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard? \n')
    if answer.lower() == "barbarian":
        print(barbarian0)
    elif answer.lower() == "bard":
        print(bard0)
    elif answer.lower() == "cleric":
        print(cleric0)
    elif answer.lower() == "druid":
        print(druid0)
    elif answer.lower() == "fighter":
        print(fighter0)
    elif answer.lower() == "monk":
        print(monk0)
    elif answer.lower() == "paladin":
        print(paladin0)
    elif answer.lower() == "ranger":
        print(ranger0)
    elif answer.lower() == "rogue":
        print(rogue0)
    elif answer.lower() == "sorcerer":
        print(sorcerer0)
    elif answer.lower() == "warlock":
        print(warlock0)
    elif answer.lower() == "wizard":
        print(wizard0)
    else:
        print("See you next time.")


main()

