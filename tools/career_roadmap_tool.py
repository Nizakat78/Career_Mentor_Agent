# tools/career_roadmap_tool.py
# from openai.agents import tool # Hypothetical decorator

# @tool
def get_career_roadmap(career_field: str) -> list[str]:
    """
    Returns a list of core skills required for a given career field.
    """
    career_field_lower = career_field.lower()
    if "data science" in career_field_lower:
        return ["Python", "R", "Statistics", "Machine Learning", "Data Visualization", "SQL"]
    elif "software engineering" in career_field_lower:
        return ["Python", "Java", "C++", "Data Structures", "Algorithms", "Web Frameworks", "Git"]
    elif "cybersecurity" in career_field_lower:
        return ["Network Security", "Cryptography", "Penetration Testing", "Security Auditing", "Linux", "Compliance"]
    else:
        return []