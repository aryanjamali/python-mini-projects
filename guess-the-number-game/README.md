# Guess The Number Game

## Overview
A simple yet engaging command-line number guessing game built with Python. The player attempts to guess a randomly generated number between 0 and 100 with feedback on each attempt.

## Key Features
- **Random Number Generation**: Uses Python's `random` module to generate a secret number between 0-100
- **User Input Validation**: Validates that inputs are integers within the valid range
- **Attempt Tracking**: Counts and displays the number of attempts taken to guess correctly
- **Smart Feedback**: Provides helpful hints including "Very close!" for guesses within 5 of the target
- **Error Handling**: Gracefully handles invalid input with informative error messages
- **Game Loop**: Continuous gameplay until the correct number is guessed

## How to Run
1. Ensure Python 3.x is installed on your system
2. Navigate to the project directory
3. Run the following command:
   ```bash
   python guess_the_number_game.py
   ```
4. Follow the on-screen prompts to guess the number
5. The game ends when you correctly guess the secret number

## Concepts Used
- **Random Module**: `random.randint()` for generating unpredictable numbers
- **While Loops**: Continuous game flow until win condition is met
- **Exception Handling**: Try-except blocks to catch `ValueError` for invalid inputs
- **Conditional Logic**: If-elif-else statements for game decision making
- **String Formatting**: F-strings for dynamic output messages
- **User Input**: `input()` function for interactive gameplay