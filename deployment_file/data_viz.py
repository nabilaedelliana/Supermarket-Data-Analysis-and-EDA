# Import library yang digunakan
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/nabilaedelliana/learning_journal/main/phase_0/week_4/supermarket_sales-Sheet1.csv')
# Memisahkan tanggal menjadi kolom tahun, bulan, dan hari
def split_date(df):
    df['Date']=pd.to_datetime(df['Date'])
    df['Year']=df.Date.dt.year
    df['Month']=df.Date.dt.month
    df['Day']=df.Date.dt.day
split_date(df)

# Menyusun Page Visualisasi
def app():
    # Bagian 1. Informasi dan pengantar page visualization
    st.header('DATA VISUALIZATION')
    
    st.caption('Data di web ini adalah data publik dan mohon digunakan dengan sebaik-baiknya.')
    
    # Bagian 2. Grafik 1. 
    st.subheader('Proporsi Jenis Product')
    st.write("""Supermarket kami menjual berbagai jenis produk. Terdapat 6 jenis produk yang kami jual. Produk yang paling banyak kami jual adalah di bidang Fashion Accessories.  """)
    fig1, ax1 = plt.subplots(figsize=[10,4])
    viz1 = df['Product line'].value_counts().plot(kind='pie', figsize=(10,10), autopct='%.2f', ax=ax1)
    st.pyplot(fig1)
    
    # Bagian 3. Grafik 2. 
    st.subheader('Grafik Rerata Rating Berdasarkan Gender di Setiap Branch')
    if st.checkbox('Tampilkan Tabel'):
        st.subheader('Tabel Rerata Rating Berdasarkan Gender di Setiap Branch')
        r_gb = df.groupby(['Branch','Gender'])[['Gender', 'Rating']].mean()
        st.write(r_gb)
    
    # Bagian 4. Tabel 1.   
    r_gbv = df[(df['Gender'] == 'Male') | (df['Gender'] == 'Female')].groupby(['Branch','Gender']).mean()['Rating'].reset_index()
    fig3, ax3 = plt.subplots(figsize=[10,4])
    sns.barplot(x=r_gbv['Branch'],y=r_gbv['Rating'],orient='v',hue=r_gbv['Gender'], ax=ax3)
    st.pyplot(fig3)
    
    # Bagian 5. Grafik 3. 
    st.subheader('Proporsi Jenis Customer')
    fig4, ax4 = plt.subplots(figsize=[10,4])
    viz3 = df['Customer type'].value_counts().plot(kind='pie', figsize=(10,10), autopct='%.2f', ax=ax4)
    st.pyplot(fig4)
    
    # Bagian 6. Grafik 4. 
    st.subheader('Data Rerata Rating Berdasarkan Jenis Customer di Setiap Branch')
    r_mbv = df[(df['Customer type'] == 'Member') | (df['Customer type'] == 'Normal')].groupby(['Branch','Customer type']).mean()['Rating'].reset_index()
    fig5, ax5 = plt.subplots(figsize=[10,4])
    viz4 = sns.barplot(x=r_mbv['Branch'],y=r_mbv['Rating'],orient='v',hue=r_mbv['Customer type'], ax=ax5)
    st.pyplot(fig5)
    
    # Bagian 7. Expander untuk penjelasan Grafik 4. 
    with st.expander("Lihat penjelasan"):
        st.write("""
            Rerata rating member customer dan non-member customer memiliki kemiripan.
             Di setiap branch supermarket, rerata rating antara member customer dan non-member customer cukup bervariasi.
             Apabila ingin melihat analisis lebih lanjut mengenai hal ini, silahkan pergi ke halaman hypothesis testing.
        """)
    
    # Bagian 8. Callback interaktivity 1
    st.subheader('Data rating per bulan oleh customer di tahun 2019')
    month = st.selectbox('Select Month:', options=[1, 2, 3])

    fig6, ax6 = plt.subplots()
    sns.histplot(df[df['Month']== 1]['Rating'])
    st.pyplot(fig6)

    # Bagian 9. Callback interaktivity 2
    st.subheader('Data rating oleh customer tiap gender di tahun 2019')
    selected_2 = st.radio('Select Gender:', options=df['Gender'].unique())

    fig7, ax7 = plt.subplots()
    sns.histplot(df[df['Gender']==selected_2]['Rating'])
    st.pyplot(fig7)
