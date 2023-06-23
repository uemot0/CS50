# Currency Converter
#### Video Demo: https://youtu.be/5SDumqc9NgQ
#### Description:

This is a simple currency converter program written in Python. It allows you to convert between different currencies using the latest exchange rates from Open Exchange Rates.

## Features

- Convert between different currencies: Enter the amount and the currencies you want to convert from and to, and the program will calculate the converted amount using the latest exchange rates.
- Update exchange rates: Update the exchange rates used by the program to ensure that you're always using the most up-to-date information.
- Get historical exchange rate data: Enter a date and the program will retrieve historical exchange rate data for that date.

## Usage

To use the currency converter, you need to have Python installed on your computer. You also need to install the `requests` library using the command `pip install requests`.

Once you have Python and the `requests` library installed, you can run the program by navigating to the directory where you saved the `currency_converter.py` file and running the command `python currency_converter.py`.

This will start the program and display a menu with several options:

1. Convert currency: Choose this option to convert between different currencies. You will be prompted to enter the amount and the currencies you want to convert from and to.
2. Update exchange rates: Choose this option to update the exchange rates used by the program.
3. Get historical data: Choose this option to retrieve historical exchange rate data for a specific date. You will be prompted to enter the date.
4. Quit: Choose this option to exit the program.

## Owner

This project was created by Pedro Uemoto Aufieri.

## How the code was made

The code for this project was written in Python. It uses the `requests` library to make API calls to Open Exchange Rates to get the latest exchange rates and historical data. The program has a simple command-line interface that allows users to interact with it and perform various actions.

The code is organized into several functions that perform different tasks such as updating exchange rates, converting currencies, and getting historical data. The `main()` function is responsible for displaying the menu and handling user input.

The `update_exchange_rates()` function uses the Open Exchange Rates API to get the latest exchange rates and updates the `exchange_rates` dictionary with the new data.

The `convert_currency()` function takes an amount and two currency codes as arguments and uses the data in the `exchange_rates` dictionary to calculate the converted amount.

The `get_historical_data()` function takes a date as an argument and uses the Open Exchange Rates API to retrieve historical exchange rate data for that date. It then displays the data on screen.