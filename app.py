import streamlit as st
from reaction_engine import susun_reaksi_dari_unsur, hitung_massa_molekul
from periodic_table_ui import tampilkan_tabel_periodik
from utils.tabel_periodik_118 import elemen_periodik

st.set_page_config(page_title="Penyusun Persamaan Reaksi", layout="wide")
st.title("Penyusun Persamaan Reaksi Kimia")

if "selected_elements" not in st.session_state:
    st.session_state.selected_elements = []

golongan_tersedia = list({elemen.get("golongan", "lainnya") for baris in elemen_periodik for elemen in baris if elemen.get("simbol")})
golongan_tersedia.sort()
gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan", ["Semua"] + golongan_tersedia)

tampilkan_tabel_periodik(filter_golongan=gol_filter if gol_filter != "Semua" else None)

if st.button("Reset Pilihan Unsur"):
    st.session_state.selected_elements = []

unsur_terpilih = st.session_state.get("selected_elements", [])
if len(unsur_terpilih) == 2:
    hasil = susun_reaksi_dari_unsur(unsur_terpilih)
else:
    hasil = None

if hasil:
    if hasil.get("setara") == "Reaksi tidak ditemukan":
        st.warning("Reaksi antara unsur yang dipilih belum tersedia.")
    else:
        st.markdown("### Persamaan Reaksi:")
        if hasil.get("setara"):
            st.latex(hasil["setara"])
        elif hasil.get("setara_opsi"):
            for opsi in hasil["setara_opsi"]:
                st.latex(opsi)

        if hasil.get("jenis"):
            st.success(f"Jenis Reaksi: {hasil['jenis']}")

        produk_akhir = hasil.get("produk") or (hasil.get("produk_opsional") or [None])[0]
        produk_latex = hasil.get("produk_latex") or (hasil.get("produk_latex_opsi") or [None])[0]

        if produk_akhir and produk_akhir != "Tidak diketahui":
            mr = hitung_massa_molekul(produk_akhir)
            if mr:
                st.info(f"Massa molekul relatif (Mr) dari {produk_latex}: {mr:.2f}")


def halaman_dasar_teori():
    st.markdown("## 📚 Dasar Teori")
    st.markdown("""
    Penyusunan persamaan reaksi kimia merupakan langkah penting dalam memahami konsep stoikiometri dan hukum kekekalan massa. Dalam proses ini, jumlah atom dari masing-masing unsur harus seimbang antara pereaksi dan hasil reaksi. Aplikasi ini membantu proses tersebut dengan cara interaktif dan otomatis menggunakan Python.

    ### Prinsip Dasar Penyusunan Reaksi
    - Berdasarkan hukum kekekalan massa (Lavoisier): massa zat sebelum dan sesudah reaksi harus sama.
    - Stoikiometri digunakan untuk menentukan perbandingan koefisien antara pereaksi dan produk.
    - Informasi massa atom relatif (Ar) digunakan dalam perhitungan massa molekul relatif (Mr).

    Aplikasi ini dirancang untuk membantu menyetarakan reaksi kimia dasar menggunakan antarmuka tabel periodik interaktif.
    """)

