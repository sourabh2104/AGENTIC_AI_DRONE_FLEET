🚀 Application Workflow (Step-by-Step)
🛰 Step 1: Start the Drone Mission
User enters site conditions and uploads site images via the Streamlit dashboard.
AI Commander Agent generates a mission plan based on conditions.
🛣 Step 2: AI Navigator Plans the Route
AI optimizes the flight path based on the site structure.
The route is displayed visually on a 3D map.
🔍 Step 3: Inspector Analyzes Images
Drones capture aerial images and videos.
AI-driven YOLOv8 model scans for anomalies (cracks, leaks, obstacles).
📡 Step 4: Communicator Sends Live Updates
Live mission logs appear in the dashboard.
Alerts are sent if an anomaly is detected.
🤖 Step 5: Decision Maker Takes Action
AI suggests rerouting, reinspection, or alerting human operators.
If no action is required, the mission continues.
📜 Step 6: Generate Mission Report
AI generates a detailed PDF mission report.
Report includes route, findings, and success rate.
📊 Step 7: Visualization & Analytics
Live drone status table (battery, active/returning status).
Mission success rate trends.
AI agent performance tracking.

⚙️ How to Run the Application
📌 1. Clone the Repository
```bash
git clone https://github.com/sourabh2104/AI-Drone-Fleet
cd AI-Drone-Fleet
```
📌 2. Set Up Virtual Environment
```bash
python3 -m venv m_drones
source m_drones/bin/activate  # On Windows use `m_drones\Scripts\activate`
```

📌 3. Install Dependencies
```bash 
pip install -r requirements.txt
```
📌 4. Set Up API Keys & Environment
Create a .env file and add:
--GROQ_API_KEY=your_api_key_here

📌 5. Run the Application
```bash
streamlit run dashboard/dashboard.py
```
Open http://localhost:8501 in your browser.



📈 Features & Functionality
✅ 1. AI-Powered Drone Mission Control
Automatically assigns tasks to AI agents.
Plans optimized routes and adjusts for obstacles.
✅ 2. Real-Time Drone Fleet Tracking
Displays current GPS location of drones on a 3D map.
Monitors battery status & mission progress.
✅ 3. AI-Based Image & Anomaly Detection
Uses YOLOv8 AI model to analyze drone-captured images.
Detects cracks, leaks, obstacles, or other hazards.
✅ 4. AI-Driven Decision Making
LLM-based Decision Maker Agent suggests reroutes or safety measures.
Live alerts notify operators of any risks.
✅ 5. Automated Reporting System
Generates professional-grade PDF reports.
Stores mission logs and success rates.
🏢 How to Scale This for Enterprises
💼 1. Multi-Drone Integration
Support for fleet-wide coordination.
Enable swarm intelligence for large-scale coverage.
🌍 2. Cloud Integration
Store mission logs in MongoDB for long-term data tracking.
Allow access to mission reports from anywhere.
📡 3. AI-Enhanced Anomaly Detection
Train a custom AI model to detect industry-specific issues.
Example: Detect pipeline leaks in oil industries.
🛠 4. Hardware Integration
Connect directly with drone APIs (DJI, Parrot, PX4)
Enable autonomous drone control.
🚀 5. Deploy as a SaaS Product
Offer AI Drone Fleet Management as a Service.
Industry clients can subscribe to manage their drones via a web platform.
🎯 Future Enhancements
🚀 Live Drone Video Streaming – Real-time surveillance via web UI.
📡 5G/IoT Connectivity – Seamless communication with drones.
🧠 Advanced AI Training – Self-learning AI agents for better decision-making.
☁️ Cloud-Based Data Storage – Store and retrieve past missions remotely.

📝 Conclusion
The AI Drone Fleet Management System transforms manual drone operations into an AI-driven, efficient, and scalable system. Whether for infrastructure monitoring, security, or disaster management, this application ensures optimized drone performance with minimal human intervention.

💡 🚀 Ready to take AI-powered drone fleet management to the next level? Let’s build the future!



📩 Contact & Contribution
👨‍💻 Developed by Sourabh
🌍 GitHub:
https://github.com/sourabh2104

📧 Email:
sourabhyadav1256@gmail.com

Feel free to contribute to this project via Pull Requests or Issues! 🎯

🔥 If you found this project useful, give it a ⭐ on GitHub!

Let me know if you need any modifications! 🚀







