import streamlit as st
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui import tampilkan_tabel_periodik
from utils.tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title="Penyusun Persamaan Reaksi", layout="wide")

st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["Dasar Teori", "Tabel Periodik"])

if halaman == "Dasar Teori":
    st.title("Penyusun Persamaan Reaksi Kimia")
    st.subheader("Dasar Teori")
    st.markdown("""
    Menyusun persamaan reaksi kimia adalah salah satu kompetensi dasar dalam pembelajaran kimia yang bertujuan untuk menggambarkan perubahan zat melalui notasi simbolik. 
    Dalam menyusun reaksi kimia, penting untuk memperhatikan hukum kekekalan massa yang menyatakan bahwa massa zat sebelum dan sesudah reaksi harus sama. 
    Oleh karena itu, reaksi harus disetarakan agar jumlah atom dari setiap unsur di kedua sisi persamaan tetap sama.

    Aplikasi ini membantu pengguna dalam menyusun dan menyetarakan persamaan reaksi kimia secara otomatis. Dengan antarmuka interaktif dan data unsur yang lengkap, 
    pengguna hanya perlu memilih unsur yang bereaksi, dan aplikasi akan menampilkan persamaan reaksi lengkap dengan informasi massa molekul relatif (Mr) dan jenis reaksinya.
    """)

elif halaman == "Tabel Periodik":
    st.title("Penyusun Persamaan Reaksi Kimia")
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    golongan_tersedia = list({elemen.get("golongan", "lainnya") for baris in elemen_periodik for elemen in baris if elemen.get("simbol")})
    golongan_tersedia.sort()
    gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan", ["Semua"] + golongan_tersedia)

    tampilkan_tabel_periodik(filter_golongan=gol_filter if gol_filter != "Semua" else None)

    if st.button("Reset Pilihan Unsur"):
        st.session_state.selected_elements = []

    if len(st.session_state.selected_elements) == 2:
        unsur1, unsur2 = st.session_state.selected_elements
        reaksi, jenis_reaksi = susun_reaksi_dari_unsur(unsur1, unsur2)
        if reaksi:
            st.markdown("### Persamaan Reaksi")
            st.latex(reaksi)

            Mr1 = hitung_massa_molekul(unsur1)
            Mr2 = hitung_massa_molekul(unsur2)
            st.markdown(f"**Mr {unsur1}** = {Mr1}")
            st.markdown(f"**Mr {unsur2}** = {Mr2}")
            st.markdown(f"**Jenis Reaksi**: {jenis_reaksi}")
        else:
            st.warning("Reaksi tidak tersedia dalam basis data.")
