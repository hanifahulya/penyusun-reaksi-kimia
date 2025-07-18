import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from utils.tabel_periodik_118 import massa_atom, elemen_periodik

st.set_page_config(page_title="Penyusun Reaksi Kimia", layout="wide")

st.title("🧪 Penyusun Persamaan Reaksi Kimia")

st.markdown("### Filter Unsur berdasarkan Golongan")
golongan_opsi = [
    "Semua", "alkali", "alkali tanah", "logam transisi", "metaloid", "nonlogam",
    "halogen", "gas mulia", "lantanida", "aktinida"
]
gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan", golongan_opsi)

# tampilkan tabel periodik dengan filter golongan jika dipilih
tampilkan_tabel_periodik(filter_golongan=None if gol_filter == "Semua" else gol_filter)

st.markdown("---")
st.markdown("### Persamaan Reaksi:")

# Tampilkan hasil reaksi jika ada 2 unsur dipilih
if "selected_elements" in st.session_state and len(st.session_state.selected_elements) == 2:
    unsur1, unsur2 = st.session_state.selected_elements
    persamaan, jenis_reaksi = susun_reaksi_dari_unsur(unsur1, unsur2)
    st.latex(persamaan)
    st.success(f"Jenis Reaksi: {jenis_reaksi}")

    massa = hitung_massa_molekul(persamaan, massa_atom)
    st.info(f"Massa Molekul Relatif (Mr) dari produk: {massa}")

    if st.button("Reset Pilihan Unsur"):
        st.session_state.selected_elements = []
else:
    st.warning("Pilih dua unsur dari tabel periodik untuk menyusun reaksi.")
