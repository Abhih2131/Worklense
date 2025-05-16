
import streamlit as st

def apply_kpi_style():
    st.markdown(
        '''
        <style>
        .kpi-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-bottom: 15px;
        }
        .kpi-value {
            font-size: 32px;
            font-weight: bold;
            color: #2C3E50;
        }
        .kpi-label {
            font-size: 16px;
            color: #6c757d;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )

def render_kpi(label, value, unit="", color="#2C3E50"):
    st.markdown(
        f"<div class='kpi-container'>"
        f"<div class='kpi-value' style='color: {color};'>{value}{unit}</div>"
        f"<div class='kpi-label'>{label}</div>"
        "</div>",
        unsafe_allow_html=True
    )
