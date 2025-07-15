import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik

# Warna golongan untuk styling
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

# Fungsi untuk menampilkan tabel periodik interaktif
def tampilkan_tabel_periodik():
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            if "simbol" in elemen and elemen["simbol"]:
                warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#EEE")
                if kolom[i].button(elemen["simbol"], key=f"btn_{elemen['simbol']}"):
                    if len(st.session_state.selected_elements) < 2 and elemen["simbol"] not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(elemen["simbol"])
                with kolom[i]:
                    st.markdown(
                        f"<div style='background-color:{warna};width:100%;text-align:center;border-radius:6px;padding:4px;color:black'><b>{elemen['simbol']}</b></div>",
                        unsafe_allow_html=True
                    )
            else:
                kolom[i].markdown(" ")
