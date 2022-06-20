# app2.py
import streamlit as st
from streamlit_lottie import st_lottie
import urllib.request
import requests
import time
import pandas as pd
st.set_page_config(layout="wide")
def app():
    def Volcanoes_load(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    load_volcanoes = Volcanoes_load('https://assets4.lottiefiles.com/packages/lf20_xCfcGS.json')
    st_lottie(load_volcanoes, speed=0.8,height=850,key='initial')
        #Welcome sidebar
    st.sidebar.write("Hi!")
    container = st.sidebar.container()
    #let the show speed to be 1
    for percent_complete in range(1):
        time.sleep(1)
        container.write(
            "Welcome to my Page")
        time.sleep(1)
        container.write(
            "Hope you like the Page")
        time.sleep(1)
    st.sidebar.write("🧠Feel free to ask question")
    st.balloons()
    
    st.sidebar.markdown('***')
    
    st.sidebar.subheader("""
    Made by:[Qiaofei Yan](https://omeletteyan.github.io/index/)
    CS602: Summer 2021                                                                     
    Data: [Volcanoes.csv](https://github.com/omeletteYAN/streamlit/blob/main/volcanoes.csv)  datasets                                                     
    Source Web: [volcano.com](https://volcano.si.edu/)""")
    st.sidebar.subheader(
        'Description: //////////////////////////////////////////')
    
    
    

