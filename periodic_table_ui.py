import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik

warna_golongan = {
    "logam alkali": "#FFB3BA",
    "logam alkali tanah": "#FFDFBA",
    "logam transisi": "#FFFFBA",
    "metaloid": "#BAFFC9",
    "nonlogam": "#BAE1FF",
    "halogen": "#D5BAFF",
    "gas mulia": "#FFBAED",
    "lanthanida": "#C2F0FC",
    "aktinida": "#E6CCFF",
    "logam pasca transisi": "#E0E0E0",
}

def klik_unsur(simbol):
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []
    if simbol in st.session_state.selected_elements:
        st.session_state.selected_elements.remove(simbol)
    elif len(st.session_state.selected_elements) < 2:
        st.session_state.selected_elements.append(simbol)

def tampilkan_tabel_periodik():
    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            warna = warna_golongan.get(elemen.get("golongan", ""), "#FFFFFF")
            if simbol:
                if kolom[i].button(simbol, key=f"{simbol}_{i}", help=elemen.get("golongan", ""), use_container_width=True):
                    klik_unsur(simbol)
