import os
import requests
from crewai.tools import BaseTool


class SerperSearchTool(BaseTool):
    name: str = "Serper Search Tool"
    description: str = "Search the internet using Google Serper"

    def _run(self, query: str) -> str:

        api_key = os.getenv("SERPER_API_KEY")

        response = requests.post(
            "https://google.serper.dev/search",
            headers={
                "X-API-KEY": api_key,
                "Content-Type": "application/json"
            },
            json={
                "q": query
            }
        )

        data = response.json()

        results = []

        for item in data.get("organic", [])[:5]:
            results.append(
                f"{item['title']} - {item['link']}"
            )

        return "\n".join(results)