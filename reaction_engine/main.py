def susun_reaksi_dari_unsur(unsur):
    return ["Contoh Persamaan"]

def hitung_massa_molekul(rumus):
    return 18.015  

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
    ],
    
    frozenset(["Cl", "Mn"]): [
    ("MnCl_2", "Mn + Cl_2 \\rightarrow MnCl_2"),
    ("MnCl_3", "2Mn + 3Cl_2 \\rightarrow 2MnCl_3")
    ],
    frozenset(["Cl", "Sb"]): [
        ("SbCl_3", "2Sb + 3Cl_2 \\rightarrow 2SbCl_3"),
        ("SbCl_5", "2Sb + 5Cl_2 \\rightarrow 2SbCl_5")
    ],
    frozenset(["Br", "P"]): [
        ("PBr_3", "2P + 3Br_2 \\rightarrow 2PBr_3"),
        ("PBr_5", "2P + 5Br_2 \\rightarrow 2PBr_5")
    ],
    frozenset(["I", "P"]): [
        ("PI_3", "2P + 3I_2 \\rightarrow 2PI_3"),
        ("PI_5", "2P + 5I_2 \\rightarrow 2PI_5")
    ],
    frozenset(["Cl", "As"]): [
        ("AsCl_3", "2As + 3Cl_2 \\rightarrow 2AsCl_3"),
        ("AsCl_5", "2As + 5Cl_2 \\rightarrow 2AsCl_5")
    ],
    frozenset(["N", "H"]): [
        ("NH_3", "N_2 + 3H_2 \\rightarrow 2NH_3"),
        ("N_2H_4", "N_2 + 2H_2 \\rightarrow N_2H_4")
    ],
    frozenset(["C", "H"]): [
        ("CH_4", "C + 2H_2 \\rightarrow CH_4"),
        ("C_2H_6", "2C + 3H_2 \\rightarrow C_2H_6")
    ],
    frozenset(["Cu", "O"]): [
        ("CuO", "2Cu + O_2 \\rightarrow 2CuO"),
        ("Cu_2O", "4Cu + O_2 \\rightarrow 2Cu_2O")
    ],
    frozenset(["Fe", "O"]): [
        ("FeO", "2Fe + O_2 \\rightarrow 2FeO"),
        ("Fe_2O_3", "4Fe + 3O_2 \\rightarrow 2Fe_2O_3"),
        ("Fe_3O_4", "3Fe + 2O_2 \\rightarrow Fe_3O_4")
    ],
    frozenset(["Sn", "O"]): [
        ("SnO", "2Sn + O_2 \\rightarrow 2SnO"),
        ("SnO_2", "Sn + O_2 \\rightarrow SnO_2")
    ],
    frozenset(["V", "Cl"]): [
    ("VCl_3", "2V + 3Cl_2 \\rightarrow 2VCl_3"),
    ("VCl_5", "2V + 5Cl_2 \\rightarrow 2VCl_5")
    ],
    frozenset(["Cr", "O"]): [
        ("CrO", "2Cr + O_2 \\rightarrow 2CrO"),
        ("Cr_2O_3", "4Cr + 3O_2 \\rightarrow 2Cr_2O_3"),
        ("CrO_3", "2Cr + 3O_2 \\rightarrow 2CrO_3")
    ],
    frozenset(["Mn", "O"]): [
        ("MnO", "2Mn + O_2 \\rightarrow 2MnO"),
        ("MnO_2", "Mn + O_2 \\rightarrow MnO_2"),
        ("Mn_2O_3", "4Mn + 3O_2 \\rightarrow 2Mn_2O_3")
    ],
    frozenset(["As", "O"]): [
        ("As_2O_3", "4As + 3O_2 \\rightarrow 2As_2O_3"),
        ("As_2O_5", "4As + 5O_2 \\rightarrow 2As_2O_5")
    ],
    frozenset(["Sb", "O"]): [
        ("Sb_2O_3", "4Sb + 3O_2 \\rightarrow 2Sb_2O_3"),
        ("Sb_2O_5", "4Sb + 5O_2 \\rightarrow 2Sb_2O_5")
    ],
    frozenset(["Bi", "Cl"]): [
        ("BiCl_3", "2Bi + 3Cl_2 \\rightarrow 2BiCl_3"),
        ("BiCl_5", "2Bi + 5Cl_2 \\rightarrow 2BiCl_5")
    ],
    frozenset(["Ti", "O"]): [
        ("TiO", "2Ti + O_2 \\rightarrow 2TiO"),
        ("TiO_2", "Ti + O_2 \\rightarrow TiO_2")
    ],
    frozenset(["Pb", "Br"]): [
        ("PbBr_2", "Pb + Br_2 \\rightarrow PbBr_2"),
        ("PbBr_4", "Pb + 2Br_2 \\rightarrow PbBr_4")
    ],
    frozenset(["Sn", "Br"]): [
        ("SnBr_2", "Sn + Br_2 \\rightarrow SnBr_2"),
        ("SnBr_4", "Sn + 2Br_2 \\rightarrow SnBr_4")
    ],
    frozenset(["Sb", "I"]): [
        ("SbI_3", "2Sb + 3I_2 \\rightarrow 2SbI_3"),
        ("SbI_5", "2Sb + 5I_2 \\rightarrow 2SbI_5")
    ],
    frozenset(["Co", "O"]): [
    ("CoO", "2Co + O_2 \\rightarrow 2CoO"),
    ("Co_2O_3", "4Co + 3O_2 \\rightarrow 2Co_2O_3")
    ],
    frozenset(["Ni", "O"]): [
        ("NiO", "2Ni + O_2 \\rightarrow 2NiO"),
        ("Ni_2O_3", "4Ni + 3O_2 \\rightarrow 2Ni_2O_3")
    ],
    frozenset(["Cr", "Cl"]): [
        ("CrCl_2", "Cr + Cl_2 \\rightarrow CrCl_2"),
        ("CrCl_3", "2Cr + 3Cl_2 \\rightarrow 2CrCl_3")
    ],
    frozenset(["Ti", "Cl"]): [
        ("TiCl_2", "Ti + Cl_2 \\rightarrow TiCl_2"),
        ("TiCl_4", "Ti + 2Cl_2 \\rightarrow TiCl_4")
    ],
    frozenset(["U", "O"]): [
        ("UO_2", "U + O_2 \\rightarrow UO_2"),
        ("UO_3", "2U + 3O_2 \\rightarrow 2UO_3")
    ],
    frozenset(["Mo", "Cl"]): [
        ("MoCl_3", "2Mo + 3Cl_2 \\rightarrow 2MoCl_3"),
        ("MoCl_5", "2Mo + 5Cl_2 \\rightarrow 2MoCl_5")
    ],
    frozenset(["W", "Cl"]): [
        ("WCl_4", "W + 2Cl_2 \\rightarrow WCl_4"),
        ("WCl_6", "W + 3Cl_2 \\rightarrow WCl_6")
    ],
    frozenset(["V", "O"]): [
        ("VO", "2V + O_2 \\rightarrow 2VO"),
        ("V_2O_5", "4V + 5O_2 \\rightarrow 2V_2O_5")
    ],
    frozenset(["Ce", "O"]): [
        ("CeO_2", "Ce + O_2 \\rightarrow CeO_2"),
        ("Ce_2O_3", "4Ce + 3O_2 \\rightarrow 2Ce_2O_3")
    ],
    frozenset(["Pr", "O"]): [
        ("PrO_2", "Pr + O_2 \\rightarrow PrO_2"),
        ("Pr_6O_11", "4Pr + 3O_2 \\rightarrow Pr_6O_11")
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
    frozenset(["Sn", "I"]): "Sn + I_2 \\rightarrow SnI_2",
    frozenset(["Ti", "Cl"]): "Ti + 2Cl_2 \\rightarrow TiCl_4",
    frozenset(["V", "O"]): "4V + 5O_2 \\rightarrow 2V_2O_5",
    frozenset(["Cr", "Cl"]): "2Cr + 3Cl_2 \\rightarrow 2CrCl_3",
    frozenset(["Mn", "O"]): "2Mn + O_2 \\rightarrow 2MnO",
    frozenset(["Co", "Cl"]): "Co + Cl_2 \\rightarrow CoCl_2",
    frozenset(["Pb", "Br"]): "Pb + Br_2 \\rightarrow PbBr_2",
    frozenset(["Fe", "O"]): "4Fe + 3O_2 \\rightarrow 2Fe_2O_3",
    frozenset(["Sn", "O"]): "2Sn + O_2 \\rightarrow 2SnO",
    frozenset(["Sb", "Cl"]): "2Sb + 3Cl_2 \\rightarrow 2SbCl_3",
    frozenset(["P", "O"]): "4P + 5O_2 \\rightarrow 2P_2O_5",
    frozenset(["C", "S"]): "C + S \\rightarrow CS",
    frozenset(["S", "O"]): "S + O_2 \\rightarrow SO_2",
    frozenset(["Ni", "Cl"]): "Ni + Cl_2 \\rightarrow NiCl_2",
    frozenset(["Zn", "O"]): "2Zn + O_2 \\rightarrow 2ZnO",
    frozenset(["Y", "Cl"]): "2Y + 3Cl_2 \\rightarrow 2YCl_3",
    frozenset(["Zr", "O"]): "2Zr + O_2 \\rightarrow 2ZrO_2",
    frozenset(["Nb", "Cl"]): "2Nb + 5Cl_2 \\rightarrow 2NbCl_5",
    frozenset(["Mo", "O"]): "2Mo + 3O_2 \\rightarrow 2MoO_3",
    frozenset(["Ag", "O"]): "4Ag + O_2 \\rightarrow 2Ag_2O",
    frozenset(["Cd", "Cl"]): "Cd + Cl_2 \\rightarrow CdCl_2",
    frozenset(["W", "O"]): "2W + 3O_2 \\rightarrow 2WO_3",
    frozenset(["Pt", "Cl"]): "Pt + Cl_2 \\rightarrow PtCl_2",
    frozenset(["Au", "Cl"]): "2Au + 3Cl_2 \\rightarrow 2AuCl_3",
    frozenset(["Hg", "Cl"]): "Hg + Cl_2 \\rightarrow HgCl_2",
    frozenset(["Sc", "O"]): "4Sc + 3O_2 \\rightarrow 2Sc_2O_3",
    frozenset(["La", "Cl"]): "2La + 3Cl_2 \\rightarrow 2LaCl_3",
    frozenset(["Ce", "O"]): "4Ce + 3O_2 \\rightarrow 2Ce_2O_3",
    frozenset(["Th", "Cl"]): "Th + 2Cl_2 \\rightarrow ThCl_4",
    frozenset(["U", "O"]): "U + O_2 \\rightarrow UO_2",
    frozenset(["Cr", "O"]): "4Cr + 3O_2 \\rightarrow 2Cr_2O_3",
    frozenset(["V", "Cl"]): "2V + 3Cl_2 \\rightarrow 2VCl_3",
    frozenset(["Ti", "O"]): "2Ti + O_2 \\rightarrow 2TiO",
    frozenset(["Nb", "O"]): "4Nb + 5O_2 \\rightarrow 2Nb_2O_5",
    frozenset(["Ru", "Cl"]): "2Ru + 3Cl_2 \\rightarrow 2RuCl_3",
    frozenset(["Rh", "Cl"]): "2Rh + 3Cl_2 \\rightarrow 2RhCl_3",
    frozenset(["Pd", "Cl"]): "Pd + Cl_2 \\rightarrow PdCl_2",
    frozenset(["In", "Cl"]): "2In + 3Cl_2 \\rightarrow 2InCl_3",
    frozenset(["Tl", "Cl"]): "2Tl + Cl_2 \\rightarrow 2TlCl",
    frozenset(["Ga", "Cl"]): "2Ga + 3Cl_2 \\rightarrow 2GaCl_3",
    frozenset(["Ge", "Cl"]): "Ge + Cl_2 \\rightarrow GeCl_2",
    frozenset(["Te", "Cl"]): "Te + Cl_2 \\rightarrow TeCl_2",
    frozenset(["Nd", "Cl"]): "2Nd + 3Cl_2 \\rightarrow 2NdCl_3",
    frozenset(["Sm", "Cl"]): "2Sm + 3Cl_2 \\rightarrow 2SmCl_3",
    frozenset(["Gd", "Cl"]): "2Gd + 3Cl_2 \\rightarrow 2GdCl_3",
    frozenset(["Dy", "Cl"]): "2Dy + 3Cl_2 \\rightarrow 2DyCl_3",
    frozenset(["Er", "Cl"]): "2Er + 3Cl_2 \\rightarrow 2ErCl_3",
    frozenset(["Tm", "Cl"]): "2Tm + 3Cl_2 \\rightarrow 2TmCl_3",
    frozenset(["Yb", "Cl"]): "2Yb + 3Cl_2 \\rightarrow 2YbCl_3",
    frozenset(["Th", "O"]): "4Th + 3O_2 \\rightarrow 2Th_2O_3",
    frozenset(["U", "Cl"]): "U + 3Cl_2 \\rightarrow UCl_6",
    frozenset(["Cl", "O"]): "2Cl + O \\rightarrow Cl_2O",
    frozenset(["Sr", "O"]): "2Sr + O_2 \\rightarrow 2SrO",
    frozenset(["Li", "O"]): "4Li + O_2 \\rightarrow 2Li_2O",
    frozenset(["Mg", "S"]): "Mg + S \\rightarrow MgS",
    frozenset(["Na", "S"]): "2Na + S \\rightarrow Na_2S",
    frozenset(["Mg", "N"]): "3Mg + 2N_2 \\rightarrow Mg_2N_2",
    frozenset(["Zn", "S"]): "Zn + S \\rightarrow ZnS",
    frozenset(["K", "O"]): "4K + O_2 \\rightarrow 2K_2O",
    frozenset(["Li","H"]): "2Li + H_2 \\rightarrow 2LiH",
    frozenset(["Na","H"]): "2Na + H_2 \\rightarrow 2NaH",
    frozenset(["K","H"]): "2K + H_2 \\rightarrow 2KH",
    frozenset(["Ca","H"]): "Ca + H_2 \\rightarrow CaH_2",
    frozenset(["Sr","H"]): "Sr + H_2 \\rightarrow SrH_2",
    frozenset(["Ba","H"]): "Ba + H_2 \\rightarrow BaH_2",
    frozenset(["Rb","H"]): "2Rb + H_2 \\rightarrow 2RbH",
    frozenset(["Cs","H"]): "2Cs + H_2 \\rightarrow 2CsH",
    frozenset(["Mg","H"]): "Mg + H_2 \\rightarrow MgH_2",
    frozenset(["Sc","H"]): "Sc + H_2 \\rightarrow ScH_2",
    frozenset(["B","H"]): "2B + 3H_2 \\rightarrow B_2H_6",
    frozenset(["Si","H"]): "Si + 2H_2 \\rightarrow SiH_4",
    frozenset(["P","H"]): "2P + 3H_2 \\rightarrow 2PH_3",
    frozenset(["As","H"]): "2As + 3H_2 \\rightarrow 2AsH_3",
    frozenset(["Sb","H"]): "2Sb + 3H_2 \\rightarrow 2SbH_3",
    frozenset(["S","H"]): "H_2 + S \\rightarrow H_2S",
    frozenset(["Se","H"]): "H_2 + Se \\rightarrow H_2Se",
    frozenset(["Ga","H"]): "2Ga + 3H_2 \\rightarrow 2GaH_3"
}
