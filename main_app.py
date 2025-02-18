import streamlit as st
from PIL import Image

st.title('わいのアプリ')
st.caption('これはわいのテストアプリや')

# 画像
image = Image.open('./image/dog.jpg')
st.image(image, width=200)