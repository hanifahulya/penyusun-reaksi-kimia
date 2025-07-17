import re
from utils.tabel_periodik_118 import massa_atom, elemen_periodik

def bersihkan_rumus(rumus_latex):
    return rumus_latex.replace("_", "")

reaksi_opsional = {
    frozenset(["Fe", "Cl"]): [
        ("FeCl_2", "Fe + Cl_2 \\rightarrow FeCl_2"),
        ("FeCl_3", "2Fe + 3Cl_2 \\rightarrow 2FeCl_3")
    ],
    frozenset(["Pb", "O"]): [
        ("PbO", "2Pb + O_2 \\rightarrow 2PbO"),
        ("PbO_2", "Pb + O_2 \\rightarrow PbO_2")
    ],
    frozenset(["N", "O"]): [
        ("NO", "N_2 + O_2 \\rightarrow 2NO"),
        ("NO_2", "N_2 + 2O_2 \\rightarrow 2NO_2")
    ],
    frozenset(["Cu", "Cl"]): [
        ("CuCl", "Cu + Cl_2 \\rightarrow CuCl"),
        ("CuCl_2", "Cu + Cl_2 \\rightarrow CuCl_2")
    ],
     frozenset(["Sn", "Cl"]): [
        ("SnCl_2", "Sn + Cl_2 \\rightarrow SnCl_2"),
        ("SnCl_4", "Sn + 2Cl_2 \\rightarrow SnCl_4")
    ],
    frozenset(["P", "Cl"]): [
        ("PCl_3", "2P + 3Cl_2 \\rightarrow 2PCl_3"),
        ("PCl_5", "2P + 5Cl_2 \\rightarrow 2PCl_5")
    ],
    frozenset(["S", "O"]): [
        ("SO_2", "S + O_2 \\rightarrow SO_2"),
        ("SO_3", "2S + 3O_2 \\rightarrow 2SO_3")
    ],
    frozenset(["C", "O"]): [
        ("CO", "2C + O_2 \\rightarrow 2CO"),
        ("CO_2", "C + O_2 \\rightarrow CO_2")
    ],
    frozenset(["Pb", "Cl"]): [
        ("PbCl_2", "Pb + Cl_2 \\rightarrow PbCl_2"),
        ("PbCl_4", "Pb + 2Cl_2 \\rightarrow PbCl_4")
    ]
}

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
    frozenset(["Ba", "I"]): "Ba + I_2 \\rightarrow BaI_2",
    frozenset(["H", "Cl"]): "H_2 + Cl_2 \\rightarrow 2HCl",
    frozenset(["H", "Br"]): "H_2 + Br_2 \\rightarrow 2HBr",
    frozenset(["H", "I"]): "H_2 + I_2 \\rightarrow 2HI",
    frozenset(["Zn", "Br"]): "Zn + Br_2 \\rightarrow ZnBr_2",
    frozenset(["Sn", "I"]): "Sn + I_2 \\rightarrow SnI_2"
}
}

reaction_rules = {}
for k, v in reaksi_tunggal.items():
    produk_latex = v.split("\\rightarrow")[-1].strip()
    produk_asli = bersihkan_rumus(produk_latex)
    reaction_rules[k] = {
        "produk": produk_asli,
        "produk_latex": produk_latex,
        "setara": v,
        "jenis": "Reaksi Sintesis"
    }

for k, daftar_opsi in reaksi_opsional.items():
    produk_opsi = [bersihkan_rumus(item[0]) for item in daftar_opsi]
    produk_latex_opsi = [item[0] for item in daftar_opsi]
    setara_opsi = [item[1] for item in daftar_opsi]
    reaction_rules[k] = {
        "produk_opsional": produk_opsi,
        "produk_latex_opsi": produk_latex_opsi,
        "setara_opsi": setara_opsi,
        "jenis": "Reaksi Sintesis"
    }

def susun_reaksi_dari_unsur(unsur_terpilih):
    kunci = frozenset(unsur_terpilih)
    return reaction_rules.get(kunci, {
        "produk": "Tidak diketahui",
        "produk_latex": "?",
        "setara": "Reaksi tidak ditemukan",
        "jenis": "Tidak diketahui"
    })

def hitung_massa_molekul(rumus):
    def parse_rumus(rumus):
        pattern = r'([A-Z][a-z]?)(\d*)'
        return re.findall(pattern, rumus)

    try:
        rumus = rumus.replace("_", "")
        total = 0
        for simbol, jumlah in parse_rumus(rumus):
            jumlah = int(jumlah) if jumlah else 1
            massa = massa_atom.get(simbol)
            if massa is None:
                return None
            total += massa * jumlah
        return total
    except:
        return None
