import os
import requests

from crewai.tools import BaseTool

from fallback.fallback_handler import FallbackHandler
from tools.tavily_search_tool import TavilySearchTool


class SerperSearchTool(BaseTool):
    name: str = "Serper Search Tool"
    description: str = (
        "Primary web search provider using Serper"
    )

    def _run(self, query: str) -> str:

        api_key = os.getenv("SERPER_API_KEY")

        try:

            response = requests.post(
                "https://google.serper.dev/search",
                headers={
                    "X-API-KEY": api_key,
                    "Content-Type": "application/json"
                },
                json={
                    "q": query
                },
                timeout=10
            )

            if response.status_code == 200:

                data = response.json()

                results = []

                for item in data.get(
                    "organic",
                    []
                )[:5]:

                    results.append(
                        f"Title: {item.get('title')}\n"
                        f"Link: {item.get('link')}\n"
                    )

                if results:
                    return "\n".join(results)

            print(
                f"Serper failed "
                f"({response.status_code})"
            )

        except Exception as e:

            print(
                f"Serper exception: {str(e)}"
            )

        print("Trying Tavily fallback...")

        tavily_results = (
            TavilySearchTool()
            ._run(query)
        )

        if (
            tavily_results
            and
            "Error" not in tavily_results
            and
            "not configured" not in tavily_results
        ):
            return tavily_results

        return (
            FallbackHandler
            .handle_search_failure(query)
        )