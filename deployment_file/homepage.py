import streamlit as st
from PIL import Image

def app():
     st.subheader('hello,')
     st.header('WELCOME, MARKETING TEAM!')
     st.caption('This website is developed for you. '
                'Please enjoy the journey of our supermarket data.')

     img = Image.open('trolley.jpg')
     st.image(img)