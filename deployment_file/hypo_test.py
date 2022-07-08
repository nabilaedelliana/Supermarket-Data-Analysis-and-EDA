# Import library yang digunakan
import streamlit as st
from PIL import Image

# Menyusun Page Hypothesis Testing
def app():
    st.title('HYPOTHESIS TESTING')
    
    st.caption('Hipotesis testing untuk membantu tim marketing mengambil keputusan dalam upaya peningkatan pendaftaran member supermarket')
    
    st.write("""
             Analisis hipotesis ini bertujuan untuk mengetahui apakah perlu adanya peningkatan fasilitas untuk 
             member customer agar menarik pelanggan non-customer untuk mendaftar member. 
             Keputusan akan dilihat apakah perbedaan rerata rating member customer dan 
             non-member customer signifikan atau tidak. Jika tidak signifikan, 
             maka perlu adanya peningkatan fasilitas agar rating member customer meningkat dan 
             menarik non-member customer untuk mendaftar member.
    """)
   
    st.subheader('Pendefinisian Hipotesis Testing')
    st.write("""
             mu1 = Mean Rating from Member Customer

             mu2 = Mean Rating from Non-Member Customer

             - H0 : mu1 = mu2
             - H1 : mu1 != mu2
    """)
    
    st.subheader('Komponen Hipotesis Testing')
    st.write("""
             Rating of Member Customer:

             mean = 6.940319
             
             std = 1.74938
             
             Rating of Non-Member Customer:

             mean = 7.00521
             
             std = 1.688222
             
             P-value: 0.5507621727856713
             
             t-statistics: -0.5968211265254104
             
             confident interval : 95%
             
             Alpha (α) : 0.05
    """)
    
    st.subheader('Grafik Hipotesis Testing')
    img = Image.open('pichypotest.png')
    st.image(img, caption='Grafik Hasil dari Hipotesis Testing Metode 2 Sample 2 Tailed')
    
    st.subheader('Kesimpulan Hipotesis Testing')
    st.write("""
             **Kesimpulan grafik hasil uji hipotesis :**
             1. Dari grafik tersebut, dapat dilihar bahwa distribusi normal rating member customer dan non-member customer memiliki variansi yang dekat dengan mean.
             2. P-Value > α, artinya gagal menolak H0.
             3. Perbedaan antara rerata rating dari member customer dan non-member customer tidak signifikan.
    """)
    
    st.subheader('Kesimpulan dan Keputusan')
    st.write("""
             1. Rerata rating dari member customer memang lebih tinggi daripada non-customer member. Akan tetapi perbedaan tersebut tidak signifikan sehingga tidak cukup kuat untuk menarik non-member customer untuk mendaftar member.
             2. Saran untuk tim marketing adalah melakukan peningkatan fasilitas dan penawaran menarik untuk member customer agar rating dari member customer dapat meningkat lagi dan menarik non-member customer untuk mendaftar member.
    """)
