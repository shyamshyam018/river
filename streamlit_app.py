import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    
    selected = option_menu('HI THIS MACHINE LEARNING MODEL IS CREATED BY SHYAM RAJ ',
                          
                          ['WHO AM I ',
                           'WHY ARE YOU HERE',
                           'CONTACT ?'],
                          icons=['activity','heart','person'],
                          default_index=0)
