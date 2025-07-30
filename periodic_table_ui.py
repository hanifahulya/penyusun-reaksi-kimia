import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, warna_golongan

def tampilkan_tabel_periodik(filter_golongan=None, dengan_warna=True):
    st.markdown("<style>div.stButton > button { width: 3em; height: 3em; }</style>", unsafe_allow_html=True)

    selected_elements = st.session_state.get("selected_elements", [])

    grid = [[None for _ in range(18)] for _ in range(10)]  # Baris x Kolom

    # Masukkan elemen ke grid sesuai posisinya
    for el in elemen_periodik:
        if filter_golongan and el['golongan'] != filter_golongan:
            continue
        row, col = el["row"] - 1, el["column"] - 1
        grid[row][col] = el

    for row in grid:
        cols = st.columns(18)
        for i, el in enumerate(row):
            if el:
                simbol = el["simbol"]
                warna = warna_golongan.get(el["golongan"], "#FFFFFF") if dengan_warna else "#FFFFFF"
                if cols[i].button(simbol, key=f"{simbol}_{i}"):
                    if simbol not in selected_elements:
                        selected_elements.append(simbol)
                        if len(selected_elements) > 2:
                            selected_elements = selected_elements[-2:]
                    st.session_state.selected_elements = selected_elements
            else:
                cols[i].empty()
