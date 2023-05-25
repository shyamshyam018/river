import streamlit as st
st.title("THIS IS MY FIRST STREAMLIT APP")
col1, col2 = st.columns(2)

with col1:
  st.markdown(":moon HEY")
  
with col2:
  st.markdown(":world WHATSUP")
