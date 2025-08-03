import streamlit as st

st.set_page_config(
    page_title="Tip Calculator",
    page_icon="💰",
)

st.title("💰 Tip Calculator")
st.write("Quickly split your bill and add a tip!")

# Input fields
bill = st.number_input("What was the total bill?", min_value=0.0, format="%.2f", step=0.5)
tip = st.slider("What percentage tip would you like to give?", min_value=0, max_value=100, value=15)
people = st.number_input("How many people to split the bill?", min_value=1, step=1)

# Only calculate if bill is entered
if bill > 0:
    tip_amount = bill * (tip / 100)
    total_bill = bill + tip_amount
    split = round(total_bill / people, 2)

    st.markdown("---")
    st.success(f"Each person should pay: **${split:.2f}**")