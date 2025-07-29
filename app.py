import streamlit as st
from reaction_engine.main import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui.tabel import tampilkan_tabel_periodik
from utils.tabel_periodik_118.tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title='Penyusun Persamaan Reaksi Kimia', layout='wide')

st.sidebar.title('Navigasi')
halaman = st.sidebar.radio('Pilih Halaman', ['Beranda', 'Dasar Teori'])

if halaman == 'Dasar Teori':
    st.title("Dasar Teori")
    st.markdown("""
    Aplikasi ini digunakan untuk menyusun persamaan reaksi kimia dari unsur-unsur yang tersedia 
    pada tabel periodik. Pengguna dapat memilih dua unsur, dan aplikasi akan mencoba menyusun 
    persamaan reaksinya jika tersedia. Hasil reaksi akan ditampilkan dalam bentuk reaksi setara, 
    jenis reaksi, serta massa molekul (BM) dari senyawa hasil reaksi.
    """)
else:
    tampilkan_tabel_periodik()
