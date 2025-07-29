import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik

def tampilkan_tabel_periodik():
    kelompok = {
        "logam alkali": ["Li", "Na", "K", "Rb", "Cs", "Fr"],
        "logam alkali tanah": ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"],
        "halogen": ["F", "Cl", "Br", "I", "At", "Ts"],
        "gas mulia": ["He", "Ne", "Ar", "Kr", "Xe", "Rn", "Og"]
    }

    warna = {
        "logam alkali": "#FFB6C1",
        "logam alkali tanah": "#87CEFA",
        "halogen": "#90EE90",
        "gas mulia": "#FFD700"
    }

    for i in range(0, len(elemen_periodik), 10):
        kolom = st.columns(10)
        for j in range(10):
            if i + j < len(elemen_periodik):
                e = elemen_periodik[i + j]
                warna_bg = ""
                for kategori, elemen in kelompok.items():
                    if e in elemen:
                        warna_bg = warna[kategori]
                        break
                kolom[j].button(e, key=e, help=f"Unsur: {e}", use_container_width=True)
