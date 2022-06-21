"""
Name: Qiaofei Yan
CS602-SN1
Data: Volcano.csv
URL: https://share.streamlit.io/omeletteyan/streamlit/main/page.py
Description:
    You can choose Two pages
    select the main page. 
    you will see the information
    about the volcanoe you select,
    also map will show the volcanoe.
"""
import main_page
import Welcome
import streamlit as st
import time
from streamlit_lottie import st_lottie
#set the page to be wide
st.set_page_config(layout="wide")

#Create two buttons
PAGES = {
    "welcome page": Welcome,
    "main page": main_page
}

time.sleep(1)
st.sidebar.title('SELECT PAGE👇🏼')
time.sleep(1)
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
time.sleep(1)
page.app()
