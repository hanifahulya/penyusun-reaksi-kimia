import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, warna_golongan

def tampilkan_tabel_periodik():
    selected_golongan = st.selectbox("Filter golongan (opsional)", ["Semua"] + list(warna_golongan.keys()))

    for baris in elemen_periodik:
        kolom_html = ""
        for elemen in baris:
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "")
            if simbol:
                if selected_golongan != "Semua" and golongan != selected_golongan:
                    continue
                warna = warna_golongan.get(golongan, "#EEE")
                kolom_html += f"""
                <button class="unsur-btn" onclick="fetch('/?element={simbol}')"
                style="background-color:{warna};width:50px;height:50px;margin:1px;border-radius:6px;font-weight:bold;">
                {simbol}</button>"""
            else:
                kolom_html += '<div style="width:50px;height:50px;margin:1px;"></div>'
        st.markdown(f"<div style='display:flex;flex-wrap:wrap'>{kolom_html}</div>", unsafe_allow_html=True)

    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    for baris in elemen_periodik:
        for elemen in baris:
            simbol = elemen.get("simbol")
            if simbol and st.button(simbol, key=f"btn_{simbol}"):
                if simbol not in st.session_state.selected_elements and len(st.session_state.selected_elements) < 2:
                    st.session_state.selected_elements.append(simbol)
