elemen_periodik = [
    # Baris 1
    [
        {"simbol": "H", "golongan": "nonlogam"},
        *[{} for _ in range(16)],
        {"simbol": "He", "golongan": "gas mulia"}
    ],
    # Baris 2
    [
        {"simbol": "Li", "golongan": "logam alkali"},
        {"simbol": "Be", "golongan": "logam alkali tanah"},
        *[{} for _ in range(10)],
        {"simbol": "B", "golongan": "metaloid"},
        {"simbol": "C", "golongan": "nonlogam"},
        {"simbol": "N", "golongan": "nonlogam"},
        {"simbol": "O", "golongan": "nonlogam"},
        {"simbol": "F", "golongan": "halogen"},
        {"simbol": "Ne", "golongan": "gas mulia"}
    ],
    # Baris 3
    [
        {"simbol": "Na", "golongan": "logam alkali"},
        {"simbol": "Mg", "golongan": "logam alkali tanah"},
        *[{} for _ in range(10)],
        {"simbol": "Al", "golongan": "logam pasca transisi"},
        {"simbol": "Si", "golongan": "metaloid"},
        {"simbol": "P", "golongan": "nonlogam"},
        {"simbol": "S", "golongan": "nonlogam"},
        {"simbol": "Cl", "golongan": "halogen"},
        {"simbol": "Ar", "golongan": "gas mulia"}
    ],
    # Baris 4
    [
        {"simbol": "K", "golongan": "logam alkali"},
        {"simbol": "Ca", "golongan": "logam alkali tanah"},
        {"simbol": "Sc", "golongan": "logam transisi"},
        {"simbol": "Ti", "golongan": "logam transisi"},
        {"simbol": "V", "golongan": "logam transisi"},
        {"simbol": "Cr", "golongan": "logam transisi"},
        {"simbol": "Mn", "golongan": "logam transisi"},
        {"simbol": "Fe", "golongan": "logam transisi"},
        {"simbol": "Co", "golongan": "logam transisi"},
        {"simbol": "Ni", "golongan": "logam transisi"},
        {"simbol": "Cu", "golongan": "logam transisi"},
        {"simbol": "Zn", "golongan": "logam transisi"},
        {"simbol": "Ga", "golongan": "logam pasca transisi"},
        {"simbol": "Ge", "golongan": "metaloid"},
        {"simbol": "As", "golongan": "metaloid"},
        {"simbol": "Se", "golongan": "nonlogam"},
        {"simbol": "Br", "golongan": "halogen"},
        {"simbol": "Kr", "golongan": "gas mulia"}
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

# Massa atom relatif (Ar) untuk masing-masing unsur
Ar_tiap_unsur = {
    "H": 1.01, "He": 4.00, "Li": 6.94, "Be": 9.01, "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00,
    "F": 19.00, "Ne": 20.18, "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97,
    "S": 32.07, "Cl": 35.45, "Ar": 39.95, "K": 39.10, "Ca": 40.08, "Sc": 44.96, "Ti": 47.87,
    "V": 50.94, "Cr": 52.00, "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69, "Cu": 63.55,
    "Zn": 65.38, "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.96, "Br": 79.90, "Kr": 83.80,
    "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22, "Nb": 92.91, "Mo": 95.95, "Tc": 98.00,
    "Ru": 101.07, "Rh": 102.91, "Pd": 106.42, "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71,
    "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29, "Cs": 132.91, "Ba": 137.33, "La": 138.91,
    "Hf": 178.49, "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 195.08,
    "Au": 196.97, "Hg": 200.59, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Po": 209.00, "At": 210.00,
    "Rn": 222.00, "Fr": 223.00, "Ra": 226.00, "Rf": 267.00, "Db": 270.00, "Sg": 271.00, "Bh": 270.00,
    "Hs": 277.00, "Mt": 278.00, "Ds": 281.00, "Rg": 282.00, "Cn": 285.00, "Nh": 286.00, "Fl": 289.00,
    "Mc": 290.00, "Lv": 293.00, "Ts": 294.00, "Og": 294.00
}
