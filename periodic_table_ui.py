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
            if "simbol" in elemen and elemen["simbol"]:
                warna = warna_golongan.get(elemen.get("golongan", "lainnya"), "#EEE")
                simbol = elemen["simbol"]
                onclick = f"window.parent.postMessage({{'type': 'streamlit:selectElement', 'value': '{simbol}'}}, '*')"
                kolom_html += f'<div class="unsur-box" style="background-color:{warna};" onclick="{onclick}">{simbol}</div>'
            else:
                kolom_html += '<div class="unsur-box" style="background-color:white;"></div>'
        st.markdown(kolom_html, unsafe_allow_html=True)

    # Tangani klik menggunakan JS hack
    st.markdown("""
        <script>
        const doc = window.parent.document;
        window.addEventListener('message', event => {
            if (event.data.type === 'streamlit:selectElement') {
                const value = event.data.value;
                const streamlitEvent = new CustomEvent('streamlit_select_element', { detail: value });
                doc.dispatchEvent(streamlitEvent);
            }
        });
        </script>
    """, unsafe_allow_html=True)

    st.markdown("""<script>
        const doc = window.parent.document;
        doc.addEventListener('streamlit_select_element', e => {
            const value = e.detail;
            const input = doc.querySelector('input[data-testid="stTextInput"]');
            if (window.parent.streamlitComponent) {
                window.parent.streamlitComponent.sendValue(value);
            }
        });
    </script>
    """, unsafe_allow_html=True)

    clicked = st.text_input("Klik dua unsur:", key="unsur_klik")
    if clicked:
        if clicked not in st.session_state.selected_elements:
            st.session_state.selected_elements.append(clicked)
