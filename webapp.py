import streamlit as st
import requests

# Streamlit App Configuration
st.set_page_config(page_title="Mortgage Calculator", layout="centered")

# API Configuration
API_KEY = "7IY8r4exuquKecRQdEq0bA==xcKDLpknEDEDyZA5"

# Function to Fetch Mortgage Calculation
def calculate_mortgage(loan_amount, interest_rate, duration_years):
    api_url = (
        f"https://api.api-ninjas.com/v1/mortgagecalculator"
        f"?loan_amount={loan_amount}&interest_rate={interest_rate}&duration_years={duration_years}"
    )
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# UI for the App
st.title("🏠 Mortgage Calculator")
st.markdown("Calculate your monthly mortgage payment using this tool.")

# User Inputs
loan_amount = st.number_input("Loan Amount ($):", min_value=1000, step=1000, value=200000)
interest_rate = st.number_input("Interest Rate (%):", min_value=0.1, step=0.1, value=3.5)
duration_years = st.number_input("Duration (Years):", min_value=1, step=1, value=30)

# Calculate Button
if st.button("Calculate Mortgage"):
    if loan_amount > 0 and interest_rate > 0 and duration_years > 0:
        result = calculate_mortgage(loan_amount, interest_rate, duration_years)
        if "error" in result:
            st.error(f"Error: {result['error']}")
        else:
            monthly_payment = result.get("monthly_payment", "N/A")
            st.success(f"💵 Your Monthly Payment: ${monthly_payment}")
    else:
        st.warning("Please enter valid inputs for all fields.")
