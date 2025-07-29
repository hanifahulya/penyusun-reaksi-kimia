reaksi_opsional = {}
reaksi_tunggal = {}

def susun_reaksi_dari_unsur(unsur):
    return ["Contoh Persamaan"]

def hitung_massa_molekul(rumus):
    return 18.015

reaksi_opsional = {
    frozenset(["Fe", "Cl"]): [
        ("FeCl_2", "Fe + Cl_2 → FeCl_2"),
        ("FeCl_3", "2Fe + 3Cl_2 → 2FeCl_3")
    ],
    frozenset(["Pb", "O"]): [
        ("PbO", "2Pb + O_2 → 2PbO")
    ]
}