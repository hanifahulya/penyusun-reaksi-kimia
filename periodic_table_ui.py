import streamlit as st
from tabel_periodik_118 import elemen_periodik, warna_golongan

def tampilkan_tabel_periodik(filter_golongan=None, dengan_warna=False):
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    def klik_unsur(symbol):
        if symbol in st.session_state.selected_elements:
            st.session_state.selected_elements.remove(symbol)
        elif len(st.session_state.selected_elements) < 2:
            st.session_state.selected_elements.append(symbol)

    last_row = -1
    for elemen in elemen_periodik:
        simbol = elemen["simbol"]
        golongan = elemen["golongan"]
        row = elemen["baris"]
        col = elemen["kolom"]

        if filter_golongan and golongan != filter_golongan:
            continue

        if row != last_row:
            if last_row != -1:
                st.write("")
            cols = st.columns(18)
            last_row = row

        warna = warna_golongan.get(golongan, "#FFFFFF") if dengan_warna else "#FFFFFF"
        idx = (col - 1) if 0 < col <= 18 else 0
        if 0 <= idx < len(cols):
            cols[idx].button(simbol, key=simbol, on_click=klik_unsur, args=(simbol,), help=golongan, use_container_width=True)