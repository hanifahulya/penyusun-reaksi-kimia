reaksi_tunggal = {
    frozenset(["Na", "Cl"]): {"reaksi": "2Na + Cl₂ → 2NaCl", "jenis": "Senyawa Ionik"},
    frozenset(["H", "O"]): {"reaksi": "2H₂ + O₂ → 2H₂O", "jenis": "Kovalen Polar"},
    frozenset(["K", "Br"]): {"reaksi": "2K + Br₂ → 2KBr", "jenis": "Senyawa Ionik"},
}

reaksi_opsional = {
    frozenset(["C", "O"]): {"reaksi": "C + O₂ → CO₂", "jenis": "Kovalen Nonpolar"},
    frozenset(["N", "H"]): {"reaksi": "N₂ + 3H₂ → 2NH₃", "jenis": "Kovalen Polar"},
}

Ar_tiap_unsur = {
    "H": 1, "O": 16, "Na": 23, "Cl": 35.5, "K": 39, "Br": 80,
    "C": 12, "N": 14
}

def proses_reaksi(unsur1, unsur2):
    pasangan = frozenset([unsur1, unsur2])
    hasil = reaksi_tunggal.get(pasangan) or reaksi_opsional.get(pasangan)
    if hasil:
        produk = hasil['reaksi'].split('→')[-1].strip()
        simbol = ''.join(filter(str.isalpha, produk))
        bm = sum(Ar_tiap_unsur.get(el, 0) for el in simbol)
        return {"reaksi": hasil["reaksi"], "jenis": hasil["jenis"], "bm": bm}
    return None