import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPER_API_KEY")

print("KEY FOUND:", bool(api_key))
print("FIRST 10:", api_key[:10])
print("LENGTH:", len(api_key))

response = requests.post(
    "https://google.serper.dev/search",
    headers={
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    },
    json={
        "q": "OpenAI"
    }
)

print("\nSTATUS CODE:")
print(response.status_code)

print("\nHEADERS:")
print(dict(response.headers))

print("\nRESPONSE:")
print(response.text)