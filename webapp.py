import streamlit as st
import requests
#123

# API URL and headers
api_url = 'https://api.api-ninjas.com/v1/mortgagecalculator'
api_key = '7IY8r4exuquKecRQdEq0bA==xcKDLpknEDEDyZA5'  # Replace this with your actual API key

def get_mortgage_data(loan_amount, interest_rate, duration_years):
    params = {
        'loan_amount': loan_amount,
        'interest_rate': interest_rate,
        'duration_years': duration_years
    }
    headers = {'X-Api-Key': api_key}
    response = requests.get(api_url, headers=headers, params=params)
    return response

def display_mortgage_info(data):
    st.subheader("Mortgage Payment Information")
    st.write(f"Monthly Payment: ${data['monthly_payment']['total']}")
    st.write(f"Annual Payment: ${data['annual_payment']['total']}")
    st.write(f"Total Interest Paid: ${data['total_interest_paid']}")

# Streamlit user interface
st.title('Mortgage Calculator')

loan_amount = st.number_input('Loan Amount', min_value=1, max_value=10000000, value=200000, step=1000)
interest_rate = st.number_input('Interest Rate (%)', min_value=0.0, max_value=100.0, value=3.5, step=0.1)
duration_years = st.number_input('Loan Duration (years)', min_value=1, max_value=50, value=30, step=1)

if st.button('Calculate'):
    response = get_mortgage_data(loan_amount, interest_rate, duration_years)
    if response.status_code == 200:
        data = response.json()
        display_mortgage_info(data)
    else:
        st.error(f"Error {response.status_code}: {response.text}")
