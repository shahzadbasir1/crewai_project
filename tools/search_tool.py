import os
import requests

from crewai.tools import BaseTool

from fallback.fallback_handler import FallbackHandler

from monitoring.trace_helper import (
    start_trace,
    end_trace
)

from tools.tavily_search_tool import TavilySearchTool


class SerperSearchTool(BaseTool):
    name: str = "Serper Search Tool"
    description: str = (
        "Searches the internet using Google Serper "
        "with Tavily fallback."
    )

    def _run(self, query: str) -> str:

        trace = start_trace(
            "Search Tool",
            {
                "query": query
            }
        )

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

                    title = item.get(
                        "title",
                        "No Title"
                    )

                    link = item.get(
                        "link",
                        "No Link"
                    )

                    snippet = item.get(
                        "snippet",
                        ""
                    )

                    results.append(
                        f"Title: {title}\n"
                        f"Link: {link}\n"
                        f"Snippet: {snippet}\n"
                    )

                if results:

                    result = "\n".join(results)

                    end_trace(
                        trace,
                        result
                    )

                    return result

            print(
                f"Serper failed "
                f"({response.status_code})"
            )

        except Exception as e:

            print(
                f"Serper exception: "
                f"{str(e)}"
            )

        # ----------------------------------
        # Tavily Fallback
        # ----------------------------------

        print(
            "Trying Tavily fallback..."
        )

        try:

            tavily_result = (
                TavilySearchTool()
                ._run(query)
            )

            if (
                tavily_result
                and
                "Error" not in tavily_result
                and
                "not configured"
                not in tavily_result
            ):

                end_trace(
                    trace,
                    tavily_result
                )

                return tavily_result

        except Exception:

            pass

        # ----------------------------------
        # Final Fallback
        # ----------------------------------

        result = (
            FallbackHandler
            .handle_search_failure(query)
        )

        end_trace(
            trace,
            result
        )

        return result