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
    - Persamaan reaksi setara
    - Jenis reaksi ⚗️
    - Berat molekul (BM) dari senyawa hasil reaksi dalam satuan **g/mol** ⚖️
    """)

elif halaman == "Tabel Periodik":
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
        hasil = proses_reaksi(unsur1, unsur2)
        if hasil:
            st.success(f"**Reaksi:** {hasil['reaksi']}")
            st.info(f"**Jenis Reaksi:** {hasil['jenis']}")
            st.write(f"**Berat Molekul (BM):** {hasil['bm']} g/mol")
        else:
            st.warning("Tidak ditemukan reaksi yang cocok antara kedua unsur ini.")
        if st.button("🔁 Reset Pilihan"):
            st.session_state.selected_elements = []



streamlit as st
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui import tampilkan_tabel_periodik
from utils.tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title="Penyusun Persamaan Reaksi", layout="wide")
st.title("🧪 Penyusun Persamaan Reaksi Kimia")

halaman = st.sidebar.selectbox("Navigasi", ["Dasar Teori", "Tabel Periodik"])

if halaman == "Dasar Teori":
    st.header("📚 Dasar Teori")
    st.markdown("""
    Reaksi kimia adalah proses di mana satu atau lebih zat (reaktan) diubah menjadi satu atau lebih zat baru (produk). Dalam reaksi kimia, atom-atom disusun ulang, tetapi tidak diciptakan atau dimusnahkan.

    Persamaan reaksi kimia menyatakan secara simbolik reaksi kimia dengan menggunakan rumus kimia dari zat-zat yang terlibat. Agar sah secara hukum kekekalan massa, persamaan ini harus setara, yaitu jumlah atom untuk setiap unsur harus sama di kedua sisi reaksi.

    ⚛️ **Contoh Persamaan Setara:**
    \[ 2H_2 + O_2 \rightarrow 2H_2O \]

    Aplikasi ini membantu menyusun reaksi antara dua unsur dan menampilkan:
    - Persamaan reaksi setara
    - Jenis reaksi ⚗️
    - Berat molekul (BM) dari senyawa hasil reaksi dalam satuan **g/mol** ⚖️
    """)

elif halaman == "Tabel Periodik":
    st.header("🔬 Tabel Periodik Unsur")

    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    golongan_tersedia = list({elemen.get("golongan", "lainnya") for baris in elemen_periodik for elemen in baris if elemen.get("simbol")})
    golongan_tersedia.sort()
    gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan", ["Semua"] + golongan_tersedia)

    tampilkan_tabel_periodik(filter_golongan=gol_filter if gol_filter != "Semua" else None, dengan_warna=True)

    if st.button("🔁 Reset Pilihan Unsur"):
        st.session_state.selected_elements = []

    unsur_terpilih = st.session_state.get("selected_elements", [])
    if len(unsur_terpilih) == 2:
        hasil = susun_reaksi_dari_unsur(unsur_terpilih)
    else:
        hasil = None

    if hasil:
        if hasil.get("setara") == "Reaksi tidak ditemukan":
            st.warning("⚠️ Reaksi antara unsur yang dipilih belum tersedia.")
        else:
            st.markdown("### 🔍 Persamaan Reaksi:")
            if hasil.get("setara"):
                st.latex(hasil["setara"])
            elif hasil.get("setara_opsi"):
                for opsi in hasil["setara_opsi"]:
                    st.latex(opsi)

            if hasil.get("jenis"):
                st.success(f"Jenis Reaksi ⚗️: {hasil['jenis']}")

            produk_akhir = hasil.get("produk") or (hasil.get("produk_opsional") or [None])[0]
            produk_latex = hasil.get("produk_latex") or (hasil.get("produk_latex_opsi") or [None])[0]

            if produk_akhir and produk_akhir != "Tidak diketahui":
                mr = hitung_massa_molekul(produk_akhir)
                if mr:
                    st.info(f"BM dari {produk_latex} = {mr:.2f} g/mol ⚖️")
