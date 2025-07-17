def tampilkan_tabel_periodik():
    max_kolom = 18  # jumlah kolom tetap
    for baris in elemen_periodik:
        while len(baris) < max_kolom:
            baris.append({})

        kolom = st.columns(max_kolom)
        for i, elemen in enumerate(baris):
            simbol = elemen.get("simbol", "")
            golongan = elemen.get("golongan", "lainnya")
            warna = warna_golongan.get(golongan, "#E0E0E0")
            if simbol:
                Ar = Ar_tiap_unsur.get(simbol, "")
                label = f"{simbol}"
                tooltip = f"{simbol} (Ar = {Ar})" if Ar else simbol
                if kolom[i].button(label, help=tooltip, key=f"{simbol}_{i}", use_container_width=True):
                    if "selected_elements" not in st.session_state:
                        st.session_state.selected_elements = []
                    if len(st.session_state.selected_elements) < 2 and simbol not in st.session_state.selected_elements:
                        st.session_state.selected_elements.append(simbol)
            else:
                kolom[i].markdown(" ")
