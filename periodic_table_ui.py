import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik

warna_golongan = {
    "logam alkali": "#FFB3BA",
    "logam alkali tanah": "#FFDFBA",
    "logam transisi": "#FFFFBA",
    "logam pasca transisi": "#FFE4B5",
    "metaloid": "#BAFFC9",
    "nonlogam": "#BAE1FF",
    "halogen": "#D5BAFF",
    "gas mulia": "#FFBAED",
    "lanthanida": "#C2F0FC",
    "aktinida": "#E6CCFF",
    "lainnya": "#E0E0E0"
}

def tampilkan_tabel_periodik():
    for baris_index, baris in enumerate(elemen_periodik):
        kolom = st.columns(18)
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")
            warna = warna_golongan.get(golongan, "#E0E0E0")

            if simbol:
                tombol_diklik = kolom[i].button(
                    simbol,
                    key=f"btn-{baris_index}-{i}",
                    help=golongan
                )
                if tombol_diklik:
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)
            else:
                kolom[i].markdown(" ")
