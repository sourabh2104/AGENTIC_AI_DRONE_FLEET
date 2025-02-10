import streamlit as st
import pandas as pd
import random
import plotly.express as px
import sys
import os
import re
from fpdf import FPDF  # For PDF report generation

# ✅ Fix PyTorch watcher issue
os.environ["STREAMLIT_WATCHDOG"] = "False"
os.environ["PYTORCH_JIT"] = "0"

# ✅ Ensure correct module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from brain.agent_orchestrator import AgentOrchestrator

st.set_page_config(page_title="AI Drone Fleet Dashboard", layout="wide")

orchestrator = AgentOrchestrator()
st.title("🚀 AI Drone Fleet - Mission Control Dashboard")

# ✅ Initialize session state
if "logs" not in st.session_state:
    st.session_state["logs"] = []

if "ai_response" not in st.session_state:
    st.session_state["ai_response"] = {}

# 📌 **Sidebar: Mission Controls**
st.sidebar.header("🛰 Mission Controls")
site_conditions = st.sidebar.text_area("📍 Site Conditions", "Clear skies, normal temperature.")
image_path = st.sidebar.text_input("📷 Sample Image Path", "sample_mining_image.jpg")

if st.sidebar.button("Start Mission"):
    st.session_state["logs"] = []  # Reset logs
    st.session_state["ai_response"] = {}  # Reset response
    result = orchestrator.execute_mission(site_conditions, image_path)  # Get AI mission response
    st.session_state["logs"].append(result)  # Store logs
    st.session_state["ai_response"] = result  # Store AI response
    st.rerun()

# ✅ **📌 Section 1: AI Mission Output (Separate UI)**
st.write("## 📝 Mission Report")

if st.session_state["ai_response"]:
    mission_data = st.session_state["ai_response"]
    
    col1, col2 = st.columns([2, 3])  # Split UI for better readability
    
    with col1:
        st.write("### 📋 Mission Summary")
        st.write(f"**Start Time:** {mission_data.get('start_time', 'N/A')}")
        st.write(f"**End Time:** {mission_data.get('end_time', 'N/A')}")
        st.write(f"**Route:** {mission_data.get('route', 'N/A')}")
    
    with col2:
        st.write("### 🏗 Inspection & Findings")
        st.warning(f"**Inspection Results:** {mission_data.get('inspection_results', 'No data')}")
        st.success(f"**Anomaly Detection:** {mission_data.get('anomaly_detection', 'No data')}")
        st.info(f"**Decision:** {mission_data.get('decision', 'No action')}")

    with st.expander("📜 View Full Mission Plan"):
        st.text_area("Mission Plan:", value=mission_data.get('mission_plan', 'No mission plan available'), height=300)

else:
    st.warning("⚠️ No mission response yet. Start a new mission.")

# ✅ **📌 AI Agent Task Outputs (Table)**
st.write("## 🤖 AI Agent Task Outputs")

if st.session_state["logs"]:
    logs_data = [{"Step": f"Step {i+1}", "Agent Output": log} for i, log in enumerate(st.session_state["logs"])]
    df_logs = pd.DataFrame(logs_data)
    st.dataframe(df_logs, use_container_width=True)
else:
    st.info("📌 No AI Agent outputs available yet.")

# ✅ **📌 Button to Download Mission Report as PDF**
st.write("### 📥 Download Mission Report")

def remove_emojis(text):
    """Removes emojis from the text to prevent encoding errors in PDF."""
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # Transport & map symbols
        u"\U0001F700-\U0001F77F"  # Alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric shapes
        u"\U0001F800-\U0001F8FF"  # Supplemental arrows
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def generate_pdf(content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    if isinstance(content, dict):
        content = "\n".join([f"{key}: {value}" for key, value in content.items()])
    
    content_cleaned = remove_emojis(content)  # ✅ Remove emojis before saving to PDF
    pdf.multi_cell(0, 10, content_cleaned.encode("latin-1", "ignore").decode("latin-1"))  # ✅ Fix encoding error
    pdf_file = "Mission_Report.pdf"
    pdf.output(pdf_file)
    return pdf_file

if st.session_state["ai_response"]:
    pdf_file = generate_pdf(st.session_state["ai_response"])
    with open(pdf_file, "rb") as f:
        st.download_button(label="📄 Download Report (PDF)", data=f, file_name="Mission_Report.pdf", mime="application/pdf")

# ✅ **📌 Section 2: Drone Fleet Status**
st.write("## 🔋 Drone Fleet Overview")
drone_data = [
    {"Drone ID": "Drone-1", "Battery": random.randint(30, 100), "Status": random.choice(["Active", "Returning", "Charging"])},
    {"Drone ID": "Drone-2", "Battery": random.randint(30, 100), "Status": random.choice(["Active", "Returning", "Charging"])},
    {"Drone ID": "Drone-3", "Battery": random.randint(30, 100), "Status": random.choice(["Active", "Returning", "Charging"])},
]
df_drones = pd.DataFrame(drone_data)
st.dataframe(df_drones, use_container_width=True)

# ✅ **📌 Section 3: Drone Battery Levels Visualization**
st.write("## 🔋 Battery Level Monitoring")
fig = px.bar(df_drones, x="Drone ID", y="Battery", color="Status", barmode="group", text="Battery")
st.plotly_chart(fig, use_container_width=True)

# ✅ **📌 Section 4: Mission Alerts**
st.write("## ⚠️ Real-Time Mission Alerts")
alert_messages = [
    "⚠️ Drone-2 detected strong wind gusts! Adjusting flight path.",
    "⚠️ Unexpected obstacle detected! Rerouting drone.",
    "⚠️ Low battery warning for Drone-1! Returning to base.",
    "✅ All drones operating normally."
]
st.warning(random.choice(alert_messages))

# ✅ **📌 Section 5: Mission Performance Over Time**
st.write("## 📊 Mission Success Rate Over Time")
mission_data = {
    "Mission ID": ["Mission-1", "Mission-2", "Mission-3", "Mission-4", "Mission-5"],
    "Success Rate (%)": ["85%", "90%", "78%", "92%", "88%"]
}
df_mission_success = pd.DataFrame(mission_data)
st.dataframe(df_mission_success, use_container_width=True)

