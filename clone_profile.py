from dotenv import load_dotenv
import os
import requests

load_dotenv()


# Set up your variables
profile_id = os.getenv('GO_PROFILE_ID')  # Replace with your profile ID
api_token = os.getenv('GO_TOKEN')

# Define the URL
url = f"https://api.gologin.com/browser/{profile_id}/clone"

# Set up the headers
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers)

# Check the response status and handle it
if response.status_code == 200:
    print("Profile cloned successfully!")
    print("Response JSON:", response.json())  # Prints the JSON response content
else:
    print(f"Failed to clone profile. Status code: {response.status_code}")
    print("Error response:", response.text)  # Prints error message if any