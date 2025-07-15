import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik

# Warna untuk golongan unsur
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

# CSS agar tombol terlihat rapi
def inject_css():
    st.markdown("""
        <style>
        .unsur-grid {
            display: grid;
            grid-template-columns: repeat(18, 50px);
            gap: 2px;
        }
        .unsur-button {
            width: 48px;
            height: 48px;
            border: none;
            font-weight: bold;
            border-radius: 6px;
            font-size: 14px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

# Tampilkan tabel periodik interaktif
def tampilkan_tabel_periodik():
    inject_css()
    st.markdown('<div class="unsur-grid">', unsafe_allow_html=True)

    for baris in elemen_periodik:
        for elemen in baris:
            simbol = elemen.get("simbol", "")
            warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#E0E0E0")

            if simbol:
                key = f"btn-{simbol}-{warna}"
                if st.button(simbol, key=key):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)

            else:
                # Tambahkan div kosong untuk posisi kosong
                st.markdown('<div style="width: 50px; height: 48px;"></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
