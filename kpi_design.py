
import streamlit as st

def apply_kpi_style():
    st.markdown(
        '''
        <style>
        .kpi-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            text-align: center;
            margin-bottom: 15px;
            width: 180px;
            height: 100px;
            display: inline-block;
        }
        .kpi-value {
            font-size: 28px;
            font-weight: bold;
            color: #2C3E50;
            margin-bottom: 4px;
        }
        .kpi-label {
            font-size: 12px;
            color: #6c757d;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )

def format_number_indian_style(value):
    try:
        value = float(value)
        if value >= 10000000:
            return f"{value / 10000000:.2f} Cr"
        elif value >= 100000:
            return f"{value / 100000:.2f} L"
        elif value >= 1000:
            return f"{value / 1000:.2f} K"
        else:
            return f"{int(value):,}"
    except:
        return value

def render_kpi(label, value, unit="", color="#2C3E50"):
    value = format_number_indian_style(value)
    st.markdown(
        f"<div class='kpi-container'>"
        f"<div class='kpi-value' style='color: {color};'>{value}{unit}</div>"
        f"<div class='kpi-label'>{label}</div>"
        "</div>",
        unsafe_allow_html=True
    )
