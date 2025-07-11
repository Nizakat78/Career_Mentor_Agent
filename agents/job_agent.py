# agents/job_agent.py
# from openai.agents import Agent

class JobAgent: # Inherit from OpenAI's Agent base class if applicable
    def __init__(self):
        self.name = "JobAgent"
        self.current_career_context = None # Context received from previous agent
        self.job_roles_data = {
            "Data Science": ["Data Scientist", "Machine Learning Engineer", "Business Intelligence Analyst"],
            "Software Engineering": ["Front-end Developer", "Back-end Developer", "DevOps Engineer"],
            "Cybersecurity": ["Security Analyst", "Ethical Hacker", "Security Consultant"],
        }

    def set_context(self, context: dict):
        self.current_career_context = context.get("chosen_career")

    def process_query(self, query: str, tools: dict) -> tuple[str, str]:
        query_lower = query.lower()

        # If context not set, try to infer from query (less ideal)
        if not self.current_career_context:
            possible_careers = ["data science", "software engineering", "cybersecurity", ...]
            for career in possible_careers:
                if career in query_lower:
                    self.current_career_context = career.title()
                    break

        if self.current_career_context:
            roles = self.job_roles_data.get(self.current_career_context, ["No specific roles found."])
            response = f"Here are some common job roles in {self.current_career_context}: {', '.join(roles)}.\nWould you like to explore another career, or are you done?"
            return response, "CareerAgent" # Signal handoff back to CareerAgent for new exploration
        else:
            return "I can share job roles if you tell me which career field you are interested in.", self.name