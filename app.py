import streamlit as st
from reaction_engine import susun_reaksi_dari_unsur, susun_reaksi_dari_senyawa
from periodic_table_ui import tampilkan_tabel_periodik

st.set_page_config(page_title="Penyusun Persamaan Reaksi", layout="wide")
st.title("\ud83d\udd2c Penyusun Persamaan Reaksi Kimia")

# Inisialisasi session state jika belum ada
if "selected_elements" not in st.session_state:
    st.session_state.selected_elements = []

mode = st.radio("Pilih mode penyusunan reaksi:", ["\ud83d\udd2c Dari Tabel Periodik", "\ud83e\uddea Dari Nama Senyawa"])

if mode == "\ud83d\udd2c Dari Tabel Periodik":
    st.subheader("Mode: Susun Reaksi dari Tabel Periodik")
    st.caption("Klik dua unsur dari tabel periodik di bawah untuk membentuk reaksi.")
    tampilkan_tabel_periodik()

    if st.button("\ud83d\udd01 Reset Pilihan Unsur"):
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

elif mode == "\ud83e\uddea Dari Nama Senyawa":
    st.subheader("Mode: Susun Reaksi dari Nama Senyawa")
    st.caption("Contoh: NaOH + HCl \u2192 NaCl + H\u2082O")

    reaktan = st.text_input("Masukkan reaktan (misal: NaOH + HCl):")
    produk = st.text_input("Masukkan produk (misal: NaCl + H\u2082O):")

    if reaktan and produk:
        hasil = susun_reaksi_dari_senyawa(reaktan + " \u2192 " + produk)
    else:
        hasil = None

    if hasil:
        st.markdown("### Persamaan Reaksi:")
        if hasil.get("setara"):
            st.latex(hasil["setara"])
        if hasil.get("jenis"):
            st.success(f"Jenis Reaksi: {hasil['jenis']}")
