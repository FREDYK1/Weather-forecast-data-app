import streamlit as st
import plotly.express as px
from backend import get_data


st.header("Weather Forecast for the Next Days")

place = st.text_input("Place")

days = st.slider("Forecast Days", min_value=1, max_value=5)

options = st.selectbox("Select date to view", ("Temperature", "Sky"))

st.subheader(f"{options} for the next {days} days in {place}")

filtered_data = get_data(place, days)

if place:
    if options == "Temperature":
        Temperature = [dict["main"]["temp"] for dict in filtered_data]
        date = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(date, Temperature, labels={"x":"Date", "y":"Temperature"})
        st.plotly_chart(figure)
    if options == "Sky":
        images = {"Clear":"images/clear.png", "Cloud":"cloud.png", "Rain":"rain.png",
                  "Snow":"snow.png"}
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in filtered_data]
        st.image(image_paths, width=115)
