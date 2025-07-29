# Placeholder untuk reaction_engine.py
# Isi lengkap reaksi_opsional dan reaksi_tunggal akan disalin dari pengguna
reaksi_opsional = {}  # digantikan nanti
reaksi_tunggal = {}  # digantikan nanti

def susun_reaksi_dari_unsur(unsur):
    # Dummy return untuk keperluan testing layout
    return ["Contoh Persamaan"]

def hitung_massa_molekul(rumus):
    return 18.015  # nilai dummy

reaksi_opsional = {
    frozenset(["Fe", "Cl"]): [
        ("FeCl_2", "Fe + Cl_2 \\rightarrow FeCl_2"),
        ("FeCl_3", "2Fe + 3Cl_2 \\rightarrow 2FeCl_3")
    ],
    frozenset(["Pb", "O"]): [
        ("PbO", "2Pb + O_2 \\rightarrow 2PbO"),
        ("PbO_2", "Pb + O_2 \\rightarrow PbO_2")
    ],
    ...
    frozenset(["Pr", "O"]): [
        ("PrO_2", "Pr + O_2 \\rightarrow PrO_2"),
        ("Pr_6O_11", "4Pr + 3O_2 \\rightarrow Pr_6O_11")
    ]
}

reaksi_tunggal = {
    frozenset(["H", "O"]): "2H_2 + O_2 \\rightarrow 2H_2O",
    frozenset(["Na", "Cl"]): "2Na + Cl_2 \\rightarrow 2NaCl",
    ...
    frozenset(["Ga","H"]): "2Ga + 3H_2 \\rightarrow 2GaH_3"
}