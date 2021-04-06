#!/usr/bin/env python3

#Library
#Class = ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Blood Hunter"]
Class = {"Caster": ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"], "Martial": ["Barbarian", "Fighter", "Monk", "Rogue", "Blood Hunter"], "Hybrid": ["Artificer", "Paladin", "Ranger"] }
message = 'What kind of character class do you want to try?'


#Test Prints
#print(*Class["Caster"], sep=", " ) #sep=", "
#print(*Class["Martial"], sep=", ")
#print(*Class["Hybrid"], sep=", ")

#getting info and supplying info
print(message)
choice = input("Caster, Martial, or Hybrid?")

if choice="Caster":
    print("Here is a list of casters "+ *Class["Caster"], sep=", ")
