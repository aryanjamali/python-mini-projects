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
        
        weather_report = get_weather(city)
        print(weather_report)
        break

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

        print(f"Weather in {city.title()}: {temp_c}°C, {description}")
    except requests.RequestException:
        return "Error: Could not retrieve weather data."

if __name__ == "__main__":
    main()