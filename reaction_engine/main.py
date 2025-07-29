reaksi_opsional = {
    frozenset(["Fe", "Cl"]): ["FeCl_2", "Fe + Cl_2 → FeCl_2", "Reaksi Sintesis", 126.75],
    frozenset(["Pb", "O"]): ["PbO", "2Pb + O_2 → 2PbO", "Reaksi Kombinasi", 223.2]
}
reaksi_tunggal = {}

def susun_reaksi_dari_unsur(unsur):
    kunci = frozenset(unsur)
    return reaksi_opsional.get(kunci, ["Tidak ditemukan", "", "", 0])

def hitung_massa_molekul(rumus):
    return 18.015  # contoh H2O