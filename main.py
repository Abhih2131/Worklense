
import streamlit as st
import sys
import os
from theme_handler import selected_theme
from data_handler import load_data

# Ensure 'reports' directory is in the Python path for module imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'reports'))

# Importing the report module with robust error handling
try:
    from people_snapshot import render_report
except ImportError:
    st.error("⚠️ Report module 'people_snapshot' not found. Ensure it exists in the 'reports' folder.")

# Apply theme for the dashboard
selected_theme()

# Sidebar setup
st.sidebar.title("HR Dashboard")
selected_report = st.sidebar.selectbox("Select Report", ["People Snapshot"])

# Load Data (Only Employee Data for this report)
employee_df, _, _ = load_data()

# Render Report
if selected_report == "People Snapshot":
    if 'render_report' in globals():
        render_report(employee_df)
    else:
        st.error("⚠️ Report 'People Snapshot' could not be loaded. Please check the reports folder.")
