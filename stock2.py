import yfinance as yf
from openpyxl import Workbook

def get_closing_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period="1d")  # Get data for the current day
    closing_price = hist['Close'].iloc[0]
    return closing_price

def main():
    ticker = "0005.HK"
    closing_price = get_closing_price(ticker)
    
    # Create a new Excel workbook and get the active sheet
    wb = Workbook()
    ws = wb.active

    # Set the value of cell 10B to the closing price
    ws['B10'] = closing_price

    # Save the workbook
    wb.save("HK_00005_closing_price.xlsx")

if __name__ == "__main__":
    main()
