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
    with open("races.json", "r") as dndjs:
        dndraces = json.load(dndjs)
    # function to determine DND race off of height
    if height >= 74:
        return "You are a Dragonborn!", respdata0.get("results")[0]["name"], dndraces.get("dragonborn")
    elif height == 72 or 73:
        return "You are a Half-Orc!", respdata0.get("results")[5]["name"], dndraces.get("half-orc")
    elif height == 70 or 71:
        return "You are a Human! How Ironic?", respdata0.get("results")[7]["name"], dndraces.get("human")
    elif height == 68 or 69:
        return "You are a Tiefling!", respdata0.get("results")[8]["name"], dndraces.get("tiefling")
    elif height == 66 or 67:
        return "You are a Half-Elf!", respdata0.get("results")[4]["name"], dndraces.get("half-elf")
    elif height == 64 or 65:
        return "You are an Elf!", respdata0.get("results")[2]["name"], dndraces.get("elf")
    elif height == 62 or 63:
        return "You are a Dwarf!", respdata0.get("results")[1]["name"], dndraces.get("dwarf")
    elif height == 60 or 61:
        return "You are a Gnome!", respdata0.get("results")[3]["name"], dndraces.get("gnome")
    elif height <= 59:
        return "You are a Halfling!", respdata0.get("results")[6]["name"], dndraces.get("halfling")
    else:
        return


def racecomp():
    # Query Height
    def truth():
        # Loop until integer is given
        while True:
            try:
                x = int(input('How tall are you in inches? Remember, 5ft is equal to 60in\n'))
                if x >= 0:
                    print("Thank you")
                elif x > 100:
                    print("You aren\'t fooling anyone")
                else:
                    break
            except ValueError:
                print("I need your height to be written in numbers only. Please try again")
                continue
            return x
    height = truth()
    dndrace = dndracecalculator(height)
    print(dndrace[0])
    print(dndrace[2])


def astroclass(sign):
    # Reference Variables
    with open("classes.json", "r") as dndj:
        dndclasses = json.load(dndj)
    while True:
        if sign.lower() == "aquarius":
            return "You got Cleric!", dndclasses.get("Cleric")
        elif sign.lower() == "pisces":
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
                "I\'m sorry, you either misspelled your astrology or you don't believe in one.\n" +
                "We recommend you finding out what your western astrology sign is so you can get full benefit.")
            break


def role():
    name = input('What is your name?\n')
    print("We will be using this to save your information for later. Thank you.")
    signs = ["capricorn", "sagittarius", "scorpio", "libra", "virgo", "leo", "cancer", "gemini", "taurus", "aries",
             "pisces", "aquarius"]
    sign = input('What is your western astrology sign?\n')
    # dndclass will be the chosen class
    dndclass = astroclass(sign.lower())
    # print(dndclass)
    if sign.lower() not in signs:
        return
    else:
        print(dndclass[0])
        print(dndclass[1])
        return dndclass


def main():
    """run time application"""
    print("Welcome to the Dungeons and Dragons gaming application. Here we will determine your ")
    role()
    racecomp()
    

if __name__ == "__main__":
    main()

