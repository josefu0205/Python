from currency_converter import CurrencyConverter


def convert_currency(amount, from_currency, to_currency):
    try:
        c = CurrencyConverter()
        converted_amount = c.convert(amount, from_currency, to_currency)
        return converted_amount
    except Exception as e:
        print(f"Error during currency conversion: {e}")
        return None


try:
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(
            f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
        )
    else:
        print("Conversion failed.")
except ValueError:
    print("Invalid amount entered. Please enter a valid number.")
