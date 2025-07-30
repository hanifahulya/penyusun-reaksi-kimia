
import streamlit as st
from streamlit.components.v1 import html
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
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    html_content = """
    <style>
        .unsur-grid {
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            gap: 6px;
        }
        .unsur-button {
            padding: 8px;
            border-radius: 6px;
            font-weight: bold;
            text-align: center;
            cursor: pointer;
            border: 1px solid #aaa;
        }
    </style>
    <div class='unsur-grid'>"""

    for baris in elemen_periodik:
        for elemen in baris:
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")
            if simbol:
                if filter_golongan is None or golongan == filter_golongan:
                    warna = warna_golongan.get(golongan, "#FFFFFF")
                    html_content += f"""
                    <div class='unsur-button' style='background-color:{warna}'
                         onclick="window.parent.postMessage('{simbol}', '*')">
                        {simbol}
                    </div>"""
                else:
                    html_content += "<div></div>"
            else:
                html_content += "<div></div>"

    html_content += "</div>"

    html(html_content, height=700)

    # Tangkap pesan dari JS dan simpan ke session_state (dilakukan di app.py listener)
