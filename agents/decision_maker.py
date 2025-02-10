from utils import speak
from utils import ask_groq

class DecisionMaker:
    def __init__(self):
        self.decisions = []

    def react_to_event(self, event):
        """AI decides how to respond to mission events & speaks the decision."""
        prompt = f"""
        A drone has reported the following event: {event}.
        Decide the next action:
        - Should we reroute another drone?
        - Should we alert ground personnel?
        - Should we collect more data?
        """

        decision = ask_groq(prompt)
        print(f"DecisionMaker: Decision -> {decision}")

        # Speak the decision
        speak(f"Agent Decision: {decision}")

        self.decisions.append({"event": event, "decision": decision})
        return decision
