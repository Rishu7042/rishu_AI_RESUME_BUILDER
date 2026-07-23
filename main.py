from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crew import run_crew

app = FastAPI(title="AI Resume Builder API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Resume Builder API Running"}


@app.post("/generate-resume")
def generate_resume():

    with open("input/student_profile.txt", "r", encoding="utf-8") as f:
        profile = f.read()

    with open("input/job_description.txt", "r", encoding="utf-8") as f:
        job_desc = f.read()

    result = run_crew(profile, job_desc)

    return {
        "result": str(result)
    }