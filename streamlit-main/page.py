#app.py
import Final_project_sample
import Welcome
import streamlit as st
from streamlit_lottie import st_lottie
PAGES = {
    "welcome page": Welcome,
    "main page": Final_project_sample
}
st.sidebar.title('SELECT PAGE')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
