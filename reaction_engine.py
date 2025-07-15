def susun_reaksi_dari_unsur(unsur_terpilih):
    kunci = frozenset(unsur_terpilih)
    if kunci == frozenset(["H", "Cl"]):
        return {"setara": "H_2 + Cl_2 \\rightarrow 2HCl", "jenis": "Reaksi Sintesis"}
    elif kunci == frozenset(["Na", "Cl"]):
        return {"setara": "2Na + Cl_2 \\rightarrow 2NaCl", "jenis": "Reaksi Sintesis"}
    else:
        return {"setara": "Reaksi tidak ditemukan", "jenis": "Tidak diketahui"}

def susun_reaksi_dari_senyawa(nama_senyawa):
    return {
        "produk": nama_senyawa,
        "setara": nama_senyawa,
        "jenis": "Reaksi Sintesis"
    }
