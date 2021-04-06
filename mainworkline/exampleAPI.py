#!/usr/bin/python3

# required to make HTTP requests
import requests

#messages
messge = 'What would you like to play?'

def main():

    # api goes here   
    api = "https://www.dnd5eapi.co/api/classes"

    # sent HTTP GET and create resp, a response object
    resp = requests.get(api)

    # respdata is the JSON attached to our 200+JSON response
    # converted to pythonic list and dictonaries
    respdata = resp.json()

    # display ALL of the data we captured
    print(respdata)


    # spend some time working with dataset
    # see if you can return the data in an interesting format
    # (make it more readable)

    #Test Prints
    #print(*Class["Caster"], sep=", " ) #sep=", "
    #print(*Class["Martial"], sep=", ")
    #print(*Class["Hybrid"], sep=", ")

    #getting info and supplying info
#    print(message)
#    choice = input("Caster, Martial, or Hybrid?")

   # if choice="Caster":
#        print("Here is a list of casters "+ *Class["Caster"], sep=", ")

main()
