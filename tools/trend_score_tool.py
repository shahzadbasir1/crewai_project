from crewai.tools import BaseTool


class TrendScoreTool(BaseTool):
    name: str = "Trend Score Tool"
    description: str = (
        "Calculates a trend score "
        "for business topics."
    )

    def _run(self, topic: str) -> str:

        score = 50

        keywords = [
            "ai",
            "automation",
            "cloud",
            "analytics",
            "data",
            "machine learning",
            "llm",
            "agent"
        ]

        topic = topic.lower()

        for keyword in keywords:

            if keyword in topic:
                score += 7

        score = min(score, 100)

        return (
            f"Topic: {topic}\n"
            f"Trend Score: {score}/100"
        )