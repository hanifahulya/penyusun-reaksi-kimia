import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from utils.tabel_periodik_118 import Ar_tiap_unsur, elemen_periodik

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")

st.title("🧪 Penyusun Persamaan Reaksi Kimia")

halaman = st.sidebar.markdown("### 🌐 Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["📖 Dasar Teori", "🔬 Tabel Periodik"], label_visibility="collapsed")

if "📖 Dasar Teori" in halaman:
    st.header("📘 Dasar Teori")
    st.markdown("""
    Persamaan reaksi kimia merupakan representasi simbolik dari reaksi kimia dengan menyatakan reaktan dan produk yang terlibat. 
    Persamaan reaksi kimia menyatakan secara simbolik reaksi kimia dengan menggunakan rumus kimia dari zat-zat yang terlibat. Agar sah secara hukum kekekalan massa, persamaan ini harus setara, yaitu jumlah atom untuk setiap unsur harus sama di kedua sisi reaksi.

    ⚛️ **Contoh Persamaan Setara:**
    \[ 2H_2 + O_2 \\rightarrow 2H_2O \]

    Jenis reaksi kimia umum meliputi:
    
    - Reaksi Kombinasi (Sintesis) 🧩
    - Reaksi Penguraian (Dekomposisi) ⚡
    - Reaksi Pergantian Tunggal 🔁
    - Reaksi Pergantian Ganda 🔄
    - Reaksi Pembakaran 🔥

    Aplikasi ini membantu menyusun reaksi antara dua unsur dan menampilkan:
    - Persamaan reaksi setara ⚖️
    - Jenis reaksi ⚗️
    - Berat molekul (BM) dari senyawa hasil reaksi dalam satuan **g/mol** 

    Silakan pilih menu di sebelah kiri untuk memilih 2 unsur yang ingin direaksikan dari tabel periodik.
    """)

elif "🔬 Tabel Periodik" in halaman:
    st.header("🧪 Tabel Periodik Unsur")

    # Ambil semua golongan dari elemen_periodik
    golongan_list = []
    for baris in elemen_periodik:
        for e in baris:
            if e and "golongan" in e:
                golongan_list.append(e["golongan"])

    filter_gol = st.selectbox(
        "Filter Unsur berdasarkan Golongan",
        ["Semua"] + sorte
