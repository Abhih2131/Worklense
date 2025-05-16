
import streamlit as st
import pandas as pd
from datetime import datetime
from kpi_design import apply_kpi_style, render_kpi

def render_report(employee_df):
    st.title("📊 People Snapshot")
    apply_kpi_style()  # Applying the centralized KPI design

    # Setting up the current fiscal year range (April 1, 2025 to today)
    current_fy_start = datetime(2025, 4, 1)
    today = datetime.today()

    # Filtering active employees (No exit date)
    active_employees = employee_df[(employee_df['date_of_exit'].isna()) & (employee_df['date_of_joining'].notna())]

    # Calculating KPIs based on active employees
    total_active_employees = len(active_employees)
    new_hires = employee_df[(employee_df['date_of_joining'] >= current_fy_start) & (employee_df['date_of_joining'] <= today)]
    total_new_hires = len(new_hires)
    exits = employee_df[(employee_df['date_of_exit'] >= current_fy_start) & (employee_df['date_of_exit'] <= today)]
    total_exits = len(exits)
    average_ctc = active_employees['total_ctc_pa'].mean()
    active_employees['tenure_years'] = (today - active_employees['date_of_joining']).dt.days / 365
    average_tenure = active_employees['tenure_years'].mean()
    active_employees['age_years'] = (today - active_employees['date_of_birth']).dt.days / 365
    average_age = active_employees['age_years'].mean()
    average_experience = active_employees['total_exp_yrs'].mean()
    promotions_this_fy = active_employees[
        (active_employees['last_promotion'].notna()) & 
        (pd.to_datetime(active_employees['last_promotion'], errors='coerce') >= current_fy_start) & 
        (pd.to_datetime(active_employees['last_promotion'], errors='coerce') <= today)
    ]
    promotion_percentage = (len(promotions_this_fy) / total_active_employees) * 100 if total_active_employees > 0 else 0

    # Rendering the KPIs with the new design
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi("Active Employees", f"{total_active_employees:,}")
    with col2:
        render_kpi("New Hires (This FY)", f"{total_new_hires:,}")
    with col3:
        render_kpi("Exits (This FY)", f"{total_exits:,}")
    with col4:
        render_kpi("Average CTC (Active)", f"₹ {average_ctc:,.2f}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi("Average Tenure (Active)", f"{average_tenure:.2f} Years")
    with col2:
        render_kpi("Average Age (Active)", f"{average_age:.2f} Years")
    with col3:
        render_kpi("Average Total Experience (Active)", f"{average_experience:.2f} Years")
    with col4:
        render_kpi("Promotion Percentage (This FY)", f"{promotion_percentage:.2f} %")
