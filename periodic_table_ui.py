import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, Ar_tiap_unsur

def tampilkan_tabel_periodik(filter_golongan=None):
    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")
            if simbol and (filter_golongan is None or golongan == filter_golongan):
                Ar = Ar_tiap_unsur.get(simbol, "")
                label = f"{simbol}"
    warna_golongan = {
        "logam alkali": "#ff9999",
        "logam alkali tanah": "#ffcc99",
        "logam transisi": "#ffff99",
        "logam pasca transisi": "#ccff99",
        "metaloid": "#99ffcc",
        "nonlogam": "#99ccff",
        "halogen": "#c299ff",
        "gas mulia": "#ffb3e6",
        "lantanida": "#d9d9d9",
        "aktinida": "#b3cccc",
        "lainnya": "#f0f0f0"
    }
    warna = warna_golongan.get(golongan.lower(), warna_golongan["lainnya"])
    tombol_html = f"""<button style='background-color:{warna}; border:none; padding:8px; width:100%;'>{label}</button>"""
    if kolom[i].button(label="", key=f"{simbol}_{i}", help=tooltip, use_container_width=True):
        if "selected_elements" not in st.session_state:
            st.session_state.selected_elements = []
        if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
            st.session_state.selected_elements.append(simbol)
    kolom[i].markdown(tombol_html, unsafe_allow_html=True)
                tooltip = f"{simbol} (Ar = {Ar})" if Ar else simbol
                if kolom[i].button(label, help=tooltip, key=f"{simbol}_{i}", use_container_width=True):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)
            else:
                kolom[i].markdown(" ")
