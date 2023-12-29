import streamlit as st
streamlit.write("<h1>This is my streamlit page</h1>",unsafe_allow_html=True)
streamlit.write("<h1 style='color':'red'>This is my streamlit page</h1>",unsafe_allow_html=True)
st.file_uploader("upload a file")
st.image('jpg','png',jpeg')
