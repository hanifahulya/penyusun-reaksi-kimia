
import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, Ar_tiap_unsur

emoji_golongan = {
    "logam alkali": "🟥",
    "logam alkali tanah": "🟨",
    "logam transisi": "🟩",
    "logam pasca transisi": "🟪",
    "metaloid": "🟧",
    "nonlogam": "🟦",
    "halogen": "🟫",
    "gas mulia": "⬜",
    "lanthanida": "⬛",
    "aktinida": "🔲",
    "lainnya": "⬛"
}

def tampilkan_tabel_periodik(filter_golongan=None, dengan_warna=False):
    if "selected_elements" not in st.session_state:
        st.session_state.selected_elements = []

    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")

            if simbol and (filter_golongan is None or golongan == filter_golongan):
                Ar = Ar_tiap_unsur.get(simbol, "")
                warna_emoji = emoji_golongan.get(golongan, "") if dengan_warna else ""
                label = f"{warna_emoji} {simbol}"

                if kolom[i].button(label, key=f"{simbol}_{i}", help=f"{simbol} (Ar = {Ar})", use_container_width=True):
                    if simbol not in st.session_state.selected_elements:
                        if len(st.session_state.selected_elements) < 2:
                            st.session_state.selected_elements.append(simbol)
            else:
                kolom[i].markdown(" ")
