
import streamlit as st

def render_report(employee_df, leave_df, sales_df):
    st.title("📊 People Snapshot")
    st.write("Employee Records:", employee_df.shape[0])
    st.write("Leave Records:", leave_df.shape[0])
    st.write("Sales Records:", sales_df.shape[0])
