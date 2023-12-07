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

img = Image.open("Streamlit_app/assets/airline.png")
img2 = Image.open("Streamlit_app/assets/airline2.png")


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

st.sidebar.title("Delay Prediction")
st.sidebar.image(img2,width = 100)
side_bar = st.sidebar.radio('What would you like to view?', [ 'About the dataset', 'Analysis 🔎', 'Predicting Delay', '📝Help: Regression'])

if side_bar == 'About the dataset':
    header = st.container()
    features = st.container()

    with header:
        
        text_col,image_col = st.columns((5.5,1))
        
        with text_col:
            st.title("Understanding the Dataset")
            st.markdown("The dataset contains information of American Airlines from 2018 - 2022.")
        
        
               
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
        st.title("SODP Regression Model")
        st.markdown("Predicts exactly when the flight will get full")  
        st.markdown("Trained on historical data from `2019-2021`") 
        st.markdown("Predicts `2022` flight") 
        st.write("")
        st.write("")
        
    with img2:
        st.image("https://media.giphy.com/media/cNZQpCC8kY60gnnd0n/giphy.gif", width = 150)
    
elif side_bar == "📝Help: Regression":
    st.markdown("Blah")