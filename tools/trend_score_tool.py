from crewai.tools import BaseTool

from fallback.fallback_handler import FallbackHandler

from monitoring.trace_helper import (
    start_trace,
    end_trace
)


class TrendScoreTool(BaseTool):
    name: str = "Trend Score Tool"
    description: str = (
        "Generates a trend score from 1 to 100 "
        "for a given topic."
    )

    def _run(self, topic: str) -> str:

        trace = start_trace(
            "Trend Score Tool",
            {
                "topic": topic
            }
        )

        try:

            score = min(
                100,
                len(topic) * 3 + 10
            )

            result = (
                f"Topic: {topic}\n"
                f"Trend Score: {score}/100"
            )

            end_trace(
                trace,
                result
            )

            return result

        except Exception as e:

            result = (
                FallbackHandler
                .handle_llm_failure(
                    str(e)
                )
            )

            end_trace(
                trace,
                result
            )

            return result