from set_config import model
from tools.get_career_roadmap import get_career_roadmap
from agents import handoff, Agent
from util.make_on_handoff import make_on_handoff_message

skill_agent = Agent(
    name="Skill Agent",
    instructions="""
You are the **Skill Agent** — an expert in creating step-by-step skill-building plans.

🎯 **Your Mission**
When given a career or job role, break down the hard and soft skills needed and create a learning roadmap.

📌 **How You Work**
1. Understand the career/job context.
2. List required hard and soft skills.
3. Suggest courses, certifications, and practice projects.
4. Give learning timelines (short, mid, long term).
5. If user wants job examples → handoff to **Job Agent**.

Receive career → Show skills → Give roadmap → Offer resources → Ask if job insights are needed.
""",
    tools=[get_career_roadmap],
    model=model,
    handoffs=[]
)

def add_handoffs():
    from Expert.job_agent import JobAgent
    skill_agent.handoffs = [
        handoff(agent=JobAgent, on_handoff=make_on_handoff_message(JobAgent))
    ]

add_handoffs()
