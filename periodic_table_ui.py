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
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    for baris_index, baris in enumerate(elemen_periodik):
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            if elemen and "simbol" in elemen and elemen["simbol"]:
                simbol = elemen["simbol"]
                warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#E0E0E0")

                button_label = f"**{simbol}**"
                if kolom[i].button(button_label, key=f"{simbol}_{baris_index}_{i}"):
                    if simbol not in st.session_state.selected_elements and len(st.session_state.selected_elements) < 2:
                        st.session_state.selected_elements.append(simbol)

                kolom[i].markdown(
                    f'<div style="text-align:center; background-color:{warna}; border-radius:8px; padding:4px;">{simbol}</div>',
                    unsafe_allow_html=True
                )
            else:
                kolom[i].markdown(" ")
