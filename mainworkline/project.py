#!/usr/bin/env python3

# standard libary
import json

# Import List
import requests


def dndracecalculator(height):
    # API List
    api0 = "https://www.dnd5eapi.co/api/races"

    # Create response object with GET
    resp0 = requests.get(api0)

    # convert response into dictionary
    respdata0 = resp0.json()

    return racecalc


def astroclass(sign):
    # Reference Variables
    with open("classes.json", "r") as dndj:
        dndclasses = json.load(dndj)

    if sign == "aquarius":
        return ("cleric", dndclasses.get("Cleric"))
    elif sign == "picses":
        return ("bard", dndclasses.get("Bard"))
    elif sign == "aries":
        return ("ranger", dndclasses.get("Ranger"))
    elif sign.lower() == "taurus":
        print(monk0)
    elif sign.lower() == "gemini":
        print(druid0)
    elif sign.lower() == "cancer":
        print(paladin0)
    elif sign.lower() == "leo":
        print(sorcerer0)
    elif sign.lower() == "virgo":
        print(wizard0)
    elif sign.lower() == "libra":
        print(rogue0)
    elif sign.lower() == "scorpio":
        print(fighter0)
    elif sign.lower() == "sagittarius":
        print(barbarian0)
    elif sign.lower() == "capricorn":
        print(warlock0)
    else:
        return "I'm sorry, you either misspelled your astrology or you don't believe in one."



# dndfile = open('Classes.txt', 'r')
# bard0 = (dndfile.read()+(print('Bard')))
# barbarian0 = (dndfile.read()+(print('Barbarian')))
# cleric0 = (dndfile.read()+(print('Cleric')))
# druid0 = (dndfile.read()+(print('Druid')))
# fighter0 = (dndfile.read()+(print('Fighter')))
# monk0 = (dndfile.read()+(print('Monk')))
# paladin0 = (dndfile.read()+(print('Paladin')))
# ranger0 = (dndfile.read()+(print('Ranger')))
# rogue0 = (dndfile.read()+(print('Rogue')))
# sorcerer0 = (dndfile.read()+(print('Sorcerer')))
# warlock0 = (dndfile.read()+(print('Warlock')))
# wizard0 = (dndfile.read()+(print('Wizard')))

# Runtime

def role():
    """Gather information to help fill out code later"""
    name = input('What is your name?\n')
    
    sign = input('What is your western astrology sign?\n')
    # dndclass will be the chosen class
    dndclass = astroclass(sign.lower())
    print(dndclass)
    print(dndclass[0])
    print(dndclass[1])


    height = input('How tall are you in inches? Rounded up to the nearest inch\n')
    return dndclass



def main():
    """run time applicaiton"""
    print("Welcome to the Dungeons and Dragons gaming application")
    role()



if __name__ == "__main__":
    main()
