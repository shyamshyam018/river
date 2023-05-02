import streamlit as st
from streamlit_option_menu import option_menu

st.title("HI THIS MACHINE LEARNING MODEL IS CREATED BY SHYAM RAJ")
with st.sidebar:
    
    selected = option_menu('CHOOSE THE PREDICTION MODEL',
                          
                          [':moon',
                           'WHY ARE YOU HERE',
                           'CONTACT ?'],
                          icons=['activity','heart','person'],
                          default_index=0)
