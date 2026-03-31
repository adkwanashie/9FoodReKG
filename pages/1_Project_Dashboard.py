# -----------------------------------------------------
# 1_ProjectDashboard.py — FoodReKG Dashboard
# -----------------------------------------------------
import streamlit as st
import json
from pathlib import Path
import datetime

import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))


# -----------------------------------------------------
# Helper Functions
# -----------------------------------------------------
def slugify(name):
    return name.lower().replace(" ", "_").replace("-", "_")

def get_user_prefix():
    return "agent"  # Replace with user auth system later

# -----------------------------------------------------
# Page Config
# -----------------------------------------------------
st.set_page_config(page_title="Project Dashboard", page_icon="")
st.title("Project Dashboard")
st.markdown("""
Welcome to the **FoodReKG Project Dashboard**.
Here you can monitor project status, view recent activities, and manage configurations.
""")
# -----------------------------------------------------
# Recent Activities Section
# -----------------------------------------------------
st.header("Recent Activities")
st.markdown("""
Here are the latest activities in your FoodReKG project:
""")
recent_activities = [
    {"timestamp": "2026-01-01 10:15", "activity": "Added new regulation: Food Fortification Regulations."},
    {"timestamp": "2026-01-28 14:30", "activity": "Updated clause details for Milk and Dairy Products Regulations."},
    {"timestamp": "2026-01-25 09:45", "activity": "Imported dataset from Kaggle: Nigerian Food Regulations."},
    {"timestamp": "2026-01-20 16:00", "activity": "Generated knowledge graph visualization."},
]
for act in recent_activities:
    st.markdown(f"- **{act['timestamp']}**: {act['activity']}")
st.markdown("⚙️ Recent Activities management feature coming soon")

# -----------------------------------------------------
# Project Status Section
st.header("Project Status")
st.markdown("""
Current status of key project components:
""")
project_status = {
    "Knowledge Graph": "✅ Up to date",
    "Data Imports": "✅ Last import on 2026-01-28",
    "Visualizations": "✅ Last generated on 2026-01-20",
    "Model Evaluations": "⚠️ Pending new data",
}   
for component, status in project_status.items():
    st.markdown(f"- **{component}**: {status}")
st.markdown("⚙️ Project management feature coming soon.")

# -----------------------------------------------------
# Configuration Management Section            

st.header("Manage Configurations")
st.markdown("""
You can manage project configurations here.
""")
st.markdown("⚙️ Configuration management features coming soon.")