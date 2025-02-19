from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('GO_TOKEN')


import requests

# Replace 'YOUR_API_TOKEN' with your actual API token
api_token = token
url = "https://api.gologin.com/browser/fingerprint?os=win&resolution=1680x1050"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

# Print the response JSON
fingerprint_data = response.json()

# Replace with your actual API token and profile ID
profile_id = os.getenv('GO_PROFILE_ID')

url = "https://api.gologin.com/browser/fingerprints"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

data = {
    "browsersIds": [profile_id],
     **fingerprint_data,
}

response = requests.patch(url, headers=headers, json=data)

# Print response status and JSON output
print("Status Code:", response.status_code)
print("Response:", response.json())
