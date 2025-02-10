from datetime import datetime

class Reporter:
    def __init__(self):
        self.reports = []

    def generate_report(self, findings):
        """Generates a mission report with timestamps and structured formatting."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = f"""
        ==========================
        🚀 AI Drone Mission Report
        ==========================
        📅 Date & Time: {timestamp}

        🔍 **Inspection Results:**
        {findings}

        ✅ Status: Mission Completed
        ==========================
        """

        self.reports.append(report)
        print(f"Reporter Generated Report:\n{report}")

        return report
