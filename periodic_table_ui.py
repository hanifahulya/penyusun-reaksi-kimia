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
                warna = {
    'logam alkali': '#FFC1C1',
    'logam alkali tanah': '#FFDEAD',
    'logam transisi': '#ADD8E6',
    'logam pasca-transisi': '#C1FFC1',
    'metaloid': '#E6E6FA',
    'nonlogam': '#FFFACD',
    'halogen': '#FFD700',
    'gas mulia': '#DDA0DD',
    'lainnya': '#F5F5F5'
}.get(golongan, '#F5F5F5')
label = f"{simbol}"
                tooltip = f"{simbol} (Ar = {Ar})" if Ar else simbol
                st.markdown(
    f"<div style='background-color:{warna}; padding:8px; border-radius:6px; text-align:center;'>"
    f"<strong>{label}</strong></div>",
    unsafe_allow_html=True
)
if kolom[i].button("", help=tooltip, key=f"{simbol}_{i}", use_container_width=True):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)
            else:
                kolom[i].markdown(" ")
