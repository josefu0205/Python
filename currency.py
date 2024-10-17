from forex-python.converter import CurrencyRates, CurrencyCodes

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        # Perform currency conversion
        converted_amount = c.convert(from_currency.upper(), to_currency.upper(), amount)
        return converted_amount
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None


def get_currency_symbol(currency_code):
    cc = CurrencyCodes()
    symbol = cc.get_symbol(currency_code.upper())
    return symbol if symbol else currency_code


try:
    # Input for amount and currencies
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()

    # Get the conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)

    # Get currency symbols for better readability
    from_symbol = get_currency_symbol(from_currency)
    to_symbol = get_currency_symbol(to_currency)

    if converted_amount is not None:
        print(
            f"{from_symbol}{amount} {from_currency} is equal to {to_symbol}{converted_amount:.2f} {to_currency}"
        )
    else:
        print("Conversion failed.")
except ValueError:
    print("Invalid amount. Please enter a valid number")
