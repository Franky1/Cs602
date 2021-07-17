import streamlit as st
from streamlit_lottie import st_lottie
import urllib.request
import requests
import pandas as pd

#def app():
#main page
#set the row style
row0_1, row0_2, row0_spacer3 = st.beta_columns(
    (2, 2, .1))
row0_1.title('This is the File look like📑')
with row0_2:
    st.title('This is the Volcano Map🌋')


#Read Github file
url = 'https://raw.githubusercontent.com/omeletteYAN/streamlit/main/volcanoes.csv'
#Read the data into a Pandas DataFram
df = pd.read_csv(url, encoding= 'Latin-1')
#set the colum I want cell DF
DF = pd.DataFrame(df,columns=['Volcano Name','Country',
                                'Primary Volcano Type',
                                'Last Known Eruption',
                                'Latitude','Longitude',
                                'Elevation (m)'
                                ])
#_______________________________________________________________
#filter
Select_list = DF.columns.values.tolist()

#select fires one
Select1 = st.sidebar.selectbox('please select',Select_list)

#select next one
Select_sublist = DF[Select1].unique()

#sort the lise
if Select1 == 'Elevation (m)':
    Select2 = st.sidebar.slider('Continue', sorted(int(Select_sublist)))
else:
    Select2 = st.sidebar.selectbox('Continue', sorted(Select_sublist))









#_______________________________________________________________

#table
with row0_1:
#Creat a new DataFram cell DF1
#select the columns number and name
#show the DF1 table in the webpage
    st.dataframe(Select_sublist,height=500)






#map for row0_2
with row0_2:
#select the Lat,Lon from data
#rename the data Lat and Lon to "lat and lon "
#show the map in the webpage
    DFMAP = Select_sublist.rename(columns={'Latitude':'latitude','Longitude':'longitude'})
    st.map(DFMAP)







st.markdown('***')
st.markdown("""If you want to know more about me! this is my 
            [website](https://omeletteyan.github.io/index/)⚓
            """)
