# Import library dan page yang digunakan
import homepage, data_viz, hypo_test
import streamlit as st
from PIL import Image

# Mengatur konfirgurasi halaman web
st.set_page_config(
    page_title="H8 Streamlit",
    page_icon="📈",
    layout="centered", # wide, center, dll
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.github.com/nabilaedelliana',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is my first *streamlit*, so fun!!"
    }
)

# Membuat variabel berisi halaman web
PAGES ={'Homepage': homepage,
        'Data Visualization': data_viz,
         'Hypothesis Testing': hypo_test,
         }

# Membuat sidebar untuk memilih halaman web
selected = st.sidebar.selectbox('Please Select Page:', options=PAGES.keys())

# Mendefinisikan isi keseluruhan halaman web
page = PAGES[selected]

page.app()

# Membuat pesan yang akan tertampil di setiap halaman web
st.write('This page is developed by Nabila Edelliana Khairunnisa. If the any issues please check the help page.')