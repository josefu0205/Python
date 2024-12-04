import yfinance as yf
import pandas as pd
from datetime import datetime

def validate_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    if start >= end:
        raise ValueError("Start date must be before end date")

def get_hsi_data(start_date, end_date):
    ticker_symbol = "^HSI"
    try:
        hsi_data = yf.download(ticker_symbol, start=start_date, end=end_date)
        if hsi_data.empty:
            raise ValueError("No data available for the specified date range")
        return hsi_data['Close']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_excel(data, filename):
    try:
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            data.to_excel(writer, sheet_name='HangSengIndex', index=True)
        print(f"Hang Seng Index closing values have been saved to {filename}")
    except Exception as e:
        print(f"Error saving to Excel: {e}")

def main():
    start_date = "2023-09-01"
    end_date = "2023-09-18"

    try:
        validate_dates(start_date, end_date)
        closing_values = get_hsi_data(start_date, end_date)
        if closing_values is not None:
            save_to_excel(closing_values, 'HangSengIndex.xlsx')
    except ValueError as e:
        print(f"Date error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
