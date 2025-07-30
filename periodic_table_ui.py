import streamlit as st
from utils.tabel_periodik_118 import Ar_tiap_unsur, element_info

def tampilkan_tabel_periodik(filter_golongan="Semua", klik_unsur=None):
    st.subheader("🔬 Tabel Periodik Unsur")

    baris_kolom = {
        1: {1: "H", 18: "He"},
        2: {1: "Li", 2: "Be", 13: "B", 14: "C", 15: "N", 16: "O", 17: "F", 18: "Ne"},
        3: {1: "Na", 2: "Mg", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar"},
        4: {1: "K", 2: "Ca", 3: "Sc", 4: "Ti", 5: "V", 6: "Cr", 7: "Mn", 8: "Fe",
            9: "Co", 10: "Ni", 11: "Cu", 12: "Zn", 13: "Ga", 14: "Ge", 15: "As", 16: "Se", 17: "Br", 18: "Kr"},
        5: {1: "Rb", 2: "Sr", 3: "Y", 4: "Zr", 5: "Nb", 6: "Mo", 7: "Tc", 8: "Ru",
            9: "Rh", 10: "Pd", 11: "Ag", 12: "Cd", 13: "In", 14: "Sn", 15: "Sb", 16: "Te", 17: "I", 18: "Xe"},
        6: {1: "Cs", 2: "Ba", 3: "La", 4: "Hf", 5: "Ta", 6: "W", 7: "Re", 8: "Os",
            9: "Ir", 10: "Pt", 11: "Au", 12: "Hg", 13: "Tl", 14: "Pb", 15: "Bi", 16: "Po", 17: "At", 18: "Rn"},
        7: {1: "Fr", 2: "Ra", 3: "Ac", 4: "Rf", 5: "Db", 6: "Sg", 7: "Bh", 8: "Hs",
            9: "Mt", 10: "Ds", 11: "Rg", 12: "Cn", 13: "Nh", 14: "Fl", 15: "Mc", 16: "Lv", 17: "Ts", 18: "Og"},
        8: {4: "Ce", 5: "Pr", 6: "Nd", 7: "Pm", 8: "Sm", 9: "Eu", 10: "Gd", 11: "Tb",
            12: "Dy", 13: "Ho", 14: "Er", 15: "Tm", 16: "Yb", 17: "Lu"},
        9: {4: "Th", 5: "Pa", 6: "U", 7: "Np", 8: "Pu", 9: "Am", 10: "Cm", 11: "Bk",
            12: "Cf", 13: "Es", 14: "Fm", 15: "Md", 16: "No", 17: "Lr"},
    }

    for baris in range(1, 10):
        kolom = st.columns(18)
        for posisi in range(1, 19):
            simbol = baris_kolom.get(baris, {}).get(posisi, "")
            if simbol:
                if filter_golongan != "Semua" and element_info.get(simbol, {}).get("golongan") != filter_golongan:
                    kolom[posisi - 1].empty()
                    continue

                e = element_info.get(simbol, {})
                tooltip = (
                    f"{e.get('nama', simbol)} - "
                    f"Golongan: {e.get('golongan', '-')}, "
                    f"Status: {e.get('status', '-')}, "
                    f"Kegunaan: {e.get('kegunaan', '-')}"
                )

                is_selected = klik_unsur and simbol in klik_unsur
                tombol = kolom[posisi - 1].button(
                    simbol,
                    key=f"{simbol}_{baris}_{posisi}",
                    help=tooltip
                )
                if is_selected:
                    kolom[posisi - 1].markdown(
                        f"<div style='border:1px solid red; padding:4px; border-radius:5px; text-align:center'>{simbol}</div>",
                        unsafe_allow_html=True
                    )
                if tombol:
                    return simbol
            else:
                kolom[posisi - 1].empty()

    return None
