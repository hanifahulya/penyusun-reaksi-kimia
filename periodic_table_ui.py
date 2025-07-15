import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik

def tampilkan_tabel_periodik():
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            if elemen and "simbol" in elemen and elemen["simbol"]:
                simbol = elemen["simbol"]
                warna = {
                    "logam alkali": "#FFB3BA",
                    "logam alkali tanah": "#FFDFBA",
                    "logam transisi": "#FFFFBA",
                    "logam pasca transisi": "#E6E6FA",
                    "metaloid": "#BAFFC9",
                    "nonlogam": "#BAE1FF",
                    "halogen": "#D5BAFF",
                    "gas mulia": "#FFBAED",
                    "lanthanida": "#C2F0FC",
                    "aktinida": "#E6CCFF"
                }.get(elemen.get("golongan", "lainnya"), "#E0E0E0")

                if kolom[i].button(simbol, key=f"{simbol}_{i}", help=elemen.get("golongan", "")):
                    if simbol not in st.session_state.selected_elements and len(st.session_state.selected_elements) < 2:
                        st.session_state.selected_elements.append(simbol)
            else:
                kolom[i].markdown(" ")  # Placeholder kosong
