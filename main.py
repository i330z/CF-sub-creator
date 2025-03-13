import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
ZONE_ID = os.getenv("ZONE_ID")
IP_ADDRESS = os.getenv("IP_ADDRESS")
PROXIED = True

SUBDOMAIN = input("Enter the subdomain: ")

url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


data = {
    "type": "A",
    "name": SUBDOMAIN,
    "content": IP_ADDRESS,
    "proxied": PROXIED,
    "ttl": 1    
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print(f"Successfully created DNS record for {SUBDOMAIN}")
else:
    print(f"Failed to create DNS record for {SUBDOMAIN}")
    print(response.json())



