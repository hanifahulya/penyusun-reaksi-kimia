import streamlit as st
from reaction_engine import proses_reaksi
from periodic_table_ui import tampilkan_tabel_periodik
from utils.tabel_periodik_118 import Ar_tiap_unsur

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")

st.title("⚗️ Penyusun Persamaan Reaksi Kimia")

halaman = st.sidebar.radio("Pilih Halaman", ["📚 Dasar Teori", "🧪 Tabel Periodik", "🧮 Reaksi Kimia"])

if "unsur_terpilih" not in st.session_state:
    st.session_state.unsur_terpilih = []

if "hasil_reaksi" not in st.session_state:
    st.session_state.hasil_reaksi = ""

if "jenis_reaksi" not in st.session_state:
    st.session_state.jenis_reaksi = ""

if "massa_molekul" not in st.session_state:
    st.session_state.massa_molekul = ""

if "error" not in st.session_state:
    st.session_state.error = ""

# Halaman 1: Dasar Teori
if "📚 Dasar Teori" in halaman:
    st.header("📚 Dasar Teori")
    st.markdown("""
    Persamaan reaksi kimia merupakan representasi simbolik dari reaksi kimia dengan menyatakan reaktan dan produk yang terlibat. 
    Persamaan reaksi kimia menyatakan secara simbolik reaksi kimia dengan menggunakan rumus kimia dari zat-zat yang terlibat. Agar sah secara hukum kekekalan massa, persamaan ini harus setara, yaitu jumlah atom untuk setiap unsur harus sama di kedua sisi reaksi.

    ⚛ *Contoh Persamaan Setara:*
    \[ 2H_2 + O_2 \\rightarrow 2H_2O \]

    Jenis reaksi kimia umum meliputi:
    
    - Reaksi Kombinasi (Sintesis) 🧩
    - Reaksi Penguraian (Dekomposisi) ⚡
    - Reaksi Pergantian Tunggal 🔁
    - Reaksi Pergantian Ganda 🔄
    - Reaksi Pembakaran 🔥

    Aplikasi ini membantu menyusun reaksi antara dua unsur dan menampilkan:
    - Persamaan reaksi setara ⚖
    - Jenis reaksi ⚗
    - Berat molekul (BM) dari senyawa hasil reaksi dalam satuan *g/mol* 

    Silakan pilih menu di sebelah kiri untuk memilih 2 unsur yang ingin direaksikan dari tabel periodik.
    """)

# Halaman 2: Tabel Periodik
elif "🧪 Tabel Periodik" in halaman:
    st.header("🔬 Tabel Periodik Unsur")

    gol_filter = st.selectbox(
        "Filter Unsur berdasarkan Golongan",
        ["Semua"] + sorted(set(e["golongan"] for e in Ar_tiap_unsur.values() if "golongan" in e))
    )

    tampilkan_tabel_periodik(
        filter_golongan=gol_filter if gol_filter != "Semua" else None
    )

    if st.session_state.hasil_reaksi:
        st.markdown("---")
        st.subheader("Hasil Reaksi:")
        st.success(st.session_state.hasil_reaksi)
        st.info(f"Jenis reaksi: {st.session_state.jenis_reaksi}")
        st.info(f"Massa molekul senyawa: {st.session_state.massa_molekul}")

    elif st.session_state.error:
        st.markdown("---")
        st.subheader("Hasil Reaksi:")
        st.error(st.session_state.error)

# Halaman 3: Reaksi Kimia
elif "🧮 Reaksi Kimia" in halaman:
    st.header("🧮 Menyusun Reaksi Kimia")

    unsur1 = st.selectbox("Pilih Unsur Pertama", sorted(Ar_tiap_unsur.keys()))
    unsur2 = st.selectbox("Pilih Unsur Kedua", sorted(Ar_tiap_unsur.keys()))

    if st.button("Susun Reaksi"):
        hasil = proses_reaksi(unsur1, unsur2)

        st.session_state.hasil_reaksi = hasil.get("reaksi", "")
        st.session_state.jenis_reaksi = hasil.get("jenis_reaksi", "")
        st.session_state.massa_molekul = hasil.get("massa_molekul", "")
        st.session_state.error = hasil.get("error", "")

    if st.session_state.hasil_reaksi:
        st.markdown("---")
        st.subheader("Hasil Reaksi:")
        st.success(st.session_state.hasil_reaksi)
        st.info(f"Jenis reaksi: {st.session_state.jenis_reaksi}")
        st.info(f"Massa molekul senyawa: {st.session_state.massa_molekul}")

    elif st.session_state.error:
        st.markdown("---")
        st.subheader("Hasil Reaksi:")
        st.error(st.session_state.error)
