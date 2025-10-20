# This script fetches domain information from a public API and displays it.

# 'requests' allows us to send HTTP requests to APIs and receive data back.
import requests

# 'json' helps format the response from the API into a readable structure.
import json

# Replace 'YOUR_API_KEY' with your actual API key from WhoisXML API (or other services).
API_KEY = "YOUR_API_KEY"

# The base URL for the domain lookup API.
# This URL will be combined with the domain you want to look up.
BASE_URL = "https://www.whoisxmlapi.com/whoisserver/WhoisService"

# Using input() lets us make the script interactive.
domain_name = input("Enter a domain name (e.g. example.com): ")

# The API expects parameters such as the domain name and API key.
# These parameters will be sent as part of the URL.
params = {
    "apiKey": API_KEY,
    "domainName": domain_name,
    "outputFormat": "JSON" 
}

# requests.get() sends a request to the API with the URL and parameters we built.
response = requests.get(BASE_URL, params=params)

# If the status code is 200, it means the request was successful.
if response.status_code == 200:
    # Parse the response content as JSON
    data = response.json()

    # json.dumps() lets us convert Python dictionaries to nicely formatted text.
    print("\n✅ Domain Information:\n")
    print(json.dumps(data, indent=4))

else:
    # If the status code is not 200, something went wrong.
    print(f"❌ Failed to fetch domain info. Status code: {response.status_code}")
