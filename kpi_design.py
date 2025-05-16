
import streamlit as st

def apply_kpi_style():
    st.markdown(
        '''
        <style>
        .kpi-container {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 220px;
            height: 130px;
            display: inline-block;
            transition: transform 0.2s, box-shadow 0.2s;
            margin: 10px;
        }
        .kpi-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.15);
        }
        .kpi-value {
            font-size: 28px;
            font-weight: bold;
            color: #1A1A1A;
            margin-bottom: 5px;
        }
        .kpi-label {
            font-size: 14px;
            color: #6c757d;
            text-transform: uppercase;
        }
        .kpi-row {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
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

def render_kpi(label, value, unit="", color="#1A1A1A"):
    value = format_number_indian_style(value)
    st.markdown(
        f"<div class='kpi-container'>"
        f"<div class='kpi-value' style='color: {color};'>{value}{unit}</div>"
        f"<div class='kpi-label'>{label}</div>"
        "</div>",
        unsafe_allow_html=True
    )
