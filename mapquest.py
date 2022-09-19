import urllib.parse
import requests
from colorama import Fore
from colorama import Style
from texttable import Texttable


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "a7i9vjVY2Qt2Ace15kn8xgHLmfGQEul1"

# functions
t = Texttable()
def printDir():
        if "Welcome" not in each["narrative"] and myUnits == "1":
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " miles)") + "\n")
        if "Welcome" not in each["narrative"] and myUnits == "2":
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)") + "\n")

        if "Welcome" in each["narrative"]:
            print(f"{Style.BRIGHT}{Fore.GREEN}Finally! {Style.RESET_ALL}" + (each["narrative"]) + "\n")

# main
print (f"{Style.BRIGHT}Welcome to Group 4's {Fore.CYAN}MapQuest{Style.RESET_ALL}!")
print (f"Remember to enter 'q' or 'quit' to {Style.BRIGHT}{Fore.RED}exit{Style.RESET_ALL} the program!\n")

name = input("Your name: ")
if name == "quit" or name == "q":
        exit

while True:

    myUnits = input("Type 1 if you prefer Miles\nType 2 if you prefer Kilometers: ")
    if myUnits == "quit" or myUnits == "q":
        break

    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print("=============================================")

        print("Directions from " + (orig) + " to " + (dest))

        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

        if myUnits == "1":
            print("Miles:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        if myUnits == "2":
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

        print("=============================================\n")

    elif json_status == 402:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

        print("**********************************************\n")

    elif json_status == 611:

        print("**********************************************")

        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

        print("**********************************************\n")

    else:

        print("************************************************************************")

        print("For Staus Code: " + str(json_status) + "; Refer to:")

        print("https://developer.mapquest.com/documentation/directions-api/status-codes")

        print("************************************************************************\n")