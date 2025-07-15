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
    st.markdown("""
        <style>
            .unsur-box {
                display: inline-block;
                width: 50px;
                height: 50px;
                line-height: 50px;
                margin: 1px;
                text-align: center;
                font-weight: bold;
                border-radius: 6px;
                font-size: 16px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    for baris in elemen_periodik:
        kolom_html = ""
        for elemen in baris:
            simbol = elemen.get("simbol", "")
            if simbol:
                warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#E0E0E0")
                onclick = f"onClick=\"document.getElementById('{simbol}_btn').click()\""
                kolom_html += f'<div class="unsur-box" style="background-color:{warna};" {onclick}>{simbol}</div>'
            else:
                kolom_html += '<div class="unsur-box" style="background-color:white;"></div>'
        st.markdown(kolom_html, unsafe_allow_html=True)

        for elemen in baris:
            simbol = elemen.get("simbol", "")
            if simbol:
                if st.button(" ", key=f"{simbol}_btn"):
                    if simbol not in st.session_state.selected_elements and len(st.session_state.selected_elements) < 2:
                        st.session_state.selected_elements.append(simbol)
