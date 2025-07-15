import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik
from utils.golongan_warna import warna_golongan  # atau langsung dict-nya

def tampilkan_tabel_periodik():
    for i, baris in enumerate(elemen_periodik):
        kolom = st.columns(len(baris))
        for j, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            if simbol:
                warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#E0E0E0")
                if kolom[j].button(simbol, key=f"{i}-{j}", help=elemen["golongan"]):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)
