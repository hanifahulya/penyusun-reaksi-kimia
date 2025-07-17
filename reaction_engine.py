import re
from utils.tabel_periodik_118 import massa_atom, elemen_periodik

def bersihkan_rumus(rumus_latex):
    return rumus_latex.replace("_", "")

reaksi_opsional = {
    frozenset(["C", "O"]): [
        ("CO", "2C + O_2 \rightarrow 2CO"),
        ("CO_2", "C + O_2 \rightarrow CO_2")
    ]
}

reaksi_tunggal = {
    frozenset(["H", "O"]): "2H_2 + O_2 \rightarrow 2H_2O",
    frozenset(["Na", "Cl"]): "2Na + Cl_2 \rightarrow 2NaCl",
    frozenset(["C", "O"]): "C + O_2 \rightarrow CO_2"
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
