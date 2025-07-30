import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from utils.tabel_periodik_118 import Ar_tiap_unsur
import streamlit.components.v1 as components

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")

st.title("🧪 Penyusun Persamaan Reaksi Kimia")

halaman = st.sidebar.markdown("### 📌 Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["📘 Dasar Teori", "🔬 Tabel Periodik"], label_visibility="collapsed")

# 👇 Tangani klik dari komponen HTML
clicked_data = st.experimental_get_query_params().get("unsur", [])
if clicked_data:
    simbol = clicked_data[0]
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []
    if simbol not in st.session_state.selected_elements and len(st.session_state.selected_elements) < 2:
        st.session_state.selected_elements.append(simbol)
    st.experimental_set_query_params()  # Reset query

# =======================
# Halaman 1: Dasar Teori
# =======================
if "Dasar Teori" in halaman:
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

# ============================
# Halaman 2: Tabel Periodik
# ============================
elif "Tabel Periodik" in halaman:
    st.header("🔬 Tabel Periodik Unsur")

    gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan", 
                              options=["Semua", "logam alkali", "logam alkali tanah", "logam transisi", 
                                       "logam pasca transisi", "metaloid", "nonlogam", "halogen", 
                                       "gas mulia", "lanthanida", "aktinida"])

    tampilkan_tabel_periodik(
        filter_golongan=gol_filter if gol_filter != "Semua" else None,
        dengan_warna=True
    )

    if "selected_elements" in st.session_state and len(st.session_state.selected_elements) == 2:
        unsur1, unsur2 = st.session_state.selected_elements
        st.subheader(f"🔍 Hasil Reaksi: {unsur1} + {unsur2}")
        hasil = susun_reaksi_dari_unsur([unsur1, unsur2])

        if hasil:
            st.subheader("📄 Persamaan Reaksi:")
            st.latex(hasil.get("setara", hasil.get("setara_opsi", ["?"])[0]))
            st.success(f"Jenis Reaksi: {hasil.get('jenis', 'Tidak diketahui')}")

            produk = hasil.get("produk", hasil.get("produk_opsional", ["?"])[0])
            bm = hitung_massa_molekul(produk)
            if bm:
                st.info(f"Massa molekul relatif (Mr) dari {produk}: {round(bm, 2)} g/mol")
            else:
                st.warning("Tidak ditemukan reaksi yang cocok antara kedua unsur ini.")
        else:
            st.warning("Tidak ada reaksi yang dikenali.")

        if st.button("🔁 Reset Pilihan"):
            st.session_state.selected_elements = []
