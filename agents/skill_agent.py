# agents/skill_agent.py
# from openai.agents import Agent

class SkillAgent: # Inherit from OpenAI's Agent base class if applicable
    def __init__(self):
        self.name = "SkillAgent"
        self.current_career_context = None # Context received from previous agent

    def set_context(self, context: dict):
        self.current_career_context = context.get("chosen_career")

    # OpenAI SDK mein tool calls aise na hon. Ye SDK ke apne tareeqe se honge.
    def process_query(self, query: str, tools: dict) -> tuple[str, str]:
        query_lower = query.lower()

        # If context not set, try to infer from query (less ideal but for simple demo)
        if not self.current_career_context:
            possible_careers = ["data science", "software engineering", "cybersecurity", ...]
            for career in possible_careers:
                if career in query_lower:
                    self.current_career_context = career.title()
                    break

        if not self.current_career_context:
            return "Please tell me which career you are interested in for skill information.", self.name

        if "skills for" in query_lower or "tell me about" in query_lower or "roadmap for" in query_lower:
            # Tool invocation for get_career_roadmap
            # OpenAI SDK mein tools aise call nahi hote; SDK runner tools ko resolve karta hai
            # Example: required_skills = self.call_tool("get_career_roadmap", career_field=self.current_career_context)
            required_skills = tools["get_career_roadmap"](self.current_career_context) # Conceptual direct call

            if required_skills:
                response = f"For {self.current_career_context}, key skills include: {', '.join(required_skills)}. Would you like a detailed skill roadmap?"
                # Store skills for the next step (generating roadmap)
                self._current_skills_for_roadmap = required_skills
                return response, self.name # Stay in SkillAgent for next user input
            else:
                return f"I don't have detailed skill information for {self.current_career_context} yet.", self.name
        elif "yes" in query_lower and hasattr(self, '_current_skills_for_roadmap') and self._current_skills_for_roadmap:
            # Tool invocation for generate_skill_roadmap
            # Example: detailed_roadmap = self.call_tool("generate_skill_roadmap", skills=self._current_skills_for_roadmap)
            detailed_roadmap = tools["generate_skill_roadmap"](self._current_skills_for_roadmap) # Conceptual direct call

            response = f"Here's a detailed skill roadmap for {self.current_career_context}:\n{detailed_roadmap}\nNow, let me tell you about some job roles in this field."
            return response, "JobAgent" # Signal handoff to JobAgent
        else:
            return "Please specify if you want skills or a roadmap, or choose another career.", self.name