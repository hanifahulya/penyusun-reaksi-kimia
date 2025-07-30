import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from utils.tabel_periodik_118 import Ar_tiap_unsur

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")
st.title("🧪 Penyusun Persamaan Reaksi Kimia")

st.sidebar.markdown("### 🧭 Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["📖 Dasar Teori", "🔬 Tabel Periodik"], label_visibility="collapsed")

if halaman == "📖 Dasar Teori":
    st.header("📘 Dasar Teori")
    st.markdown(
        """
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
        """
    )

elif halaman == "🔬 Tabel Periodik":
    st.header("🔬 Tabel Periodik Unsur")

    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    filter_gol = st.selectbox("Filter Unsur berdasarkan Golongan", ["Semua"] + sorted(set(e["golongan"] for e in Ar_tiap_unsur.values() if "golongan" in e)))
    filter_gol = None if filter_gol == "Semua" else filter_gol

    tampilkan_tabel_periodik(filter_golongan=filter_gol, dengan_warna=True)

    if len(st.session_state.selected_elements) == 2:
        unsur1, unsur2 = st.session_state.selected_elements
        st.markdown("### ⚗️ Hasil Reaksi")

        hasil = susun_reaksi_dari_unsur(unsur1, unsur2)
        if hasil:
            st.success(hasil)
            bm = hitung_massa_molekul(hasil)
            st.markdown(f"**BM (Berat Molekul):** {bm}")
        else:
            st.warning("Tidak ditemukan reaksi antara kedua unsur tersebut.")

        if st.button("🔄 Reset"):
            st.session_state.selected_elements = []
