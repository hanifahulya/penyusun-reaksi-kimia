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
    Aplikasi ini membantu menyusun persamaan reaksi kimia sederhana secara otomatis.
    Kamu bisa memilih dua unsur dari tabel periodik, dan aplikasi akan menampilkan reaksi
    kimia yang terjadi jika memungkinkan, lengkap dengan jenis reaksi dan massa molekulnya.
    """)

elif "🔬 Tabel Periodik" in halaman:
    st.header("🧪 Tabel Periodik Unsur")

    # Ambil semua golongan dari elemen_periodik
    golongan_list = []
    for baris in elemen_periodik:
        for e in baris:
            if e and "golongan" in e:
                golongan_list.append(e["golongan"])

    # Tampilkan dropdown filter dengan selectbox
    filter_gol = st.selectbox(
        "Filter Unsur berdasarkan Golongan",
        ["Semua"] + sorted(set(golongan_list))
    )

    # Tampilkan tabel sesuai filter
    tampilkan_tabel_periodik(filter_gol)
