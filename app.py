import os

from dotenv import load_dotenv

from crewai import LLM

from agents import (
    create_research_agent,
    create_analysis_agent,
    create_strategy_agent,
    create_reviewer_agent
)

from tasks import create_tasks
from crew import create_crew

load_dotenv()

def main():

    topic = input(
        "\nEnter topic to analyze: "
    )

    llm = LLM(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    research_agent = create_research_agent(llm)

    analysis_agent = create_analysis_agent(llm)

    strategy_agent = create_strategy_agent(llm)

    reviewer_agent = create_reviewer_agent(llm)

    tasks = create_tasks(
        research_agent,
        analysis_agent,
        strategy_agent,
        reviewer_agent,
        topic
    )

    crew = create_crew(
        [
            research_agent,
            analysis_agent,
            strategy_agent,
            reviewer_agent
        ],
        tasks
    )

    result = crew.kickoff()

    print("\n")
    print("=" * 80)
    print("FINAL REPORT")
    print("=" * 80)
    print(result)

if __name__ == "__main__":
    main()