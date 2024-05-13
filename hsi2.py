import yfinance as yf
import pandas as pd

# Define the ticker symbol for Hang Seng Index
ticker_symbol = "^HSI"

# Define the start and end date for the data retrieval
start_date = "2023-09-01"
end_date = "2023-09-18"

# Fetch Hang Seng Index data from Yahoo Finance
hsi_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Extract only the 'Close' column
closing_values = hsi_data['Close']

# Create a Pandas DataFrame
df = pd.DataFrame(closing_values)

# Create a new Excel writer object
excel_writer = pd.ExcelWriter('HangSengIndex.xlsx', engine='openpyxl')

# Write the data to an Excel sheet
df.to_excel(excel_writer, sheet_name='HangSengIndex', index=False)

# Save the Excel file
excel_writer._save()

print("Hang Seng Index closing values have been saved to HangSengIndex.xlsx")
