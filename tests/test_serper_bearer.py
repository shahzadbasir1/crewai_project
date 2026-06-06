import os
import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://google.serper.dev/search",
    headers={
        "Authorization": f"Bearer {os.getenv('SERPER_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={"q": "OpenAI"}
)

print(response.status_code)
print(response.text)