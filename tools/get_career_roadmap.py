from agents import function_tool, RunContextWrapper, AsyncOpenAI
from typing import TypedDict
import os
from dotenv import load_dotenv, find_dotenv
from set_config import model

# Load API key
load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# ✅ Strict input schema
class CareerRoadmapInput(TypedDict):
    career_field: str

# ✅ Strict output schema
class CareerRoadmapOutput(TypedDict):
    roadmap: str

@function_tool
async def get_career_roadmap(wrapper: RunContextWrapper, input: CareerRoadmapInput) -> CareerRoadmapOutput:
    """
    Fetches a detailed career roadmap for the given field.
    """
    career_field = input["career_field"].strip()
    prompt = (
        f"[TOOL: get_career_roadmap] Provide a detailed career roadmap for {career_field}.\n"
        "Include beginner, intermediate, and advanced stages.\n"
        "Clearly format the response with bullet points for each stage."
    )

    response = await client.chat.completions.create(
        model=getattr(model, "model_id", "gemini-2.5-flash"),
        messages=[{"role": "user", "content": prompt}],
    )

    content = (
        getattr(response.choices[0].message, "content", None)
        or getattr(response.choices[0], "text", None)
        or ""
    )

    return {"roadmap": f"[TOOL: get_career_roadmap]\n{content.strip()}"}
