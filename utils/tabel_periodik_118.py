# 📦 Massa atom relatif (Ar)
Ar = {
    "H": 1.01, "He": 4.00, "Li": 6.94, "Be": 9.01, "B": 10.81, "C": 12.01,
    "N": 14.01, "O": 16.00, "F": 19.00, "Ne": 20.18, "Na": 22.99, "Mg": 24.31,
    "Al": 26.98, "Si": 28.09, "P": 30.97, "S": 32.07, "Cl": 35.45, "Ar": 39.95,
    "K": 39.10, "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 52.00,
    "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69, "Cu": 63.55, "Zn": 65.38,
    "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.96, "Br": 79.90, "Kr": 83.80,
    "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22, "Nb": 92.91, "Mo": 95.95,
    "Tc": 98.00, "Ru": 101.1, "Rh": 102.9, "Pd": 106.4, "Ag": 107.9, "Cd": 112.4,
    "In": 114.8, "Sn": 118.7, "Sb": 121.8, "Te": 127.6, "I": 126.9, "Xe": 131.3,
    "Cs": 132.9, "Ba": 137.3, "La": 138.9, "Ce": 140.1, "Pr": 140.9, "Nd": 144.2,
    "Pm": 145.0, "Sm": 150.4, "Eu": 152.0, "Gd": 157.3, "Tb": 158.9, "Dy": 162.5,
    "Ho": 164.9, "Er": 167.3, "Tm": 168.9, "Yb": 173.0, "Lu": 175.0, "Hf": 178.5,
    "Ta": 180.9, "W": 183.8, "Re": 186.2, "Os": 190.2, "Ir": 192.2, "Pt": 195.1,
    "Au": 197.0, "Hg": 200.6, "Tl": 204.4, "Pb": 207.2, "Bi": 208.9, "Po": 209.0,
    "At": 210.0, "Rn": 222.0, "Fr": 223.0, "Ra": 226.0, "Ac": 227.0, "Th": 232.0,
    "Pa": 231.0, "U": 238.0, "Np": 237.0, "Pu": 244.0, "Am": 243.0, "Cm": 247.0,
    "Bk": 247.0, "Cf": 251.0, "Es": 252.0, "Fm": 257.0, "Md": 258.0, "No": 259.0,
    "Lr": 262.0, "Rf": 267.0, "Db": 270.0, "Sg": 271.0, "Bh": 270.0, "Hs": 277.0,
    "Mt": 276.0, "Ds": 281.0, "Rg": 282.0, "Cn": 285.0, "Nh": 286.0, "Fl": 289.0,
    "Mc": 290.0, "Lv": 293.0, "Ts": 294.0, "Og": 294.0
}

# 🎨 Warna golongan unsur
warna_golongan = {
    "logam alkali": "#FFB3BA",
    "logam alkali tanah": "#FFDFBA",
    "logam transisi": "#FFFFBA",
    "logam pasca transisi": "#FFE4B5",
    "metaloid": "#BAFFC9",
    "nonlogam": "#BAE1FF",
    "halogen": "#D5BAFF",
    "gas mulia": "#FFBAED",
    "lanthanida": "#C2F0FC",
    "aktinida": "#E6CCFF",
    "lainnya": "#E0E0E0"
}

# 🧪 Reaksi tunggal
reaksi_tunggal = {
    frozenset(["H", "O"]): "2H_2 + O_2 \\rightarrow 2H_2O",
    frozenset(["Na", "Cl"]): "2Na + Cl_2 \\rightarrow 2NaCl",
    frozenset(["C", "O"]): "C + O_2 \\rightarrow CO_2",
    frozenset(["Mg", "O"]): "2Mg + O_2 \\rightarrow 2MgO",
    frozenset(["Mg", "Cl"]): "Mg + Cl_2 \\rightarrow MgCl_2",
    frozenset(["Fe", "S"]): "Fe + S \\rightarrow FeS",
    frozenset(["Ca", "Cl"]): "Ca + Cl_2 \\rightarrow CaCl_2",
    frozenset(["Ca", "O"]): "2Ca + O_2 \\rightarrow 2CaO",
    frozenset(["Al", "O"]): "4Al + 3O_2 \\rightarrow 2Al_2O_3",
    frozenset(["Zn", "Cl"]): "Zn + Cl_2 \\rightarrow ZnCl_2",
    frozenset(["K", "Br"]): "2K + Br_2 \\rightarrow 2KBr",
    frozenset(["Ba", "Cl"]): "Ba + Cl_2 \\rightarrow BaCl_2",
    frozenset(["Li", "Cl"]): "2Li + Cl_2 \\rightarrow 2LiCl",
    frozenset(["Cu", "O"]): "2Cu + O_2 \\rightarrow 2CuO",
    frozenset(["Ag", "Cl"]): "2Ag + Cl_2 \\rightarrow 2AgCl",
    frozenset(["C", "H"]): "C + 2H_2 \\rightarrow CH_4",
    frozenset(["Si", "O"]): "Si + O_2 \\rightarrow SiO_2",
    frozenset(["B", "Cl"]): "2B + 3Cl_2 \\rightarrow 2BCl_3",
    frozenset(["Ca", "Br"]): "Ca + Br_2 \\rightarrow CaBr_2",
    frozenset(["Na", "Br"]): "2Na + Br_2 \\rightarrow 2NaBr",
    frozenset(["K", "I"]): "2K + I_2 \\rightarrow 2KI",
    frozenset(["Al", "Br"]): "2Al + 3Br_2 \\rightarrow 2AlBr_3",
    frozenset(["Ba", "I"]): "Ba + I_2 \\rightarrow BaI_2"
}

