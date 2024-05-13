import yfinance as yf

def get_closing_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period="1d")  # Get data for the current day
    closing_price = hist['Close'].iloc[0]
    return closing_price

def main():
    ticker = "0005.HK"  # HK.00005 on Yahoo Finance
    closing_price = get_closing_price(ticker)
    print(f"Closing price of {ticker} is: {closing_price}")

    # Exporting to Excel
    hist = yf.Ticker(ticker).history(period="1d")
    hist.to_excel("HK_00005_closing_price.xlsx")

if __name__ == "__main__":
    main()
