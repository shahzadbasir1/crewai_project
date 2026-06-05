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
        Research the following topic:

        {topic}

        Gather:
        - Current trends
        - Opportunities
        - Risks
        - Market observations
        """,
        expected_output="Research report",
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
        expected_output="Business analysis",
        agent=analysis_agent
    )

    strategy_task = Task(
        description="""
        Generate executive recommendations
        based on the analysis.
        """,
        expected_output="Strategic recommendations",
        agent=strategy_agent
    )

    review_task = Task(
        description="""
        Review the complete report.

        Improve:
        - Clarity
        - Accuracy
        - Structure
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