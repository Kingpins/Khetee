import streamlit as st
from streamlit_option_menu import option_menu
from predict_weather import *
from predict_crop import *
from predict_dieases import *

st.set_page_config(page_title="Khetee - A Farmar's Assistant", page_icon="👨‍🌾", layout='centered', initial_sidebar_state="collapsed")

if __name__ == '__main__':
    with st.sidebar:
        choose = option_menu("Khetee", ["About", "Weather Predictor", "Crop Recommender", "Dieases Detection", "Developer"],
                         icons=['book', 'cloud', 'flower1', 'file-earmark','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
        )
    if choose == "About":
        intro_markdown = read_markdown_file("./doc/intro.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)
    elif choose == "Weather Predictor":
        weather_main()
    elif choose == "Crop Recommender":
        croprecommendor_main()
    elif choose == "Dieases Detection":
        diesesdetection_main()