import requests
import pprint
def get_astrological_sign(month, day):
    zodiac_signs = [
        ("Capricorn", (1, 20)), ("Aquarius", (2, 18)),
        ("Pisces", (3, 20)), ("Aries", (4, 20)),
        ("Taurus", (5, 20)), ("Gemini", (6, 20)),
        ("Cancer", (7, 22)), ("Leo", (8, 22)),
        ("Virgo", (9, 22)), ("Libra", (10, 22)),
        ("Scorpio", (11, 21)), ("Sagittarius", (12, 21)),
        ("Capricorn", (12, 31))
    ]
    for sign, (end_month, end_day) in zodiac_signs:
        if (month, day) <= (end_month, end_day):
            return sign
    return "Capricorn"

def main():
    letterHead = """
               _             _                      _____ _               _             
     /\       | |           | |                    / ____| |             | |            
    /  \   ___| |_ _ __ ___ | | ___   __ _ _   _  | |    | |__   ___  ___| | _____ _ __ 
   / /\ \ / __| __| '__/ _ \| |/ _ \ / _` | | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
  / ____ \\__ \ |_| | | (_) | | (_) | (_| | |_| | | |____| | | |  __/ (__|   <  __/ |   
 /_/    \_\___/\__|_|  \___/|_|\___/ \__, |\__, |  \_____|_| |_|\___|\___|_|\_\___|_|   
                                      __/ | __/ |                                       
                                     |___/ |___/                                        
"""
    print(letterHead)
    while True:
        print("Welcome to Astrology Checker CLI App!")
        print("Find out your star sign and forecast with our calculator")
        dob = input("Enter your date of birth (MM-DD-YYYY) or enter \"Quit\" to close app: ")
        if dob == "Quit":
            print("Thank you for using Astrology Checker CLI App!")
            break
        dobList = dob.split("-")
        month = int(dobList[0])
        day = int(dobList[1])
        astrologicalSign = get_astrological_sign(month, day)
        print(f"You are {astrologicalSign}!")
        redo = input("Do you wish to go back and add another D.O.B? (Y / N): ")

        if redo == "Y":
            print("\n")
            continue

        wantForecast = input("Do you want a forecast for your astrological sign? (Y / N) (Will be a short wait): ")
        print("\n")
        if wantForecast == "Y":
            pprint.pprint(requests.get(f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={astrologicalSign.lower()}&day=TODAY").json()['data']['horoscope_data'])
            print("")
            anotherAstrology = input("Do you wish to see another astrology (Y / N)? ")
            if anotherAstrology == "Y":
                nextOption = input("Enter Astrology name: ")
                print("")
                pprint.pprint(requests.get(f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={nextOption.lower()}&day=TODAY").json()['data']['horoscope_data'])
                print("")
            else:
                continue

        elif wantForecast == "N":
            continue

main()
