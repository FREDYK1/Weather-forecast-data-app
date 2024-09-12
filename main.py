import streamlit as st


st.header("Weather Forecast for the Next Days")

place = st.text_input("Place")

days = st.slider("Forecast Days", min_value=1, max_value=5)

options = st.selectbox("Select date to view", ("Temperature", "Sky"))

st.subheader(f"{options} for the next {days} days in {place}")