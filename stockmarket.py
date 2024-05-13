import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os
# Get current date and time
now = datetime.now()

# Format the date and time string
timestamp_str = now.strftime('%Y%m%d_%H%M%S')


## Define the list of tickers
tickers = ['1850.HK','3888.HK','6098.HK','1128.HK','6918.HK','600355.SS','002796.SZ']


## Set the end date to today
end_date = datetime.today()
print(end_date)

## Set the start date to 2 years ago
start_date = end_date - timedelta(days = 7)
print(start_date)

## Create an empty DataFrame to store the close prices
close_df = pd.DataFrame()

## Download the close prices for each ticker
for ticker in tickers:
    data = yf.download(ticker, start = start_date, end = end_date)
    close_df[ticker] = data['Close']

## Display the DataFrame
print(close_df)

## Set the output folder path
output_folder = "/Users/josephfu/Python/"

# Incorporate the timestamp into the filename
filename = f"stockprice_{timestamp_str}.xlsx"
print(filename)

## Export the DataFrame to Excel
output_file = os.path.join(output_folder, filename)
close_df.to_excel(output_file)