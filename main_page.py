import streamlit as st
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import pandas as pd
import pydeck as pdk
import seaborn as sns
import numpy as np

#app() connect to page.py
def app():
    # create pie_chaet
    def pie_chart(DF2):
        DF2 = pd.DataFrame(DF2)
        list = DF2['Primary Volcano Type'].to_list()
        #pie chart label
        unique_type_list = []
        Count_Type_list = []
        for volcano_type in list:
            if volcano_type not in unique_type_list:
                unique_type_list.append(volcano_type)
        #add the number to count type list
        for uni_type in unique_type_list:
            number = list.count(uni_type)
            Count_Type_list.append(number)
        fig,ax = plt.subplots()
        plt.style.use('seaborn')
        #set Background color
        fig.patch.set_facecolor('#FEF8EF')
        maxValue = max(Count_Type_list)
        explodeList =[]
        for i in Count_Type_list:
            if i == maxValue:
                explodeList.append(0.1)
            else:
                explodeList.append(0)
        explode = tuple(explodeList)
        ax.pie(Count_Type_list,shadow=True,explode=explode,labels=unique_type_list,autopct='%1.1f%%')
        st.pyplot(fig)
    
    # create scatterplots
    def scatter_plot(DF2):
        sns.set_theme(style="whitegrid")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        numeric_columns = DF2.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
        # add select widget
        select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
        select_box2 = st.sidebar.selectbox(label="Y axis", options=numeric_columns)
        sns.relplot(x=select_box1, y=select_box2,data=DF2)
        st.pyplot()

    #Read the Vocanoes files
    @st.cache
    def load_data():
        #load the volcanoes
        Data = pd.read_csv('volcanoes.csv', encoding= 'Latin-1')
        return Data
    df = load_data()

    #Creat  DF1
    #DF1 columns:name,country,type,lat,lon,elevation
    DF1 = pd.DataFrame(df,columns=['Volcano Name','Country',
                                    'Primary Volcano Type',
                                    'Latitude','Longitude',
                                    'Elevation (m)','Link'])
    #_______________________________________________________________
    #filter
    #only select country
    Select_list = DF1['Country'].unique()

    #sort the lise
    Select2 = st.sidebar.selectbox('Select a Country', sorted(Select_list))

    #Country table
    #pie_chart
    #scatter_plot
    DF2 = DF1[DF1['Country']==Select2]
    E_table = pd.pivot_table(DF2,values=['Elevation (m)'],index=['Country'],aggfunc={np.mean})
    st.title('TABLE')
    st.write(DF2)
    
    #side by side
    col1, col2 = st.beta_columns([6, 4]) 
    with col1:
        st.title('PIE CHART')
        st.subheader('Percentage of Primary Volcano Type')
        pie_chart(DF2)
    with col2:
        st.title('SCATTER PLOT')
        st.subheader('The relationship between latitude,longitude and Elevation (m)')
        scatter_plot(DF2)
        st.write(E_table)
    
    
    # create map
    st.title('MAP')
    # create zoom and radius slider
    z2 = st.sidebar.slider('Map: Zoom Factor', min_value= 0, max_value = 10, value = 5)
    z3 = st.sidebar.slider('Map: Radius', min_value=0, max_value= 30000, value= 15000)
    view_state = pdk.ViewState(
        latitude= DF2["Latitude"].mean(),
        longitude= DF2["Longitude"].mean(),
        zoom = z2,)
    layer1 = pdk.Layer('ScatterplotLayer',
                        data = DF2,
                        pickable = True,
                        opacity = 0.20,
                        get_position = '[Longitude,Latitude]',
                        get_radius = z3,
                        get_color = [255,100,50],
                        )
    tool_tip = {"html": "<b>Volcano Name:<b><br/> {Volcano Name} <br/> Type: {Primary Volcano Type} <br/>Lat: {Latitude} Long: {Longitude}",
                "style": {"backgroundColor": "steelblue",
                            "color": "black"}
            }
    map = pdk.Deck(
        map_style='mapbox://styles/mapbox/satellite-streets-v11',
        layers = [layer1],
        initial_view_state=view_state,
        tooltip= tool_tip
    )
    st.pydeck_chart(map)


    st.markdown('***')
    st.markdown("""If you have any questions!you can find me here 
                [⚓](https://omeletteyan.github.io/index/)
                """)
app()
