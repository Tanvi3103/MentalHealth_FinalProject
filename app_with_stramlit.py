import streamlit as st
from predict import show_predict_page
#from xplore_page import show_explore_page
from home import show_home_page

page = st.sidebar.selectbox("**:black[MENU]**", ("HOME","PREDICT", "EXPLORE"))

if page == "PREDICT":
    show_predict_page()

if page == "HOME":
    show_home_page()