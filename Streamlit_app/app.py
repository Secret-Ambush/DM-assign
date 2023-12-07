import streamlit as st
import pandas as pd
from PIL import Image  
import pandas as pd
import pickle
from datetime import datetime, timedelta
import numpy as np
import xgboost as xg
from plotly_calplot import calplot
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time
from streamlit_option_menu import option_menu


#reading csv file
@st.cache_data
def fetch_flight_data(fltnumber):
    with st.spinner('Loading Data...'):
        time.sleep(0.5)
        flight_data = pd.read_csv()
    return flight_data

img = Image.open("/Users/bristi/Desktop/DM assign/Streamlit_app/assets/airline.png")
img2 = Image.open("/Users/bristi/Desktop/DM assign/Streamlit_app/assets/airline2.png")


st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"]{
        min-width: 250px;
        max-width: 500px;
    }
    """,
    unsafe_allow_html=True,
)   

st.sidebar.title("Delay Prediction + Flight Analysis")
st.sidebar.image(img2,width = 100)
st.sidebar.markdown("")
side_bar = st.sidebar.radio('What would you like to view?', [ 'About the dataset', 'Analysis 🔎', 'Predicting Delay', 'Help: Regression📝'])

if side_bar == 'About the dataset':
    header = st.container()
    features = st.container()

    with header:
        
        text_col,image_col = st.columns((5.5,1))
        
        with text_col:
            st.title("Understanding the Dataset")
            st.markdown("The dataset contains information of American Airlines from 2018 - 2022.")
            markdown_text = '''
            ```
            Data columns (total 61 columns):
            No   Column                                   Dtype  
            ---  ------                                   -----  
            0   FlightDate                               object 
            1   Airline                                  object 
            2   Origin                                   object 
            3   Dest                                     object 
            4   Cancelled                                bool   
            5   Diverted                                 bool   
            6   CRSDepTime                               int64  
            7   DepTime                                  float64
            8   DepDelayMinutes                          float64
            9   DepDelay                                 float64
            10  ArrTime                                  float64
            11  ArrDelayMinutes                          float64
            12  AirTime                                  float64
            13  CRSElapsedTime                           float64
            14  ActualElapsedTime                        float64
            15  Distance                                 float64
            16  Year                                     int64  
            17  Quarter                                  int64  
            18  Month                                    int64  
            19  DayofMonth                               int64  
            20  DayOfWeek                                int64  
            21  Marketing_Airline_Network                object 
            22  Operated_or_Branded_Code_Share_Partners  object 
            23  DOT_ID_Marketing_Airline                 int64  
            24  IATA_Code_Marketing_Airline              object 
            25  Flight_Number_Marketing_Airline          int64  
            26  Operating_Airline                        object 
            27  DOT_ID_Operating_Airline                 int64  
            28  IATA_Code_Operating_Airline              object 
            29  Tail_Number                              object 
            30  Flight_Number_Operating_Airline          int64  
            31  OriginAirportID                          int64  
            32  OriginAirportSeqID                       int64  
            33  OriginCityMarketID                       int64  
            34  OriginCityName                           object 
            35  OriginState                              object 
            36  OriginStateFips                          int64  
            37  OriginStateName                          object 
            38  OriginWac                                int64  
            39  DestAirportID                            int64  
            40  DestAirportSeqID                         int64  
            41  DestCityMarketID                         int64  
            42  DestCityName                             object 
            43  DestState                                object 
            44  DestStateFips                            int64  
            45  DestStateName                            object 
            46  DestWac                                  int64  
            47  DepDel15                                 float64
            48  DepartureDelayGroups                     float64
            49  DepTimeBlk                               object 
            50  TaxiOut                                  float64
            51  WheelsOff                                float64
            52  WheelsOn                                 float64
            53  TaxiIn                                   float64
            54  CRSArrTime                               int64  
            55  ArrDelay                                 float64
            56  ArrDel15                                 float64
            57  ArrivalDelayGroups                       float64
            58  ArrTimeBlk                               object 
            59  DistanceGroup                            int64  
            60  DivAirportLandings                       int64 
            ```
            '''
            st.markdown(markdown_text)
            st.write("")
        
        
               
elif side_bar == 'Analysis 🔎':
    col1, col2 = st.columns((5,5))       
    with col1:
        st.markdown(""" ## Classification Model Documentation""")
    with col2:
        st.image("https://media.giphy.com/media/H1dXomvQ0jxNLASIqK/giphy.gif", width = 200)
        
    st.markdown(""" 

""")
elif side_bar == "Predicting Delay":  
     
    text,img2 = st.columns((2,1))
    with text:
        st.title("Predicting by how many minutes a flight will be delayed")
        st.markdown("Trained on historical data from `2018-2021`") 
        st.markdown("Predicts `2022` flight") 
        st.write("")
        st.write("")
        
    with img2:
        st.image("https://media.giphy.com/media/fsDIB8vYY4Vq2OSVwt/giphy.gif", width = 150)
        
    st.write("We have identified that SouthWestern Airlines and Delta Airlines are the most \
            popular and have maximum data available in the dataset.")
    
    st.write("In this page, you can choose between these two airlines and \
        use our model to predict by hom many minutes flights will get delayed all through out the year.")
    
    st.write("⚠️ Please note that these airlines have multiple flights going out on the same day\
        So, predicted delay and actual delay are averaged.")
    
    options = ["Southwestern Airlines", "Delta Airlines"]
    with st.form(key='airline_form'):
        selected_option = st.selectbox("Select an Airline", options)
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        markdown_text = f" You have selected: `{selected_option}\n`"
        st.sidebar.markdown(markdown_text)
          
          
          
elif side_bar == "📝Help: Regression":
    st.markdown("Blah")