import streamlit as st
from data import data

st.title("AI Instrument Recommendation System")

user_input = st.text_input("Enter research objective:")

if user_input:
    result = data.get(user_input.lower())

    if result:
        st.subheader("Recommended Instrument:")
        st.write(result["instrument"])

        st.subheader("Reason:")
        st.write(result["reason"])
    else:
        st.write("No data available. Try another input.")