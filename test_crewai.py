from crewai import Agent

agent = Agent(
    role="Tester",
    goal="Verify installation",
    backstory="Simple test agent",
    verbose=True
)

print("CrewAI Agent Created Successfully")