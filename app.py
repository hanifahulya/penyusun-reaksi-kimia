import streamlit as st
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui import tampilkan_tabel_periodik

st.set_page_config(page_title="Penyusun Persamaan Reaksi", layout="wide")
st.title("🔬 Penyusun Persamaan Reaksi Kimia")

if "selected_elements" not in st.session_state:
    st.session_state.selected_elements = []

st.subheader("Mode: Susun Reaksi dari Tabel Periodik")
st.caption("Klik dua unsur dari tabel periodik di bawah untuk membentuk reaksi.")
tampilkan_tabel_periodik()

if st.button("🔁 Reset Pilihan Unsur"):
    st.session_state.selected_elements = []

unsur_terpilih = st.session_state.get("selected_elements", [])
if len(unsur_terpilih) == 2:
    hasil = susun_reaksi_dari_unsur(unsur_terpilih)
else:
    hasil = None

if hasil:
    st.markdown("### Persamaan Reaksi:")
    if hasil.get("setara"):
        st.latex(hasil["setara"])
    elif hasil.get("setara_opsi"):
        for opsi in hasil["setara_opsi"]:
            st.latex(opsi)

    if hasil.get("jenis"):
        st.success(f"Jenis Reaksi: {hasil['jenis']}")

    if hasil.get("produk") or hasil.get("produk_opsional"):
        produk_akhir = hasil.get("produk") if hasil.get("produk") else hasil.get("produk_opsional")[0]
        mr = hitung_massa_molekul(produk_akhir)
        if mr:
            st.info(f"Massa molekul relatif (Mr) dari {produk_akhir}: {mr:.2f}")
