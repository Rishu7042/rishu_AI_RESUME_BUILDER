from crewai import Task

def resume_task(agent, profile, job):
    return Task(
        description=f"Create ATS resume. Student Profile: {profile}. Target Job: {job}",
        agent=agent,
        expected_output="Markdown formatted resume"
    )

def ats_task(agent, job):
    return Task(
        description=f"Review the resume against Job: {job}",
        agent=agent,
        expected_output="ATS Score"
    )

def improvement_task(agent, feedback):
    return Task(
        description=f"Improve the resume based on ATS feedback: {feedback}",
        agent=agent,
        expected_output="Improved ATS-friendly resume"
    )