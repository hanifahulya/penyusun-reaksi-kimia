import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, Ar_tiap_unsur


def tampilkan_tabel_periodik(filter_golongan=None):
    for baris in elemen_periodik:
        kolom = st.columns(len(baris))
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")
