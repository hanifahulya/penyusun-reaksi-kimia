import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import proses_reaksi

st.set_page_config(page_title="Penyusun Persamaan Reaksi Kimia", layout="wide")

# Navigasi Halaman
halaman = st.sidebar.selectbox("Navigasi", ["Dasar Teori", "Tabel Periodik"])

if halaman == "Dasar Teori":
    st.title("🧪 Penyusun Persamaan Reaksi Kimia")
    st.markdown("""
    Aplikasi ini membantu menyusun persamaan reaksi kimia secara otomatis.  
    Klik dua unsur dari tabel periodik untuk melihat reaksi yang terjadi.  
    """)
elif halaman == "Tabel Periodik":
    st.title("🧪 Penyusun Persamaan Reaksi Kimia")
    st.header("📖 Tabel Periodik Unsur")
    gol_filter = st.selectbox("Filter Unsur berdasarkan Golongan",
                              options=["Semua", "logam alkali", "logam alkali tanah", "logam transisi",
                                       "logam pasca transisi", "metaloid", "nonlogam", "halogen",
                                       "gas mulia", "lanthanida", "aktinida"])
    filter_golongan = gol_filter if gol_filter != "Semua" else None
    tampilkan_tabel_periodik(filter_golongan=filter_golongan, dengan_warna=True)

    # Tampilkan hasil reaksi jika 2 unsur dipilih
    if "selected_elements" in st.session_state and len(st.session_state.selected_elements) == 2:
        unsur1, unsur2 = st.session_state.selected_elements
        st.subheader(f"🧪 Hasil Reaksi: {unsur1} + {unsur2}")
        hasil = proses_reaksi(unsur1, unsur2)
        if hasil:
            st.success(f"**Reaksi:** {hasil['reaksi']}")
            st.info(f"**Jenis Reaksi:** {hasil['jenis']}")
            st.write(f"**Berat Molekul (BM):** {hasil['bm']} g/mol")
        else:
            st.warning("Tidak ditemukan reaksi yang sesuai antara kedua unsur tersebut.")