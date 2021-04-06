#!/usr/bin/python3

# required to make HTTP requests
import requests

#messages
message = 'What DND class do you want to know about?'

def main():

    # api goes here   
    api = "https://www.dnd5eapi.co/api/classes"

    # sent HTTP GET and create resp, a response object
    resp = requests.get(api)

    # respdata is the JSON attached to our 200+JSON response
    # converted to pythonic list and dictonaries
    respdata = resp.json()

    # display ALL of the data we captured
    #print(respdata)


    # spend some time working with dataset
    # see if you can return the data in an interesting format
    # (make it more readable)

    #Starting
    print(message)
    answer = input('Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard? \n' )
    

    #Test Prints
    if answer.lower()=="barbarian":
        print(respdata.get('results')[0]["name"] ) #Barbarian
    elif answer.lower()== "bard":
        print(respdata.get('results')[1]["name"] ) #Bard
    elif answer.lower()== "cleric":    
        print(respdata.get('results')[2]["name"] ) #Cleric
    elif answer.lower()== "druid":    
        print(respdata.get('results')[3]["name"] ) #Druid
    elif answer.lower()== "fighter":    
        print(respdata.get('results')[4]["name"] ) #Fighter
    elif answer.lower()== "monk":    
        print(respdata.get('results')[5]["name"] ) #Monk
    elif answer.lower()== "paladin":    
        print(respdata.get('results')[6]["name"] ) #Paladin
    elif answer.lower()== "ranger":    
        print(respdata.get('results')[7]["name"] ) #Ranger
    elif answer.lower()== "rogue":    
        print(respdata.get('results')[8]["name"] ) #Rogue
    elif answer.lower()== "sorcerer":    
        print(respdata.get('results')[9]["name"] ) #Sorcerer
    elif answer.lower()== "warlock":    
        print(respdata.get('results')[10]["name"] ) #Warlock
    elif answer.lower()== "wizard":    
        print(respdata.get('results')[11]["name"] ) #Wizard
    else:
        print("Thank you for choosing.")




main()
