
import streamlit as st
from theme_handler import selected_theme
from reports.people_snapshot import render_report
from data_handler import load_data

# Apply theme for the dashboard
selected_theme()

# Sidebar setup
st.sidebar.title("HR Dashboard")
selected_report = st.sidebar.selectbox("Select Report", ["People Snapshot"])

# Load Data (Only Employee Data for this report)
employee_df, _, _ = load_data()

# Render Report
if selected_report == "People Snapshot":
    render_report(employee_df)
