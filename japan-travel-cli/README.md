# Japan Weather & Currency CLI Assistant

[![Work in Progress](https://img.shields.io/badge/status-work--in--progress-orange.svg)](#roadmap)

A small command-line travel assistant for Japan. The project currently helps a traveler:

- validate that a city exists in Japan,
- fetch the current weather for that city,
- ask for a travel budget in USD,
- convert that budget into Japanese Yen using a live exchange-rate API.

This project is still under active development, but the core workflow already works end-to-end.

## Current Project Status

The current version of the app supports the following flow:

1. Ask the user for a city name.
2. Check whether the city is a Japanese city.
3. If valid, fetch the live weather from `wttr.in`.
4. Ask for a budget in USD.
5. Retrieve the current USD-to-JPY conversion rate from an exchange-rate API.
6. Print the converted amount in JPY.

## What the App Does Right Now

The assistant currently includes these features:

- Interactive city.prompt in the terminal
- Japanese city validation using `geonamescache`
- Weather lookup with `wttr.in`
- Temperature and weather description display
- Budget input validation for positive numeric values
- Real-time USD to JPY conversion
- Friendly error handling for bad city names, invalid budget input, and API failures

## Project Structure

```text
japan-travel-cli/
├── japan-travel-cli.py
├── README.md
```

## Main Code Flow

The application is intentionally lightweight and organized around a few key functions:

- `main()`
  - Runs the user interaction loop
  - Prompts for city and budget
  - Validates input
  - Calls weather and conversion functions

- `is_japanese_city(city)`
  - Uses `geonamescache` to check whether a city belongs to Japan

- `get_weather(city)`
  - Calls the wttr.in JSON API
  - Extracts the current temperature and description

- `usd_to_jpy(usd_amount)`
  - Calls a live exchange-rate API
  - Converts USD into JPY using the current rate

## Example Usage

Run the script:

```bash
python japan-travel-cli.py
```

Example interaction:

```text
Where are you visiting? Tokyo
What is your budget for the trip? (USD) 250
Weather in Tokyo: 27°C, Partly cloudy
Your budget in JPY is approximately: 39,625.00 JPY
```

If the city is not recognized as part of Japan, the app asks again:

```text
Where are you visiting? Paris
Error: 'Paris' is not a city in Japan.
```

If the budget is invalid, the user is prompted again:

```text
What is your budget for the trip? (USD) abc
Error: Please enter a valid number for the budget.
```

## Installation

### Requirements

- Python 3.9+
- Internet access for the weather and currency APIs

### Setup

Clone the repository:

```bash
git clone <your-repository-url>
cd japan-travel-cli
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install requests geonamescache
```

## Dependencies

This project currently uses:

- `requests` for API calls
- `geonamescache` for city lookup validation

## Current Roadmap

The project is still in progress. The next development steps are likely to include:

- [ ] add clothing recommendations based on weather temperature
- [ ] persist user queries in a history log or JSON file
- [ ] improve city lookup speed with an indexed dictionary/set
- [ ] add stronger validation for empty or malformed input
- [ ] add automated tests for validation, API handling, and conversion logic
- [ ] support broader travel features such as daily itinerary suggestions or local tips

## Notes

This project is a personal learning project and is not yet a finished production tool. It is already usable as a simple travel assistant prototype, but there is room for better structure, persistence, and testing before it becomes more feature-complete.

## License

This project is currently unlicensed and remains a personal learning project.