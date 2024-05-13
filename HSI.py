import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the URL to fetch Hang Seng Index data
url = 'https://www.bloomberg.com/quote/HSI:IND'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element that contains the closing value (usually a <div> with a specific class)
closing_value_element = soup.find('div', class_='price')

if closing_value_element:
    # Extract the closing value from the element
    closing_value = closing_value_element.text.strip()

    # Create a Pandas DataFrame to store the data
    data = {'Date': [pd.Timestamp.now().date()], 'Hang Seng Index Closing Value': [closing_value]}
    df = pd.DataFrame(data)

    # Define the name of the Excel spreadsheet
    excel_file = 'HangSengIndex.xlsx'

    # Write the DataFrame to an Excel file
    with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Hang Seng Index', index=False)

    print(f'Hang Seng Index closing value ({pd.Timestamp.now().date()}): {closing_value} saved to {excel_file}')
else:
    print('Error: Unable to retrieve the closing value.')