# 🔁 Reaksi opsional (multi produk)
reaksi_opsional = {
    frozenset(["Fe", "Cl"]): [
        ("FeCl_2", "Fe + Cl_2 \\rightarrow FeCl_2"),
        ("FeCl_3", "2Fe + 3Cl_2 \\rightarrow 2FeCl_3")
    ],
    frozenset(["N", "O"]): [
        ("NO", "N_2 + O_2 \\rightarrow 2NO"),
        ("NO_2", "N_2 + 2O_2 \\rightarrow 2NO_2")
    ],
    frozenset(["Pb", "O"]): [
        ("PbO", "2Pb + O_2 \\rightarrow 2PbO"),
        ("PbO_2", "Pb + O_2 \\rightarrow PbO_2")
    ],
    frozenset(["P", "Cl"]): [
        ("PCl_3", "2P + 3Cl_2 \\rightarrow 2PCl_3"),
        ("PCl_5", "2P + 5Cl_2 \\rightarrow 2PCl_5")
    ]
}

elemen_periodik = [
    # Baris 1
    [
        {"simbol": "H", "golongan": "nonlogam", "Ar": 1.01},
        *[{} for _ in range(16)],
        {"simbol": "He", "golongan": "gas mulia", "Ar": 4.00}
    ],
    # Baris 2
    [
        {"simbol": "Li", "golongan": "logam alkali", "Ar": 6.94},
        {"simbol": "Be", "golongan": "logam alkali tanah", "Ar": 9.01},
        *[{} for _ in range(10)],
        {"simbol": "B", "golongan": "metaloid", "Ar": 10.81},
        {"simbol": "C", "golongan": "nonlogam", "Ar": 12.01},
        {"simbol": "N", "golongan": "nonlogam", "Ar": 14.01},
        {"simbol": "O", "golongan": "nonlogam", "Ar": 16.00},
        {"simbol": "F", "golongan": "halogen", "Ar": 19.00},
        {"simbol": "Ne", "golongan": "gas mulia", "Ar": 20.18}
    ],
    # Baris 3
    [
        {"simbol": "Na", "golongan": "logam alkali", "Ar": 22.99},
        {"simbol": "Mg", "golongan": "logam alkali tanah", "Ar": 24.31},
        *[{} for _ in range(10)],
        {"simbol": "Al", "golongan": "logam pasca transisi", "Ar": 26.98},
        {"simbol": "Si", "golongan": "metaloid", "Ar": 28.09},
        {"simbol": "P", "golongan": "nonlogam", "Ar": 30.97},
        {"simbol": "S", "golongan": "nonlogam", "Ar": 32.07},
        {"simbol": "Cl", "golongan": "halogen", "Ar": 35.45},
        {"simbol": "Ar", "golongan": "gas mulia", "Ar": 39.95}
    ],
    # Baris 4
    [
        {"simbol": "K", "golongan": "logam alkali", "Ar": 39.10},
        {"simbol": "Ca", "golongan": "logam alkali tanah", "Ar": 40.08},
        {"simbol": "Sc", "golongan": "logam transisi", "Ar": 44.96},
        {"simbol": "Ti", "golongan": "logam transisi", "Ar": 47.87},
        {"simbol": "V", "golongan": "logam transisi", "Ar": 50.94},
        {"simbol": "Cr", "golongan": "logam transisi", "Ar": 52.00},
        {"simbol": "Mn", "golongan": "logam transisi", "Ar": 54.94},
        {"simbol": "Fe", "golongan": "logam transisi", "Ar": 55.85},
        {"simbol": "Co", "golongan": "logam transisi", "Ar": 58.93},
        {"simbol": "Ni", "golongan": "logam transisi", "Ar": 58.69},
        {"simbol": "Cu", "golongan": "logam transisi", "Ar": 63.55},
        {"simbol": "Zn", "golongan": "logam transisi", "Ar": 65.38},
        {"simbol": "Ga", "golongan": "logam pasca transisi", "Ar": 69.72},
        {"simbol": "Ge", "golongan": "metaloid", "Ar": 72.63},
        {"simbol": "As", "golongan": "metaloid", "Ar": 74.92},
        {"simbol": "Se", "golongan": "nonlogam", "Ar": 78.96},
        {"simbol": "Br", "golongan": "halogen", "Ar": 79.90},
        {"simbol": "Kr", "golongan": "gas mulia", "Ar": 83.80}
    ],
    # Baris 5
    [
        {"simbol": "Rb", "golongan": "logam alkali"},
        {"simbol": "Sr", "golongan": "logam alkali tanah"},
        {"simbol": "Y", "golongan": "logam transisi"},
        {"simbol": "Zr", "golongan": "logam transisi"},
        {"simbol": "Nb", "golongan": "logam transisi"},
        {"simbol": "Mo", "golongan": "logam transisi"},
        {"simbol": "Tc", "golongan": "logam transisi"},
        {"simbol": "Ru", "golongan": "logam transisi"},
        {"simbol": "Rh", "golongan": "logam transisi"},
        {"simbol": "Pd", "golongan": "logam transisi"},
        {"simbol": "Ag", "golongan": "logam transisi"},
        {"simbol": "Cd", "golongan": "logam transisi"},
        {"simbol": "In", "golongan": "logam pasca transisi"},
        {"simbol": "Sn", "golongan": "logam pasca transisi"},
        {"simbol": "Sb", "golongan": "metaloid"},
        {"simbol": "Te", "golongan": "metaloid"},
        {"simbol": "I", "golongan": "halogen"},
        {"simbol": "Xe", "golongan": "gas mulia"}
    ],
    # Baris 6
    [
        {"simbol": "Cs", "golongan": "logam alkali"},
        {"simbol": "Ba", "golongan": "logam alkali tanah"},
        *[{} for _ in range(1)],  # Spacer untuk lantanida
        {"simbol": "Hf", "golongan": "logam transisi"},
        {"simbol": "Ta", "golongan": "logam transisi"},
        {"simbol": "W", "golongan": "logam transisi"},
        {"simbol": "Re", "golongan": "logam transisi"},
        {"simbol": "Os", "golongan": "logam transisi"},
        {"simbol": "Ir", "golongan": "logam transisi"},
        {"simbol": "Pt", "golongan": "logam transisi"},
        {"simbol": "Au", "golongan": "logam transisi"},
        {"simbol": "Hg", "golongan": "logam transisi"},
        {"simbol": "Tl", "golongan": "logam pasca transisi"},
        {"simbol": "Pb", "golongan": "logam pasca transisi"},
        {"simbol": "Bi", "golongan": "logam pasca transisi"},
        {"simbol": "Po", "golongan": "metaloid"},
        {"simbol": "At", "golongan": "halogen"},
        {"simbol": "Rn", "golongan": "gas mulia"}
    ],
    # Baris 7
    [
        {"simbol": "Fr", "golongan": "logam alkali"},
        {"simbol": "Ra", "golongan": "logam alkali tanah"},
        *[{} for _ in range(1)],  # Spacer untuk aktinida
        {"simbol": "Rf", "golongan": "logam transisi"},
        {"simbol": "Db", "golongan": "logam transisi"},
        {"simbol": "Sg", "golongan": "logam transisi"},
        {"simbol": "Bh", "golongan": "logam transisi"},
        {"simbol": "Hs", "golongan": "logam transisi"},
        {"simbol": "Mt", "golongan": "logam transisi"},
        {"simbol": "Ds", "golongan": "logam transisi"},
        {"simbol": "Rg", "golongan": "logam transisi"},
        {"simbol": "Cn", "golongan": "logam transisi"},
        {"simbol": "Nh", "golongan": "logam pasca transisi"},
        {"simbol": "Fl", "golongan": "logam pasca transisi"},
        {"simbol": "Mc", "golongan": "logam pasca transisi"},
        {"simbol": "Lv", "golongan": "logam pasca transisi"},
        {"simbol": "Ts", "golongan": "halogen"},
        {"simbol": "Og", "golongan": "gas mulia"}
    ]
]
