import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import susun_reaksi_dari_unsur as susun_reaksi_, hitung_massa_molekul
from utils.tabel_periodik_118 import elemen_periodik, element_info

# State
if "elemen_terpilih" not in st.session_state:
    st.session_state.elemen_terpilih = []

def reset_elemen():
    st.session_state.elemen_terpilih = []

# Navigasi halaman
st.sidebar.markdown("### 📘 Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["Dasar Teori", "Tabel Periodik"])

if halaman == "Dasar Teori":
    st.title("🧪 Penyusun Persamaan Reaksi Kimia")
    st.markdown("""
    Aplikasi ini membantu menyusun persamaan reaksi kimia otomatis berdasarkan dua unsur yang kamu pilih.

    #### 📚 Cara Kerja:
    1. Pilih dua unsur dari tabel periodik.
    2. Aplikasi akan menampilkan:
       - Persamaan reaksi jika tersedia.
       - Jenis reaksi (tunggal/opsional).
       - Massa molekul senyawa hasil reaksi.

    #### 🎯 Tujuan:
    Membantu memahami bagaimana unsur-unsur bereaksi satu sama lain serta menghitung massa molekul hasil reaksi.

    """)
elif halaman == "Tabel Periodik":
    st.title("🔬 Tabel Periodik Unsur")

    st.markdown("### Filter Unsur berdasarkan Golongan")
    gol_filter = st.selectbox(
        "Pilih Golongan",
        options=["Semua"] + sorted(set(info["golongan"] for info in element_info.values()))
    )

    tampilkan_tabel_periodik(
        elemen_periodik,
        info_unsur=element_info,
        elemen_terpilih=st.session_state.elemen_terpilih,
        callback=reset_elemen,
        filter_golongan=gol_filter if gol_filter != "Semua" else None
    )

    if len(st.session_state.elemen_terpilih) == 2:
        unsur1, unsur2 = st.session_state.elemen_terpilih

        st.markdown("---")
        st.subheader("🔁 Hasil Reaksi Kimia")

        hasil = susun_reaksi_(unsur1, unsur2)

        if hasil:
            for hasil_reaksi in hasil:
                rumus = hasil_reaksi["hasil"]
                jenis = hasil_reaksi["tipe"]
                massa = hitung_massa_molekul(rumus)

                st.markdown(f"""
                ✅ **Reaksi {jenis.capitalize()}:**
                \n**{unsur1} + {unsur2} → {rumus}**
                \n💠 Massa Molekul: **{massa:.2f} g/mol**
                """)
        else:
            st.warning(f"Tidak ditemukan reaksi antara {unsur1} dan {unsur2}.")
    else:
        st.info("Silakan pilih dua unsur untuk melihat hasil reaksi.")
