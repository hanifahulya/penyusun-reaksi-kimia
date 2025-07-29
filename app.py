import streamlit as st
from reaction_engine.main import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui.tabel import tampilkan_tabel_periodik
from utils.tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title='Penyusun Persamaan Reaksi Kimia', layout='wide')

st.sidebar.title('Navigasi')
halaman = st.sidebar.radio('Pilih Halaman', ['Dasar Teori', 'Penyusun Reaksi'])

if halaman == 'Dasar Teori':
    st.title("Dasar Teori")
    st.markdown("""
    Aplikasi ini dirancang untuk membantu dalam menyusun persamaan reaksi kimia secara otomatis.
    Pengguna dapat memilih unsur-unsur dari tabel periodik untuk menghasilkan reaksi yang setara,
    disertai jenis reaksinya, serta menghitung massa molekul relatif (BM) senyawa yang terbentuk.
    """)
elif halaman == 'Penyusun Reaksi':
    st.title("Penyusun Persamaan Reaksi Kimia")
    tampilkan_tabel_periodik()