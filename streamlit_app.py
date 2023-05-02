import streamlit as st
from streamlit_option_menu import option_menu

st.title("HI THIS MACHINE LEARNING MODEL IS CREATED BY SHYAM RAJ")
with st.sidebar:
    
    selected = option_menu('CHOOSE AN ACTION BELOW',
                          
                          ['WHAT CAN THIS MODEL DETECT',
                           'UPLOAD YOUR IMAGE',
                           'ABOUT US'],
                          icons=['image','upload','globe'],
                          default_index=0)
if selected == 'WHAT CAN THIS MODEL DETECT':
    st.write('This model can detect...')
    # Add code to show output for this option
    
elif selected == 'UPLOAD YOUR IMAGE':
    uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    # Add code to show output for this option
    
else:
    st.write('About us...')
    # Add code to show output for this option
