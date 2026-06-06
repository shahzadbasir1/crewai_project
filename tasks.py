from crewai import Task


def create_tasks(
    research_agent,
    analysis_agent,
    strategy_agent,
    reviewer_agent,
    topic
):

    research_task = Task(
        description=f"""
        Research the topic:

        {topic}

        Use the Search Tool to gather:

        - Current trends
        - Industry developments
        - Market opportunities
        - Risks

        Produce a detailed research report.
        """,
        expected_output="Detailed research report",
        agent=research_agent
    )

    analysis_task = Task(
        description="""
        Analyze the research findings.

        Identify:

        - Key trends
        - Business opportunities
        - Risks
        - Competitive considerations
        """,
        expected_output="Business analysis report",
        agent=analysis_agent
    )

    strategy_task = Task(
        description="""
        Generate executive recommendations.

        Use the Trend Score Tool to evaluate
        the business relevance of the topic.

        Produce strategic recommendations.
        """,
        expected_output="Strategic recommendations",
        agent=strategy_agent
    )

    review_task = Task(
        description="""
        Review the entire report.

        Improve:

        - Clarity
        - Accuracy
        - Structure
        - Executive readability
        """,
        expected_output="Final reviewed report",
        agent=reviewer_agent
    )

    return [
        research_task,
        analysis_task,
        strategy_task,
        review_task
    ]