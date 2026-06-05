from crewai import Crew
from crewai import Process

def create_crew(
    agents,
    tasks
):
    return Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )