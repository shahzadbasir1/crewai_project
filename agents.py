from crewai import Agent

def create_research_agent(llm):
    return Agent(
        role="Research Specialist",
        goal="Research business trends and market information",
        backstory="Expert business researcher who gathers accurate market intelligence.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_analysis_agent(llm):
    return Agent(
        role="Business Analyst",
        goal="Analyze research findings and identify opportunities",
        backstory="Experienced analyst who evaluates business trends.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_strategy_agent(llm):
    return Agent(
        role="Strategy Consultant",
        goal="Generate actionable recommendations",
        backstory="Executive consultant focused on business growth.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_reviewer_agent(llm):
    return Agent(
        role="Quality Reviewer",
        goal="Review and improve final report",
        backstory="Senior reviewer ensuring quality and completeness.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )