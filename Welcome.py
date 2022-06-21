# app2.py
import streamlit as st
from streamlit_lottie import st_lottie
import urllib.request
import requests
import time
import pandas as pd

#connect to page.py
def app():
    def Volcanoes_load(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    load_volcanoes = Volcanoes_load('https://assets6.lottiefiles.com/packages/lf20_ZdVYgO.json')#https://assets4.lottiefiles.com/packages/lf20_xCfcGS.json
    st_lottie(load_volcanoes, speed=0.8,height=850,key='initial')
       
    #Welcome sidebar
    st.sidebar.write("Hi!")
    container = st.sidebar.beta_container()
    
    #set time.sleep
    for percent_complete in range(1):
        time.sleep(1)
        container.write(
            "Welcome to my homepage. ")
        time.sleep(1)
        container.write(
            "I hope you like it")
        time.sleep(1)
    st.sidebar.write("Welcome to ask questions💡")
    time.sleep(1)
    
    st.sidebar.markdown('***')
    
    st.sidebar.subheader(
        """Description: 
        You can choose Two pages
        select the main page. 
        you will see the information
        about the volcanoe you select,
        also map will show the volcanoe""")
    
    st.sidebar.markdown('***')
    
    st.sidebar.subheader("""
    Made by:[Qiaofei Yan](https://omeletteyan.github.io/index/)
    Summer 2021 Cs602 Class                                                                     
    Data: [Volcanoes.csv](https://github.com/omeletteYAN/streamlit/blob/main/volcanoes.csv)  datasets                                                     
    Source Web: [volcano.com](https://volcano.si.edu/)""")
    
    
    
    
    

