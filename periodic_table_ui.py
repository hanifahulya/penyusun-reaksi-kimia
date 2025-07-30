import streamlit as st

def tampilkan_tabel_periodik(elemen_periodik):
    st.subheader("Filter Unsur berdasarkan Golongan")
    semua_golongan = sorted(set(e['golongan'] for e in elemen_periodik))
    pilihan_golongan = st.selectbox("Pilih Golongan", options=["Semua"] + semua_golongan)

    filtered = elemen_periodik if pilihan_golongan == "Semua" else [e for e in elemen_periodik if e['golongan'] == pilihan_golongan]
    kolom = st.columns(18)
    st.markdown("---")

    if 'terpilih' not in st.session_state:
        st.session_state.terpilih = []

    for elemen in filtered:
        idx = elemen['posisi']
        col = kolom[idx % 18]
        warna = elemen['warna']
        if col.button(elemen['simbol'], key=elemen['simbol']):
            if len(st.session_state.terpilih) < 2:
                st.session_state.terpilih.append(elemen['simbol'])
            else:
                st.session_state.terpilih = [elemen['simbol']]

    if len(st.session_state.terpilih) == 2:
        from reaction_engine.main import susun_reaksi_dari_unsur, hitung_massa_molekul
        hasil = susun_reaksi_dari_unsur(st.session_state.terpilih)
        if hasil:
            for h in hasil:
                st.success(f"{h['reaksi']}\nJenis: {h['jenis']}\nBM: {hitung_massa_molekul(h['senyawa'])}")
        else:
            st.warning("Reaksi tidak ditemukan.")
    elif len(st.session_state.terpilih) == 1:
        st.info(f"Pilih satu unsur lagi.")
