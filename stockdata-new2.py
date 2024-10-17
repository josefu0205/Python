import yfinance as yf
import pandas as pd

def get_closing_price(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="1d")
        if hist.empty:
            raise ValueError(f"No data available for ticker {ticker_symbol}")
        closing_price = hist['Close'].iloc[0]
        return closing_price
    except Exception as e:
        print(f"Error retrieving closing price for {ticker_symbol}: {e}")
        return None

def main():
    ticker = "0005.HK"  # HK.00005 on Yahoo Finance
    closing_price = get_closing_price(ticker)
    if closing_price is not None:
        print(f"Closing price of {ticker} is: {closing_price}")

        # Exporting to Excel
        try:
            hist = yf.Ticker(ticker).history(period="1d")
            if not hist.empty:
                # Convert datetime index to timezone-unaware
                hist.index = hist.index.tz_localize(None)
                hist.to_excel("HK_00005_closing_price.xlsx")
                print("Data exported to HK_00005_closing_price.xlsx")
            else:
                print(f"No historical data to export for ticker {ticker}")
        except Exception as e:
            print(f"Error exporting data to Excel: {e}")
    else:
        print("No closing price data available.")

if __name__ == "__main__":
    main()
