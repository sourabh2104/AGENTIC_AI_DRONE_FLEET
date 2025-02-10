from utils import ask_groq

class Commander:
    def __init__(self):
        self.missions = []

    def create_mission(self, site_conditions):
        """Generates an autonomous mission plan using LLM."""
        prompt = f"""
        You are an AI Drone Commander.
        Given the current site conditions: {site_conditions},
        Generate an optimized mission plan including:
        - Flight path strategy
        - Inspection priorities
        - Potential risks and mitigations
        """

        mission_plan = ask_groq(prompt)
        print(f"Commander: Mission Plan Created -> {mission_plan}")

        self.missions.append(mission_plan)
        return mission_plan
