from crewai import Agent


resume_agent = Agent(
    role="ATS Resume Writer",
    goal="Create ATS friendly resumes",
    backstory="Expert resume writer for software jobs.",
    llm="ollama/llama3.2:1b",
    verbose=True
)