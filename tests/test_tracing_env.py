import os
from dotenv import load_dotenv

load_dotenv()

print(
    os.getenv("CREWAI_TRACING_ENABLED")
)