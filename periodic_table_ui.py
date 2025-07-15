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

    st.write("Klik 2 unsur untuk menyusun reaksi. Maksimal 2 unsur!")

    for baris_idx, baris in enumerate(elemen_periodik):
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            if "simbol" in elemen and elemen["simbol"]:
                simbol = elemen["simbol"]
                warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#CCCCCC")

                with kolom[i]:
                    klik = st.button(
                        simbol,
                        key=f"{simbol}-{baris_idx}-{i}",
                        help=f"{simbol} ({elemen['golongan']})"
                    )
                    if klik:
                        if simbol not in st.session_state.selected_elements:
                            st.session_state.selected_elements.append(simbol)
                        if len(st.session_state.selected_elements) > 2:
                            st.session_state.selected_elements = st.session_state.selected_elements[-2:]
            else:
                with kolom[i]:
                    st.markdown("")

    st.markdown(f"**Unsur Terpilih:** {', '.join(st.session_state.selected_elements)}")
