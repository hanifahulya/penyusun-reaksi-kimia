
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
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []
    if "clicked" not in st.session_state:
        st.session_state.clicked = None

    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")

            if simbol and (filter_golongan is None or golongan == filter_golongan):
                Ar = Ar_tiap_unsur.get(simbol, "")
                warna = warna_golongan.get(golongan, "#FFFFFF") if dengan_warna else "#FFFFFF"
                tombol_id = f"{simbol}_{i}"

                is_selected = simbol in st.session_state.selected_elements
                border = "2px solid black" if is_selected else "1px solid #ccc"

                tombol_html = f'''
                <form action="" method="post">
                    <button name="clicked" value="{simbol}"
                            style="
                                background-color:{warna};
                                border:{border};
                                border-radius:6px;
                                width:100%;
                                height:40px;
                                font-weight:bold;
                                cursor:pointer;"
                            title="{simbol} (Ar = {Ar})">
                        {simbol}
                    </button>
                </form>
                '''
                kolom[i].markdown(tombol_html, unsafe_allow_html=True)
            else:
                kolom[i].markdown(" ")

    if st.session_state.clicked:
        simbol = st.session_state.clicked
        if simbol not in st.session_state.selected_elements:
            if len(st.session_state.selected_elements) < 2:
                st.session_state.selected_elements.append(simbol)
        st.session_state.clicked = None
