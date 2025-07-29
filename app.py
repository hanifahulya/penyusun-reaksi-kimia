import streamlit as st
from reaction_engine.main import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui.tabel import tampilkan_tabel_periodik
from utils.tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title='Penyusun Persamaan Reaksi', layout='wide')

st.sidebar.title('Navigasi')
halaman = st.sidebar.radio('Pilih Halaman', ['Beranda', 'Dasar Teori'])

if halaman == 'Beranda':
    st.title("Penyusun Persamaan Reaksi Kimia")
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    st.write("Pilih unsur dari tabel periodik:")
    tampilkan_tabel_periodik()
elif halaman == "Dasar Teori":
    st.title("Dasar Teori")
    st.markdown("""
    Aplikasi ini digunakan untuk menyusun persamaan reaksi kimia berdasarkan unsur yang dipilih.
    Kamu dapat memilih satu atau lebih unsur dari tabel periodik yang disediakan. Setelah itu,
    aplikasi akan membantu menampilkan kemungkinan reaksi kimia berdasarkan kombinasi unsur tersebut.
    """)
