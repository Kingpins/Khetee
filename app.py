import streamlit as st
from predict_weather import *
from predict_crop import *
from predict_dieases import *

st.set_page_config(page_title="Khetee - A Farmar's Assistant", page_icon="👨‍🌾", layout='centered', initial_sidebar_state="collapsed")

if __name__ == '__main__':
    st.sidebar.header('Khetee')
    activities = ["About", "Weather Predictor", "Crop Recommender", "Dieases Detection"]
    choose = st.sidebar.selectbox("Select Application",activities)
    if choose == "About":
        intro_markdown = read_markdown_file("./doc/intro.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)
    elif choose == "Weather Predictor":
        weather_main()
    elif choose == "Crop Recommender":
        croprecommendor_main()
    elif choose == "Dieases Detection":
        diesesdetection_main()
