import random

class Navigator:
    def __init__(self):
        self.routes = []

    def plan_route(self, mission_details):
        """AI generates an optimized flight path for drones."""
        waypoints = [
            {"lat": -24.6272, "lon": 25.9239, "alt": 120},
            {"lat": -24.6290, "lon": 25.9280, "alt": 100},
            {"lat": -24.6315, "lon": 25.9325, "alt": 110}
        ]

        adjusted_route = [wp for wp in waypoints]
        print(f"Navigator: Planned Route -> {adjusted_route}")

        self.routes.append(adjusted_route)
        return adjusted_route
