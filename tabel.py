import streamlit as st
from utils.tabel_periodik_118.data import elemen_periodik

def warna_golongan(golongan):
    warna = {
        "nonlogam": "#ff9999",
        "logam": "#9999ff",
        "logam transisi": "#99ff99",
        "halogen": "#ffff99"
    }
    return warna.get(golongan, "#ffffff")

def tampilkan_tabel_periodik():
    st.markdown("### Filter Unsur berdasarkan Golongan")
    pilihan = st.selectbox("Pilih Golongan", ["Semua"] + sorted(set([e["golongan"] for e in elemen_periodik])))
    kolom = st.columns(10)
    for i, elemen in enumerate(elemen_periodik):
        if pilihan == "Semua" or elemen["golongan"] == pilihan:
            warna = warna_golongan(elemen["golongan"])
            with kolom[i % 10]:
                st.button(elemen["simbol"], key=elemen["simbol"], help=elemen["nama"], args=None, kwargs=None, type="secondary")