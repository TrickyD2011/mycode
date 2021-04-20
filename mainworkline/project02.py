#!/usr/bin/env python3

# python3 -m pip install crayons
# standard library
import json
import os
import crayons
import sys
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
    if height in range (74,107):
        return "You are a Dragonborn!", respdata0.get("results")[0]["name"], dndraces.get("dragonborn")
    elif height in range (72,73):
        return "You are a Half-Orc!", respdata0.get("results")[5]["name"], dndraces.get("half-orc")
    elif height in range (70,71):
        return "You are a Human! How Ironic?", respdata0.get("results")[7]["name"], dndraces.get("human")
    elif height in range (68,69):
        return "You are a Tiefling!", respdata0.get("results")[8]["name"], dndraces.get("tiefling")
    elif height in range (66,67):
        return "You are a Half-Elf!", respdata0.get("results")[4]["name"], dndraces.get("half-elf")
    elif height in range (64,65):
        return "You are an Elf!", respdata0.get("results")[2]["name"], dndraces.get("elf")
    elif height in range (62,63):
        return "You are a Dwarf!", respdata0.get("results")[1]["name"], dndraces.get("dwarf")
    elif height in range (60,61):
        return "You are a Gnome!", respdata0.get("results")[3]["name"], dndraces.get("gnome")
    elif height in range (0,59):
        return "You are a Halfling!", respdata0.get("results")[6]["name"], dndraces.get("halfling")
    else:
        return


def racecomp():
    # Query Height
    def truth():
        # Loop until integer is given
        while True:
            try:
                x = int(input(crayons.red('How tall are you in inches? Remember, 5ft is equal to 60in\n', bold=True)))
                if x in range (0,100):
                    print(crayons.green("Thank you"))
                elif x > 100:
                    print(crayons.magenta("You aren\'t fooling anyone", bold=True))
                    continue
                else:
                    break
            except ValueError:
                print(crayons.red("I need your height to be written in numbers only. Please try again"))
                continue
            return x
    height = truth()
    dndrace = dndracecalculator(height)
    print(crayons.cyan("Fact checking with online resources: "), crayons.blue(dndrace[1]))
    print(crayons.green(dndrace[0]))
    print(crayons.yellow(dndrace[2]))
    return dndrace


def astroclass(sign):
    # Reference Variables
    with open("classes.json", "r") as dndj:
        dndclasses = json.load(dndj)
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
        print(crayons.red(
            "I\'m sorry, you either misspelled your astrology or you don't believe in one.\n" +
            "We recommend you finding out what your western astrology sign is so you can get full benefit."))


def role():
    signs = ["capricorn", "sagittarius", "scorpio", "libra", "virgo", "leo", "cancer", "gemini", "taurus", "aries",
             "pisces", "aquarius"]
    sign = input(crayons.red('What is your western astrology sign?\n', bold=True))
    # dndclass will be the chosen class
    dndclass = astroclass(sign.lower())
    # print(dndclass)
    if sign.lower() not in signs:
        sys.exit(0)
    else:
        print(crayons.green(dndclass[0]))
        print(crayons.yellow(dndclass[1]))
        return dndclass


#def saving(names, dndclass, dndrace):
#    look = "/home/student/mycode/mainworkline/{}.txt".format(names)
#    if os.path.exists(look):
#        print("You already have a file.")
#        r = open("{}.txt".format(names), "r")
#        print(r.read())
#        r.close()
#    else:
#        f = open("{}.txt".format(names), "w")
#        f.write(dndclass + "\n")
#        f.write(dndrace + "\n")
#        f.close()

def names():
    names = input(crayons.red('First, what is your name? \n', bold=True))
    print(crayons.green("We will save your character as a text named after you"))
    print(crayons.yellow(names))
    return names

def main():
    """run time application"""
    print(crayons.white("Welcome to the Dungeons and Dragons gaming. Here we will determine your first Character.\n", bold=True ))
    names()
    role()
    racecomp()
#    saving(names, dndclass, dndrace)

if __name__ == "__main__":
    main()

