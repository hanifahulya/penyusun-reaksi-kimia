import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, Ar_tiap_unsur

warna_golongan = {
    "logam alkali": "#FFA07A",
    "logam alkali tanah": "#F0E68C",
    "logam transisi": "#90EE90",
    "logam pasca transisi": "#D8BFD8",
    "metaloid": "#FFB6C1",
    "nonlogam": "#87CEFA",
    "halogen": "#FFDEAD",
    "gas mulia": "#E0FFFF",
    "lanthanida": "#E6E6FA",
    "aktinida": "#FFE4E1",
    "lainnya": "#FFFFFF"
}

def tampilkan_tabel_periodik(filter_golongan=None, dengan_warna=False):
    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")
            if simbol and (filter_golongan is None or golongan == filter_golongan):
                Ar = Ar_tiap_unsur.get(simbol, "")
                tooltip = f"{simbol} (Ar = {Ar})" if Ar else simbol
                warna = warna_golongan.get(golongan, "#FFFFFF") if dengan_warna else "#FFFFFF"

                tombol_html = f"""
                <button style="background-color:{warna};
                               width:100%;
                               height:40px;
                               border:none;
                               border-radius:6px;
                               cursor:pointer;">
                    <strong>{simbol}</strong>
                </button>
                """

                if kolom[i].button(simbol, key=f"{simbol}_{i}", help=tooltip, use_container_width=True):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)
                elif dengan_warna:
                    kolom[i].markdown(tombol_html, unsafe_allow_html=True)
            else:
                kolom[i].markdown(" ")
