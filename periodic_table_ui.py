import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, warna_golongan

def tampilkan_tabel_periodik():
    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for idx, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "")
            warna = warna_golongan.get(golongan, "#FFFFFF")

            if simbol:
                if kolom[idx].button(simbol, key=f"{simbol}_{idx}", help=f"{simbol} - {golongan}", use_container_width=True):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2:
                        st.session_state.selected_elements.append(simbol)
            else:
                # Tampilkan tombol kosong agar grid tetap terjaga
                kolom[idx].markdown(f"<div style='height: 2.5em; background-color: white;'></div>", unsafe_allow_html=True)
