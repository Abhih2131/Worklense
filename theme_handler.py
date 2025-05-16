
import streamlit as st

def selected_theme():
    st.set_page_config(page_title="Worklense HR Dashboard", layout="wide")
    st.markdown("""
        <style>
            .main { background-color: #f4f4f9; }
            .sidebar { background-color: #2C3E50; color: white; }
            .report-title { font-size: 28px; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)
