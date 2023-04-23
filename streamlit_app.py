import streamlit as st

st.write('HELLO WORLD')

window = st.slider("Forecast")
st.write(m.run(window=15))
