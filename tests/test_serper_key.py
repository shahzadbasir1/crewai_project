from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("SERPER_API_KEY")

print("REPR:")
print(repr(key))

print("\nFIRST 10:")
print(key[:10])

print("\nLAST 10:")
print(key[-10:])

print("\nLENGTH:")
print(len(key))