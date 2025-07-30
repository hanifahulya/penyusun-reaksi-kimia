import streamlit as st
from periodic_table_ui import tampilkan_tabel_periodik
from reaction_engine import susun_reaksi_dari_unsur as susun_reaksi_, hitung_massa_molekul
from utils.tabel_periodik_118 import elemen_periodik

# State
if "elemen_terpilih" not in st.session_state:
    st.session_state.elemen_terpilih = []

def reset_elemen():
    st.session_state.elemen_terpilih = []

# Navigasi halaman
st.sidebar.markdown("### 📘 Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["Dasar Teori", "Tabel Periodik", "Tentang Aplikasi"])

if halaman == "Dasar Teori":
    st.title("🧪 Penyusun Persamaan Reaksi Kimia")
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

elif halaman == "Tabel Periodik":
    st.title("🔬 Tabel Periodik Unsur")

    tampilkan_tabel_periodik(
        elemen_periodik,
        
        elemen_terpilih=st.session_state.elemen_terpilih,
        callback=reset_elemen
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

elif halaman == "Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
    ### 📚 Cara Kerja:
    1. Pilih dua unsur dari tabel periodik.
    2. Aplikasi akan menampilkan:
       - Persamaan reaksi jika tersedia.
       - Jenis reaksi (tunggal/opsional).
       - Massa molekul senyawa hasil reaksi.

    ### 🎯 Tujuan:
    Membantu memahami bagaimana unsur-unsur bereaksi satu sama lain serta menghitung massa molekul hasil reaksi.
    """)
