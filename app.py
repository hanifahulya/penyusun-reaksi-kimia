import streamlit as st
from reaction_engine.main import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui import tampilkan_tabel_periodik
from utils.tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title='Penyusun Persamaan Reaksi', layout='wide')

st.sidebar.title('Navigasi')
halaman = st.sidebar.radio('Pilih Halaman', ['Dasar Teori', 'Tabel Periodik'])

if halaman == 'Dasar Teori':
    st.title("Dasar Teori")
    st.markdown("""
    **Reaksi kimia** adalah proses di mana satu atau lebih zat (reaktan) diubah menjadi satu atau lebih zat baru (produk). 
    Dalam reaksi kimia, terjadi perubahan susunan atom yang melibatkan pemutusan dan pembentukan ikatan kimia.

    **Contoh umum reaksi kimia**:
    - Reaksi pembakaran
    - Reaksi pengendapan
    - Reaksi asam-basa
    - Reaksi redoks

    Aplikasi ini membantu dalam menyusun persamaan reaksi dari dua unsur dan menampilkan hasil reaksi yang setara, jenis reaksi, serta massa molekul relatif (BM) dari senyawa hasil reaksi.
    """)
elif halaman == 'Tabel Periodik':
    st.title("Penyusun Persamaan Reaksi Kimia")
    tampilkan_tabel_periodik(elemen_periodik)
