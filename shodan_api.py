import os
import shodan

# Get the API key from environment variable
API_KEY = os.getenv("SHODAN_API_KEY")

if not API_KEY:
    raise ValueError("Shodan API key not found. Please set the SHODAN_API_KEY environment variable.")

api = shodan.Shodan(API_KEY)

def get_shodan_info(ip):
    try:
        # Query Shodan for information about the target IP
        result = api.host(ip)
        print(f"[+] Shodan Info for {ip}: {result}")
        return result
    except shodan.APIError as e:
        print(f"[-] Shodan API Error: {e}")
        return None

