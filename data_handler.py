
import pandas as pd

def load_data():
    # Ensure correct paths for data files
    employee_df = pd.read_excel('data/employee_master.xlsx')
    leave_df = pd.read_excel('data/HRMS_Leave.xlsx')
    sales_df = pd.read_excel('data/Sales_INR.xlsx')
    return employee_df, leave_df, sales_df
