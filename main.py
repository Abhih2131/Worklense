
import streamlit as st
from theme_handler import selected_theme
from data_handler import load_data
import os

# Apply theme for the dashboard
selected_theme()

# Sidebar setup
st.sidebar.title("HR Dashboard")
selected_report = st.sidebar.selectbox("Select Report", ["People Snapshot"])

# Load Data
employee_df, leave_df, sales_df = load_data()

# Dynamically detect report folder (report or reports)
if os.path.exists("report/people_snapshot.py"):
    from report.people_snapshot import render_report
elif os.path.exists("reports/people_snapshot.py"):
    from reports.people_snapshot import render_report
else:
    st.error("Report module not found. Please ensure 'people_snapshot.py' is in the correct folder.")

# Render Report
if selected_report == "People Snapshot":
    render_report(employee_df, leave_df, sales_df)
