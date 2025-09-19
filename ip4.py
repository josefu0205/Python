import requests

def get_ip_info(ip_address):
    try:
        api_url = f"http://ip-api.com/json/{ip_address}"
        print(f"Fetching data from: {api_url}")
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success":
            print(f"IP: {data['query']}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"ISP: {data.get('isp', 'N/A')}")
            print(f"Country: {data.get('country', 'N/A')}")
            print(f"Region: {data.get('region', 'N/A')}")
            print(f"Timezone: {data.get('timezone', 'N/A')}")
        else:
            print(f"API Error: {data.get('message', 'Unknown error')}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Unable to reach the API")
    except requests.exceptions.Timeout:
        print("Timeout Error: Request took too long")
    except requests.exceptions.JSONDecodeError:
        print("Error: Invalid JSON response from API")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def main():
    while True:
        user_input = input("Enter target IP (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        if not user_input:
            print("Please provide a valid IP address.")
            continue
        get_ip_info(user_input)

if __name__ == "__main__":
    main()