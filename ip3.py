import urllib.request
import json

def query_ip(ip):
    try:
        # Use the modern urllib.request alias (urllib2 is outdated in Python 3)
        url = f"http://ip-api.com/json/{ip}"
        print(f"Querying URL: {url}")  # Debug: Show the URL being queried
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')  # Decode bytes to string
        print(f"Raw response: {data}")  # Debug: Print raw API response
        values = json.loads(data)
        
        # Check if the API returned a success status
        if values.get("status") == "success":
            print("IP: " + values["query"])
            print("City: " + values.get("city", "N/A"))
            print("ISP: " + values.get("isp", "N/A"))
            print("Country: " + values.get("country", "N/A"))
            print("Region: " + values.get("region", "N/A"))
            print("Timezone: " + values.get("timezone", "N/A"))
        else:
            print(f"API Error: {values.get('message', 'Unknown error')}")
            
    except urllib.request.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.request.URLError as e:
        print(f"URL Error: {e.reason}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON response from API")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

while True:
    ip = input("What is your target IP (or 'exit' to quit): ").strip()
    if ip.lower() == 'exit':
        break
    if not ip:
        print("Please enter a valid IP address.")
        continue
    query_ip(ip)