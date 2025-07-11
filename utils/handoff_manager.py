# utils/handoff_manager.py

class HandoffManager:
    """
    Conceptual class to manage the handoff logic between agents.
    In a real OpenAI Agent SDK implementation, this might be handled internally
    by the SDK's runner or by defining specific "tools" for handoff.
    """
    def __init__(self):
        self.current_agent_name = "CareerAgent" # Initial agent

    def set_current_agent(self, agent_name: str):
        """Sets the name of the currently active agent."""
        self.current_agent_name = agent_name

    def get_current_agent(self) -> str:
        """Returns the name of the currently active agent."""
        return self.current_agent_name

    def decide_next_agent(self, current_agent_response: str, user_input: str) -> str:
        """
        This method would contain the logic to determine which agent should take over.
        This is a highly simplified example.
        """
        if "tell me about" in user_input.lower() and self.current_agent_name == "CareerAgent":
            return "SkillAgent"
        elif "skill roadmap" in current_agent_response.lower() and "yes" in user_input.lower() and self.current_agent_name == "SkillAgent":
            return "SkillAgent" # Stay in SkillAgent to generate roadmap
        elif "job roles" in current_agent_response.lower() and self.current_agent_name == "SkillAgent":
            return "JobAgent"
        elif "explore another career" in current_agent_response.lower() and "yes" in user_input.lower() and self.current_agent_name == "JobAgent":
            return "CareerAgent"
        # Default to current agent or a fallback
        return self.current_agent_name