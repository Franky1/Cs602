# app2.py
import streamlit as st
from streamlit_lottie import st_lottie
import urllib.request
import requests
import time
import pandas as pd

#connect to page.py
def app():
    #Welcome sidebar
    st.sidebar.write("Hi!")

    st.sidebar.subheader("""
    Made by:[Qiaofei Yan](https://omeletteyan.github.io/index/)
    Summer 2021 Cs602 Class                                                                     
    Data: [Volcanoes.csv](https://github.com/omeletteYAN/streamlit/blob/main/volcanoes.csv)  datasets                                                     
    Source Web: [volcano.com](https://volcano.si.edu/)""")

    
    
    
    

