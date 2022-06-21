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

    st.sidebar.subheader("""
    Made by:[Qiaofei Yan](https://omeletteyan.github.io/index/)
    Summer 2021 Cs602 Class                                                                     
    Data: [Volcanoes.csv](https://github.com/omeletteYAN/streamlit/blob/main/volcanoes.csv)  datasets                                                     
    Source Web: [volcano.com](https://volcano.si.edu/)""")
    
    
    
    
    

