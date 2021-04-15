#!/usr/bin/python3

# python3 -m pip install requests
import requests
import json


def apikey():
    """returns a str containing our API key"""
    # place your API key within /home/student/nasa.cred
    with open("/home/student/nasa.cred", "r") as nc:
        apikey = nc.readline()   # returns just the first line in a file
        return apikey.rstrip("\n")   # return the api key missing any "extra" \n char



def main():
    """run-time code"""
    # you can use the API if you want, but there are LOTS to choose from!
    # choose your OWN nasa API adventure!
    api = f"https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"  # if your API choose requires MORE key/values, you may need to add more
                                                                     # than JUST api_key={apikey()}

    # sends HTTP GET to our API
    nasaresp = requests.get(api)

    # we now have a 200 + JSON response
    nasajson = nasaresp.json()  # strip JSON off our response

    # display the JSON on the screen
    # print(nasajson) # you are encouraged to display your data in a more easily read format!

    
    # Printing the latest Sol Date weather in human readable format
    # parsed = json.loads()
    print(json.dumps(nasajson.get("841"), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()

