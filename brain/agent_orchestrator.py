from agents.commander import Commander
from agents.navigator import Navigator
from agents.inspector import Inspector
from agents.decision_maker import DecisionMaker
from agents.anomaly_detector import AnomalyDetector  # New Import
from datetime import datetime

class AgentOrchestrator:
    def __init__(self):
        self.commander = Commander()
        self.navigator = Navigator()
        self.inspector = Inspector()
        self.decision_maker = DecisionMaker()
        self.anomaly_detector = AnomalyDetector()  # Initialize Anomaly Detector

    def execute_mission(self, site_conditions, image_path):
        """Runs a full AI-driven drone mission and returns structured results."""
        mission_start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"🚀 Mission Started at {mission_start_time}")

        # Step 1: Generate mission plan
        mission_plan = self.commander.create_mission(site_conditions)

        # Step 2: Plan optimal route
        route = self.navigator.plan_route(mission_plan)

        # Step 3: Perform inspections
        inspection_alert = self.inspector.analyze_images(image_path)

        # Step 4: Detect anomalies and reroute if needed
        anomaly_alert = self.anomaly_detector.detect_anomalies(image_path)

        # Step 5: AI reacts to findings
        decision = "No action needed"
        if "⚠️" in anomaly_alert:
            decision = self.decision_maker.react_to_event(anomaly_alert)

        mission_end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"✅ Mission Completed at {mission_end_time}")

        # Return structured mission report
        return {
            "start_time": mission_start_time,
            "end_time": mission_end_time,
            "mission_plan": mission_plan,
            "route": route,
            "inspection_results": inspection_alert,
            "anomaly_detection": anomaly_alert,
            "decision": decision,
        }
