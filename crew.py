from crewai import Agent, Task, Crew


resume_agent = Agent(
    role="ATS Resume Writer",
    goal="Create ATS-friendly resumes",
    backstory="You are an expert ATS resume writer who creates professional resumes for software jobs.",
    llm="ollama/llama3.2:1b",
    verbose=True
)


def run_crew(profile, job_desc):

    resume_task = Task(
        description=f"""
        Create an ATS-friendly resume.

        Student Profile:
        {profile}

        Target Job:
        {job_desc}

        Include:
        - Professional Summary
        - Skills
        - Projects
        - Education
        - Career Objective
        """,

        agent=resume_agent,

        expected_output="A professional ATS-friendly resume in Markdown format"
    )


    crew = Crew(
        agents=[resume_agent],
        tasks=[resume_task],
        verbose=True
    )


    result = crew.kickoff()

    return result