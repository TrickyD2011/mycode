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
    while True:
        if sign.lower() == "aquarius":
            return ("You got Cleric!", dndclasses.get("Cleric"))
        elif sign.lower() == "picses":
            return ("You got Bard!", dndclasses.get("Bard"))
        elif sign.lower() == "aries":
            return ("You got Ranger!", dndclasses.get("Ranger"))
        elif sign.lower() == "taurus":
            return ("You got Monk!", dndclasses.get("Monk"))
        elif sign.lower() == "gemini":
            return ("You got Druid!", dndclasses.get("Druid"))
        elif sign.lower() == "cancer":
            return ("You got Paladin", dndclasses.get("Paladin"))
        elif sign.lower() == "leo":
            return ("You got Sorcerer!", dndclasses.get("Sorcerer"))
        elif sign.lower() == "virgo":
            return ("You got Wizard!", dndclasses.get("Wizard"))
        elif sign.lower() == "libra":
            return ("You got Rogue!", dndclasses.get("Rogue"))
        elif sign.lower() == "scorpio":
            return ("You got Fighter!", dndclasses.get("Fighter"))
        elif sign.lower() == "sagittarius":
            return ("You got Barbarian!", dndclasses.get("Barbarian"))
        elif sign.lower() == "capricorn":
            return ("You got Warlock!", dndclasses.get("Warlock"))
        else:
            print("I\'m sorry, you either misspelled your astrology or you don't believe in one.\n"+"We recommend you finding out what your western astrology sign is so you can get full benefit.")
            break


def role():
    name = input('What is your name?\n')
    print("We will be using this to save your information for later. Thank you.")
    signs = ["capricorn","sagittarius","scorpio","libra","virgo","leo","cancer","gemini","taurus","aries","pisces","aquarius"]
    sign = input('What is your western astrology sign?\n')
    # dndclass will be the chosen class
    dndclass = astroclass(sign.lower())
    # print(dndclass)
    if sign.lower() not in signs:
        return
    else:
        print(dndclass[0])
        print(dndclass[1])
        
    


    height = input('How tall are you in inches? Rounded up to the nearest inch\n')
    return dndclass

def main():
    """run time applicaiton"""
    print("Welcome to the Dungeons and Dragons gaming application. Here we will determine your ")
    role()



if __name__ == "__main__":
    main()
