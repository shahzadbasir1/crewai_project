import os

from tavily import TavilyClient
from crewai.tools import BaseTool


class TavilySearchTool(BaseTool):
    name: str = "Tavily Search Tool"
    description: str = (
        "Backup search provider using Tavily."
    )

    def _run(self, query: str) -> str:

        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:
            return "TAVILY_API_KEY not configured"

        try:

            client = TavilyClient(api_key=api_key)

            response = client.search(
                query=query,
                max_results=5
            )

            results = []

            for item in response.get("results", []):

                results.append(
                    f"Title: {item.get('title')}\n"
                    f"URL: {item.get('url')}\n"
                    f"Content: {item.get('content')}\n"
                )

            return "\n".join(results)

        except Exception as e:

            return f"Tavily Error: {str(e)}"