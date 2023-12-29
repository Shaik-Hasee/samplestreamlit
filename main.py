import streamlit as st
from PIL import Image
st.write("<h1>This is my streamlit page</h1>",unsafe_allow_html=True)
st.write("<h1 style='color:red;'>This is my streamlit page</h1>",unsafe_allow_html=True)
uploaded_file=st.file_uploader("upload a file")
st.image("https://rukminim1.flixcart.com/flap/96/96/image/22fddf3c7da4c4f4.png?q=100")
image=Image.open(uploaded_file)
st.image(image, caption='Image uploaded',use_column_width=True)
