from utils.tabel_periodik_118 import Ar, reaksi_opsional, reaksi_tunggal

reaction_rules = {}

for k, v in reaksi_tunggal.items():
    reaction_rules[k] = {
        "produk": v.split("→")[-1].strip(),
        "setara": v,
        "jenis": "Reaksi Sintesis"
    }

for k, daftar_opsi in reaksi_opsional.items():
    reaction_rules[k] = {
        "produk_opsional": [item[0] for item in daftar_opsi],
        "setara_opsi": [item[1] for item in daftar_opsi],
        "jenis": "Reaksi Sintesis"
    }

# 🔬 Fungsi untuk menyusun reaksi dari dua unsur
def susun_reaksi_dari_unsur(unsur_terpilih):
    kunci = frozenset(unsur_terpilih)
    if kunci in reaksi_opsional:
        return {
            "produk_opsional": [item[0] for item in reaksi_opsional[kunci]],
            "setara_opsi": [item[1] for item in reaksi_opsional[kunci]],
            "jenis": "Reaksi Sintesis"
        }
    elif kunci in reaction_rules:
        return reaction_rules[kunci]
    else:
        return {
            "produk": "Tidak diketahui",
            "setara": "Reaksi tidak ditemukan",
            "jenis": "Tidak diketahui"
        }

# 🧪 Fungsi menghitung massa molekul relatif (Mr)
import re

def hitung_massa_molekul(rumus):
    total = 0
    pattern = r"([A-Z][a-z]?)(\d*)"
    try:
        for unsur, jumlah in re.findall(pattern, rumus):
            jumlah = int(jumlah) if jumlah else 1
            total += Ar.get(unsur, 0) * jumlah
        return total if total > 0 else None
    except:
        return None
