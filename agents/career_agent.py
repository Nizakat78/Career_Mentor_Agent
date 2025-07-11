# agents/career_agent.py
# from openai.agents import Agent # Hypothetical SDK base class

class CareerAgent: # Inherit from OpenAI's Agent base class if applicable
    def __init__(self):
        self.name = "CareerAgent"
        self.interests_keywords = {
            "solving problems": ["Software Engineering", "Data Science", "Cybersecurity"],
            "creativity": ["Graphic Design", "Content Creator", "Marketing"],
            "helping people": ["Healthcare", "Education", "Social Work"],
            "data": ["Data Science", "Business Analyst", "Statistician"],
            "art": ["Graphic Design", "Content Creator"], # Added for broader interest
            "design": ["Graphic Design", "Content Creator"], # Added for broader interest
            "math": ["Data Science", "Statistician", "Software Engineering"], # Added for broader interest
            "logic": ["Software Engineering", "Cybersecurity"] # Added for broader interest
        }
        self.suggested_careers_from_last_turn = [] # To store what was suggested last
        self.chosen_career = None

    def process_query(self, query: str, tools: dict) -> tuple[str, str]:
        query_lower = query.lower()
        found_keywords = []
        current_suggestions = []

        # Step 1: Check for new interests in the query
        for keyword, careers in self.interests_keywords.items():
            if keyword in query_lower:
                found_keywords.append(keyword)
                current_suggestions.extend(careers)

        if found_keywords:
            unique_suggestions = list(set(current_suggestions))
            # Store these suggestions for the next turn, if the user picks one
            self.suggested_careers_from_last_turn = unique_suggestions
            response = f"Based on your interests ({', '.join(found_keywords)}), you might consider fields like {', '.join(unique_suggestions)}. Which one interests you most?"
            return response, self.name # Stay in CareerAgent, waiting for user to choose from suggestions
        else:
            # Step 2: If no new interests found, check if the user is choosing from previous suggestions
            # This handles the case where the agent has already suggested careers and is waiting for a choice.
            if self.suggested_careers_from_last_turn:
                for career in self.suggested_careers_from_last_turn:
                    # Check if any of the previously suggested careers are in the current query
                    if career.lower() in query_lower:
                        self.chosen_career = career
                        # Clear previous suggestions once a choice is made to avoid re-matching
                        self.suggested_careers_from_last_turn = []
                        response = f"Great! Let's explore {career}. Handoff to SkillAgent initiated..."
                        return response, "SkillAgent" # Signal handoff to SkillAgent
            # Fallback if no interests found and no valid choice made
            return "I'm not sure about that. Could you tell me more about your interests?", self.name