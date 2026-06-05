from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

print("FIRST 15:", key[:15])
print("LAST 15 :", key[-15:])
print("LENGTH  :", len(key))