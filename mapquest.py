import urllib.parse
import requests
from colorama import Fore #colorama for print() color options
from colorama import Style
from texttable import Texttable

main_api = "https://www.mapquestapi.com/directions/v2/route?"
map_api = "https://www.mapquestapi.com/staticmap/v5/map?"
map_api_zoom = "&zoom=16&type=hyb&size=1600,1200@2x"
key = "a7i9vjVY2Qt2Ace15kn8xgHLmfGQEul1"

# functions
t = Texttable()
def printDir():
        if "Welcome" not in each["narrative"] and myUnits == "1":
            print((each["narrative"]) + "\n")
        if "Welcome" not in each["narrative"] and myUnits == "2" or myUnits.isalpha():
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)") + "\n")


        if "Welcome" in each["narrative"]:
            print(f"{Style.BRIGHT}{Fore.GREEN}\n\nFinally! {Style.RESET_ALL}" + (each["narrative"]) + "\n")

        # print(f"This is {Fore.GREEN}color{Style.RESET_ALL}!")
def printCardinalDir():
        if "Arrive" not in each["narrative"]:
            print(f"{Fore.YELLOW}[NOW HEADING " + (each["directionName"]).upper() + f"]{Style.RESET_ALL}")
        if "Arrive" in each["narrative"]:
            print(f"{Style.BRIGHT}{Fore.GREEN}Welcome to your Destination {Style.RESET_ALL}{Style.BRIGHT}{Fore.BLUE}" + name + f"!{Style.RESET_ALL}")

# main
# prints "Welcome messages"
print(f"{Style.BRIGHT}----------------------------------{Style.RESET_ALL}")
print (f"{Style.BRIGHT}| Welcome to Group 4's {Fore.CYAN}MapQuest!{Style.RESET_ALL}{Style.BRIGHT} |{Style.RESET_ALL}")
print(f"{Style.BRIGHT}----------------------------------{Style.RESET_ALL}")

print (f"Remember to enter 'q' or 'quit' to {Style.BRIGHT}{Fore.RED}exit{Style.RESET_ALL} the program!\n")
# Start of user input
name = input("Enter your name: ")
if name == "quit" or name == "q":
        exit()
#While loop that continuously seeks user input
while True:
    print (f"\nRemember to enter 'q' or 'quit' to {Style.BRIGHT}{Fore.RED}exit{Style.RESET_ALL} the program!\n")
    myUnits = input("Unit Measurement - 1 (Miles), 2 (Kilometers): ")
    if myUnits == "quit" or myUnits == "q":
        break
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    myMapURL = map_api + urllib.parse.urlencode({"key":key, "center":dest}) + map_api_zoom

    json_data = requests.get(url).json()

    print(f"{Style.BRIGHT}{Fore.YELLOW}\n\nURL to your directions: {Style.RESET_ALL}" + (url))
    print(f"{Style.BRIGHT}{Fore.YELLOW}\nSattelite image to your destination: {Style.RESET_ALL}" + (myMapURL))


    json_data = requests.get(url).json()
    
    #if Input is correct, retrieve status code.
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:

        print(f"{Style.BRIGHT}============================================={Style.RESET_ALL}")

        print("DIRECTIONS FROM " + (orig.upper()) + " to " + (dest.upper()))

        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

        if myUnits == "1": #Simple check for distance units
            print("Miles:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        if myUnits == "2":
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        if myUnits != "1" or "2":
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        #print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

        print(f"{Style.BRIGHT}============================================={Style.RESET_ALL}")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            printDir()
            printCardinalDir()

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