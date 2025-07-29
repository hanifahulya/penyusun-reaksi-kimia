import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, Ar_tiap_unsur
warna_golongan = {'logam alkali': 'lightcoral', 'logam alkali tanah': 'lightsalmon', 'logam transisi': 'gold', 'logam pasca transisi': 'lightgreen', 'metaloid': 'mediumturquoise', 'nonlogam': 'deepskyblue', 'halogen': 'violet', 'gas mulia': 'plum', 'aktinida': 'salmon', 'lantanida': 'khaki', 'lainnya': 'lightgray'}

def tampilkan_tabel_periodik(filter_golongan=None):
    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")
            if simbol and (filter_golongan is None or golongan == filter_golongan):

            color = warna_golongan.get(golongan, "lightgray")
            st.markdown(f"<div style='text-align:center; background-color:{color}; padding:4px; border-radius:6px'>{label}</div>", unsafe_allow_html=True)

                Ar = Ar_tiap_unsur.get(simbol, "")
                label = f"{simbol}"
                tooltip = f"{simbol} (Ar = {Ar})" if Ar else simbol
                if kolom[i].button(label, help=tooltip, key=f"{simbol}_{i}", use_container_width=True):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)
            else:
                kolom[i].markdown(" ")
