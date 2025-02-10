import streamlit as st
import pydeck as pdk
import time
import random

st.title("🌩 AI Drone Fleet - Extreme Weather Simulation")

# Simulated Weather Conditions
weather_conditions = ["Clear Skies", "High Winds", "Thunderstorm", "Extreme Heat", "Snowstorm"]
current_weather = random.choice(weather_conditions)

st.write(f"### ⛅ Current Weather: {current_weather}")

# Adjust Drone Behavior Based on Weather
battery_drain = {
    "Clear Skies": 1,
    "High Winds": 5,
    "Thunderstorm": 10,
    "Extreme Heat": 7,
    "Snowstorm": 8
}

# Define GPS locations
WAYPOINTS = [
    {"lat": -24.6272, "lon": 25.9239, "alt": 120, "desc": "Mining Site A"},
    {"lat": -24.6290, "lon": 25.9280, "alt": 100, "desc": "Mining Site B"},
    {"lat": -24.6315, "lon": 25.9325, "alt": 110, "desc": "Refinery Area"},
]

drones = [{"lat": wp["lat"], "lon": wp["lon"], "alt": wp["alt"], "id": f"Drone-{i+1}", "desc": wp["desc"], "battery": 100} for i, wp in enumerate(WAYPOINTS)]

def update_positions():
    """Simulate drone movement and weather impact."""
    for drone in drones:
        drone["lat"] += random.uniform(-0.0002, 0.0002)
        drone["lon"] += random.uniform(-0.0002, 0.0002)
        drone["battery"] -= battery_drain[current_weather]
    return drones

# 3D Visualization
st.write("### 🛰 Drone Fleet Simulation")
layer = pdk.Layer(
    "ScatterplotLayer",
    update_positions(),
    get_position=["lon", "lat"],
    get_color=[255, 0, 0, 160],
    get_radius=50,
    pickable=True,
)

view_state = pdk.ViewState(latitude=-24.6272, longitude=25.9239, zoom=15, pitch=50)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{id} - {desc}"}))

# Simulate movement
for _ in range(10):
    time.sleep(1)
    drones = update_positions()
    st.rerun()
