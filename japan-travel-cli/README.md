# Japan Weather & Currency CLI Assistant

[![Work in Progress](https://img.shields.io/badge/status-work--in--progress-orange.svg)](#roadmap)

A command-line assistant for travelers and residents in Japan. The project is being developed to combine live Japanese weather data, currency conversion, travel-focused recommendations, and a lightweight history of user queries.

## Current Status

The current prototype:

- Prompts for a city name.
- Checks whether the city is listed as a Japanese city.
- Retrieves the current weather for the city from `wttr.in`.
- Displays the current temperature and weather description.

The exchange-rate, budget-conversion, clothing-recommendation, and query-history features are planned next.

## Architecture & Code Highlights

The application is intentionally small and modular:

- `main()` controls the interactive command-line flow and retries invalid city names.
- `is_japanese_city()` uses the `geonamescache` package to validate Japanese cities.
- `get_weather()` calls the `wttr.in` JSON endpoint and extracts the current temperature and weather description.
- The planned city-validation improvement is an indexed dictionary or set lookup, giving O(1) average lookup time instead of scanning every cached city for each query.
- Network failures are handled through `requests.RequestException` so the CLI can report weather-service errors cleanly.

## Feature Checklist

### Completed

- [x] Interactive command-line city input
- [x] Japanese-city validation with `geonamescache`
- [x] Current weather retrieval from `wttr.in`
- [x] Temperature and weather-condition display
- [x] Basic handling for invalid city names and request failures

### Planned

- [ ] Add real-time JPY exchange rates against USD or Toman
- [ ] Prompt for a travel budget
- [ ] Convert the budget into Japanese Yen
- [ ] Support weather lookup for additional Japanese cities
- [ ] Add clothing recommendations based on temperature
- [ ] Store query details and timestamps in `history.json` or `log.txt`
- [ ] Build an O(1) indexed city lookup for faster validation
- [ ] Add input validation for empty or malformed values
- [ ] Add tests for validation, API responses, and recommendation logic

## Installation

### Requirements

- Python 3.9 or newer
- Internet access for the `wttr.in` request

### Setup

Clone the repository and enter the project directory:

```bash
git clone <your-repository-url>
cd japan-travel-cli
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the current dependencies:

```bash
python -m pip install requests geonamescache
```

## Usage

Run the assistant with:

```bash
python japan-travel-cli.py
```

Enter a Japanese city when prompted, for example:

```text
Where are you visiting? Tokyo
Weather in Tokyo: 24°C, Partly cloudy
```

If the city is not recognized as a Japanese city, the program asks again. Weather data requires a working internet connection.

## Roadmap

The next development stage will add exchange-rate retrieval and budget conversion. After that, the assistant will provide temperature-based clothing advice and persist each query with a timestamp for later review.

## License

This project is currently a personal learning project. A formal license may be added later.
