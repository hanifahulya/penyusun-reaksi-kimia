import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik

warna_golongan = {
    "logam alkali": "#FFB3BA",
    "logam alkali tanah": "#FFDFBA",
    "logam transisi": "#FFFFBA",
    "logam pasca transisi": "#FFE0AC",
    "metaloid": "#BAFFC9",
    "nonlogam": "#BAE1FF",
    "halogen": "#D5BAFF",
    "gas mulia": "#FFBAED",
    "lanthanida": "#C2F0FC",
    "aktinida": "#E6CCFF",
    "lainnya": "#E0E0E0"
}

def tampilkan_tabel_periodik():
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            if "simbol" in elemen and elemen["simbol"]:
                warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#E0E0E0")
                simbol = elemen["simbol"]

                if kolom[i].button(simbol, key=f"{simbol}-{i}", help=elemen["golongan"]):
                    if simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)

                    # Batasi hanya 2 unsur
                    if len(st.session_state.selected_elements) > 2:
                        st.session_state.selected_elements = st.session_state.selected_elements[-2:]
            else:
                kolom[i].empty()

    st.markdown("**Unsur Terpilih:** " + ", ".join(st.session_state.selected_elements))
