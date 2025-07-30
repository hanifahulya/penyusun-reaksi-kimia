
import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import proses_reaksi
from utils.tabel_periodik_118 import Ar_tiap_unsur

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")

st.title("🧪 Penyusun Persamaan Reaksi Kimia")
halaman = st.sidebar.selectbox("Navigasi", ["Dasar Teori", "Tabel Periodik"])

if halaman == "Dasar Teori":
    st.header("📘 Dasar Teori")
    st.markdown("""
    Persamaan reaksi kimia merupakan representasi simbolik dari reaksi kimia dengan menyatakan reaktan dan produk yang terlibat.
    Persamaan ini harus setara, yaitu jumlah atom untuk setiap unsur harus sama di kedua sisi reaksi.

    ⚛️ **Contoh Persamaan Setara:**
    \[ 2H_2 + O_2 \rightarrow 2H_2O \]

    Jenis reaksi kimia umum meliputi:

    - Reaksi Kombinasi (Sintesis) 🧩
    - Reaksi Penguraian (Dekomposisi) ⚡
    - Reaksi Pergantian Tunggal 🔁
    - Reaksi Pergantian Ganda 🔄
    - Reaksi Pembakaran 🔥

    Aplikasi ini membantu menyusun reaksi antara dua unsur dan menampilkan:
    - Persamaan reaksi setara
    - Jenis reaksi ⚗️
    - Berat molekul (BM) hasil reaksi dalam **g/mol**
    """)

elif halaman == "Tabel Periodik":
    st.header("🔬 Tabel Periodik Unsur")
    gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan", options=[
        "Semua", "logam alkali", "logam alkali tanah", "logam transisi",
        "logam pasca transisi", "metaloid", "nonlogam", "halogen",
        "gas mulia", "lanthanida", "aktinida"
    ])
    tampilkan_tabel_periodik(filter_golongan=None if gol_filter == "Semua" else gol_filter, dengan_warna=True)

    if "selected_elements" in st.session_state and len(st.session_state.selected_elements) == 2:
        unsur1, unsur2 = st.session_state.selected_elements
        st.subheader(f"🔍 Hasil Reaksi: {unsur1} + {unsur2}")
        hasil = proses_reaksi(unsur1, unsur2)
        if hasil:
            st.success(f"**Reaksi:** {hasil['reaksi']}")
            st.info(f"**Jenis Reaksi:** {hasil['jenis']}")
            st.write(f"**Berat Molekul (BM):** {hasil['bm']} g/mol")
        else:
            st.warning("Tidak ditemukan reaksi yang cocok antara kedua unsur ini.")
        if st.button("🔁 Reset Pilihan"):
            st.session_state.selected_elements = []
    