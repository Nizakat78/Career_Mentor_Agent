from set_config import model
from agents import Agent
from tools.get_career_roadmap import get_career_roadmap
from util.make_on_handoff import make_on_handoff_message
from agents import handoff

JobAgent = Agent(
    name="Job Agent",
    instructions="""
You are the **Job Agent** — a specialist in providing real-world job role insights.

🎯 **Your Mission**
When given a career, show at least 3 current job titles with:
- Role description
- Required skills/certifications
- Salary range
- Companies/industries hiring
- Demand trends


Receive career → Show jobs → Share market info → Ask if skills needed → Handoff to SkillAgent.
""",
    tools=[get_career_roadmap],
    model=model,
    handoffs=[]
)

def add_handoffs():
    from Expert.skill_agent import skill_agent
    JobAgent.handoffs = [
        handoff(agent=skill_agent, on_handoff=make_on_handoff_message(skill_agent))
    ]

add_handoffs()
