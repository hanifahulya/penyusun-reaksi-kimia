reaksi_opsional = {
    frozenset(["Fe", "Cl"]): [
        ("FeCl2", "Fe + Cl2 → FeCl2"),
        ("FeCl3", "2Fe + 3Cl2 → 2FeCl3")
    ],
    frozenset(["Pb", "O"]): [
        ("PbO", "2Pb + O2 → 2PbO")
    ],
    frozenset(["H", "O"]): [
        ("H2O", "2H2 + O2 → 2H2O")
    ]
}

reaksi_tunggal = {}

def susun_reaksi_dari_unsur(unsur):
    pasangan = frozenset(unsur)
    if pasangan in reaksi_opsional:
        hasil = reaksi_opsional[pasangan]
        return [{
            "senyawa": h[0],
            "reaksi": h[1],
            "jenis": "Reaksi Penggabungan"
        } for h in hasil]
    return []

def hitung_massa_molekul(rumus):
    massa_atom = {'H': 1.008, 'O': 16.00, 'Cl': 35.45, 'Fe': 55.85, 'Pb': 207.2}
    import re
    unsur_terdeteksi = re.findall(r'([A-Z][a-z]*)(\d*)', rumus)
    massa = 0.0
    for unsur, jumlah in unsur_terdeteksi:
        jumlah = int(jumlah) if jumlah else 1
        massa += massa_atom.get(unsur, 0) * jumlah
    return round(massa, 3)
