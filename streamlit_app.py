import streamlit as st
from streamlit_option_menu import option_menu

st.title("HI THIS MACHINE LEARNING MODEL IS CREATED BY SHYAM RAJ")
with st.sidebar:
    
    selected = option_menu('CHOOSE THE ACTION BELOW',
                          
                          ['WHAT CAN THIS MODEL DETECT',
                           'UPLOAD YOUR IMAGE',
                           'ABOUT US'],
                          icons=['glass','plant','person'],
                          default_index=0)
