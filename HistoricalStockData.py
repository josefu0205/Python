import requests
import pandas

API_KEY = 'API_KEYd0IUET6VOROX3N6P7K2PX64MYA34JC41' # get your free API key from https://moon.finage.co.uk/register?subscribe=API00

symbol = input('Symbol: ')
start_date = input('Start date: ')
end_date = input('End date: ')

response = requests.get('https://api.finage.co.uk/agg/stock/'+ symbol +'/1/day/'+ start_date +'/'+ end_date +'?apikey=' + API_KEY)


print('Total Result(s): ' + str(response.json()['totalResults']))

json_list = []

for item in response.json()['results']:

    json_element = {
        'open': item['o'],
        'high': item['h'],
        'low': item['l'],
        'close': item['c'],
        'volume': item['v'],
        'date': pandas.to_datetime(item['t'], unit='ms')
    }
    json_list.append(json_element)

df = pandas.DataFrame(json_list).to_excel(symbol+".xlsx", index=False)