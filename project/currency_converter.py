import requests
from datetime import datetime

exchange_rates = {
    'USD': 1,
    'EUR': 0.85,
    'BRL': 5.24,
    'GBP': 0.72,
    'JPY': 110.14,
    'CHF': 0.92,
    'CAD': 1.25,
    'AUD': 1.36,
    'NZD': 1.43,
    'ZAR': 14.51,
    'CNY': 6.47,
    'BTC': 0.000007, # current exchange rate for Bitcoin
    'HKD': 7.77,
    'SGD': 1.34,
    'THB': 33.23,
    'SEK': 8.57,
    'NOK': 8.54,
    'MXN': 20.06,
    'INR': 74.24,
    'RUB': 73.50,
}

def update_exchange_rates():
    app_id = '331039272d5f44fe89dc8d22626770a9' #APPID
    url = f'https://openexchangerates.org/api/latest.json?app_id={app_id}'
    response = requests.get(url)
    data = response.json()
    rates = data['rates']
    exchange_rates.update(rates)

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates:
        print(f"Sorry, I don't have the exchange rate for {from_currency}.")
        return
    if to_currency not in exchange_rates:
        print(f"Sorry, I don't have the exchange rate for {to_currency}.")
        return
    rate = exchange_rates[to_currency] / exchange_rates[from_currency]
    converted_amount = amount * rate
    print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}.")

def get_historical_data(date):
    app_id = '331039272d5f44fe89dc8d22626770a9' #APPID
    url = f'https://openexchangerates.org/api/historical/{date}.json?app_id={app_id}'
    response = requests.get(url)
    data = response.json()
    rates = data['rates']

    print(f"\nExchange rates for {date}:")

    for currency, rate in rates.items():
        print(f"{currency}: {rate}")

def main():
    print("Welcome to the Currency Converter!")

    while True:
        print("\nPlease choose an option:")
        print("1. Convert currency")
        print("2. Update exchange rates")
        print("3. Get historical data")
        print("4. Quit")

        choice = input("> ")

        if choice == "1":
            amount = float(input("Enter the amount: "))
            from_currency = input("Enter the currency to convert from (e.g. USD): ")
            to_currency = input("Enter the currency to convert to (e.g. EUR): ")
            convert_currency(amount, from_currency, to_currency)

        elif choice == "2":
            update_exchange_rates()
            print("Exchange rates updated successfully!")

        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")

            try:
                datetime.strptime(date, '%Y-%m-%d')
                get_historical_data(date)

            except ValueError:
                print("Invalid date format.")

        elif choice == "4":
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()