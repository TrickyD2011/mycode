#!/usr/bin/env python3

# standard library
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
    # height will be chosen race
    if height >= 74:
        return respdata0.get("dragonborn")
    elif height == 72 or 73:
        return respdata0.get("half-orc")
    elif height == 70 or 71:
        return respdata0.get("human")
    elif height == 68 or 69:
        return respdata0.get("tiefling")
    elif height == 66 or 67:
        return respdata0.get("half-elf")
    elif height == 64 or 65:
        return respdata0.get("elf")
    elif height == 62 or 63:
        return respdata0.get("dwarf")
    elif height == 60 or 61:
        return respdata0.get("gnome")
    elif height <= 59:
        return respdata0.get("halfling")
    else:
        return


def astroclass(sign):
    # Reference Variables
    with open("classes.json", "r") as dndj:
        dndclasses = json.load(dndj)
        if sign.lower() == "aquarius":
            return "You got Cleric!", dndclasses.get("Cleric")
        elif sign.lower == "pisces":
            return "You got Bard!", dndclasses.get("Bard")
        elif sign.lower() == "aries":
            return "You got Ranger!", dndclasses.get("Ranger")
        elif sign.lower() == "taurus":
            return "You got Monk!", dndclasses.get("Monk")
        elif sign.lower() == "gemini":
            return "You got Druid!", dndclasses.get("Druid")
        elif sign.lower() == "cancer":
            return "You got Paladin", dndclasses.get("Paladin")
        elif sign.lower() == "leo":
            return "You got Sorcerer!", dndclasses.get("Sorcerer")
        elif sign.lower() == "virgo":
            return "You got Wizard!", dndclasses.get("Wizard")
        elif sign.lower() == "libra":
            return "You got Rogue!", dndclasses.get("Rogue")
        elif sign.lower() == "scorpio":
            return "You got Fighter!", dndclasses.get("Fighter")
        elif sign.lower() == "sagittarius":
            return "You got Barbarian!", dndclasses.get("Barbarian")
        elif sign.lower() == "capricorn":
            return "You got Warlock!", dndclasses.get("Warlock")
        else:
            print(
                "I\'m sorry, you either misspelled your astrology or you don\'t believe in one.\n"
                "We recommend you finding out what your western astrology sign is so you can get full benefit.")


def role():
    """Gather information to help fill out code later"""
    name = input('What is your name?\n')
    print("We will be using this to save your information for later. Thank you.")
    sign = input('What is your western astrology sign?\n')
    signs = ["capricorn", "sagittarius", "scorpio", "libra", "virgo", "leo", "cancer", "gemini", "taurus", "aries",
             "pisces", "aquarius"]
    # dndclass will be the chosen class
    dndclass = astroclass(sign.lower())
    # print(dndclass)
    if sign.lower() != signs:
        return
    else:
        print(dndclass[0])
        print(dndclass[1])


height = input('How tall are you in inches? Rounded up to the nearest inch\n')


def main():
    """run time application"""
    print("Welcome to the Dungeons and Dragons application. We want to help you decide your first DND Character")
    role()


if __name__ == "__main__":
    main()
