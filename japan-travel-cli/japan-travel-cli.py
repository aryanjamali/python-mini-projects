import sys
import requests
import json
import geonamescache

def main():
    while True:
        city = input("Where are you visiting? ")
        if not is_japanese_city(city):
            print(f"Error: '{city.title()}' is not a city in Japan.")
            continue
        
        break

    while True:
        budget = input("What is your budget for the trip? (USD) ")
        try:
            budget = float(budget)
            if budget <= 0:
                print("Error: Budget must be a positive number.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number for the budget.")


    print(get_weather(city))
    print(f"Your budget in JPY is approximately: {usd_to_jpy(budget):,.2f} JPY")
    

def is_japanese_city(city):
    gc = geonamescache.GeonamesCache()
    cities = gc.get_cities()
    for city_info in cities.values():
        if city_info['name'].lower() == city.lower() and city_info['countrycode'] == 'JP':
            return True
    return False

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        temp_c = data["current_condition"][0]["temp_C"]
        description = data["current_condition"][0]["weatherDesc"][0]["value"]

        return f"Weather in {city.title()}: {temp_c}°C, {description}"
    except requests.RequestException:
        return "Error: Could not retrieve weather data."


def usd_to_jpy(usd_amount):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        jpy_rate = data["rates"]["JPY"]
        return usd_amount * jpy_rate
    except requests.RequestException:
        print("Error: Could not retrieve exchange rate data.")
        return None

if __name__ == "__main__":
    main()