# Career Mentor Agent

## Project Description
The Career Mentor Agent is a multi-agent system designed to guide students through career exploration. It recommends career paths based on interests, outlines necessary skills for chosen fields, and provides information on real-world job roles.

## How it Works
This system leverages the OpenAI Agent SDK + Runner to orchestrate interactions between specialized agents and tools.

1.  **Career Exploration**: The `CareerAgent` suggests various career fields based on user input regarding their interests.
2.  **Skill Roadmapping**: Once a career field is selected, the `CareerAgent` hands off to the `SkillAgent`. The `SkillAgent` then uses the `get_career_roadmap()` tool to identify required skills and the `Skill Roadmap Generator` tool to provide a plan for acquiring those skills.
3.  **Job Role Insight**: After providing skill guidance, the `SkillAgent` hands off to the `JobAgent`. The `JobAgent` presents real-world job roles associated with the chosen career field.

## Agents Involved
* **`CareerAgent`**: Responsible for suggesting initial career fields.
* **`SkillAgent`**: Focuses on providing skill-building plans and roadmaps.
* **`JobAgent`**: Shares information about real-world job roles.

## Tools Utilized
* **`get_career_roadmap()`**: A tool used by the `SkillAgent` to show skills needed for a chosen field.
* **`Skill Roadmap Generator`**: A tool used by the `SkillAgent` to generate detailed skill-building plans.

## Handoff Logic
Dynamic handoffs are managed between `CareerAgent`, `SkillAgent`, and `JobAgent`. The `HandoffManager` (or similar logic within the `main.py` and agent classes) orchestrates these transitions based on the user's progress and the information provided.

## Setup and Installation
(Instructions on how to set up your Python environment, install dependencies, and configure the OpenAI Agent SDK)

```bash
# Example:
# git clone <your-repo-link>
# cd career_mentor_agent
# pip install -r requirements.txt
# export OPENAI_API_KEY="your_openai_api_key"