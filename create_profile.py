import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Your API token
api_token = os.getenv('GO_TOKEN')

# API URL
url = 'https://api.gologin.com/browser'

# Headers
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

# Data for creating the profile (converted from curl)
data = {
    "name": "create _ profile",
    "notes": "",
    "browserType": "chrome",
    "os": "lin",
    "startUrl": "https://whoer.net",
    "googleServicesEnabled": False,
    "lockEnabled": False,
    "debugMode": False,
    "navigator": {
        "userAgent": "random",
        "resolution": "1920x1080",  
        'language': 'en-US,en;q=0.9',
        "platform": "Win32",
        "doNotTrack": None,
        "hardwareConcurrency": 4,
        "deviceMemory": 8,
        "maxTouchPoints": 0
    },
    "geoProxyInfo": {},
    "storage": {
        "local": True,
        "extensions": True,
        "bookmarks": True,
        "history": True,
        "passwords": True,
        "session": True
    },
    "proxyEnabled": True,
    "proxy": {
        "mode": "http",
        "host": "brd.superproxy.io",
        "port": 22225,
        "username": "brd-customer-hl_529771b1-zone-profile_1-ip-5.253.184.92",
        "password": "95ehexayo02x"
    },
    "dns": "8.8.8.8",
    "plugins": {
        "enableVulnerable": True,
        "enableFlash": True
    },
    "timezone": {
        "enabled": True,
        "fillBasedOnIp": True,
        "timezone": ""
    },
    "geolocation": {
        'mode': 'prompt', 
        'enabled': True, 
        'customize': True, 
        'fillBasedOnIp': True, 
        'isCustomCoordinates': False, 
        'latitude': 0, 
        'longitude': 0, 
        'accuracy': 10
    },
    "audioContext": {
            "mode": "noise",
            "noise": 2.79784790072e-08
    },
    'fonts': {
        'enableMasking': True, 
        'enableDomRect': True, 
        'families': ['AIGDT', 'AMGDT']
    },
    "canvas": {
        "mode": "off",
        "noise": 0.2904888
    },
    'mediaDevices': {
        'enableMasking': True, 
        'uid': '338156d30f944cf4bda1de9b613b91e9ef63824dcf3e4af0a8118944f4', 'videoInputs': 0, 
        'audioInputs': 0, 
        'audioOutputs': 0},
    'webRTC': {
        'enable': True, 
        'isEmptyIceList': True, 
        'mode': 'alerted', 
        'enabled': True, 
        'customize': True, 
        'localIpMasking': False, 
        'fillBasedOnIp': True, 
        'publicIp': '', 
        'localIps': []
    }, 
    'webGL': {
        'mode': 'off', 
        'getClientRectsNoise': 9.44704, 
        'noise': 59.328
    },
    'webGpu': {
        'api': {
            'gpu': True, 
            'adapter': True, 
            'compat': True, 
            'device': True, 
            'context': True, 
            'offscreen': True, 
            'twoD': True
        },
    },
    'clientRects': {
        'mode': 'off', 
        'noise': 9.44704
    },
    "webGLMetadata": {
        "mode": "mask",
        "vendor": "string",
        "renderer": "string"
    },
    "webglParams": [],
    "profile": "string",
    "googleClientId": "string",
}

# Convert the data to JSON
json_data = json.dumps(data)

# Send the POST request to create a profile
response = requests.post(url, headers=headers, data=json_data)

# Check if the request was successful
if response.status_code == 200:
    print('Profile created successfully!')
    print('Response:', response.json())
else:
    print(f'Failed to create profile. Status code: {response.status_code}')
    print('Response:', response.text)
    print('Response:', response.json())
