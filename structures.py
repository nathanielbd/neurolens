from openeye import oechem
import numpy as np

with open("data/drug_lists/depression/depression_drugs.txt", "r") as d:
    depression_drugs = d.read().split("\n")

depression_smiles = ['CN(C)CCCC1(OCC2=C1C=CC(=C2)C#N)C1=CC=C(F)C=C1', 'CN(C)CCC[C@]1(OCC2=C1C=CC(=C2)C#N)C1=CC=C(F)C=C1', 'CNCCC(OC1=CC=C(C=C1)C(F)(F)F)C1=CC=CC=C1', 'COCCCC\C(=N/OCCN)C1=CC=C(C=C1)C(F)(F)F', 'FC1=CC=C(C=C1)[C@@H]1CCNC[C@H]1COC1=CC2=C(OCO2)C=C1', 'CN[C@H]1CC[C@@H](C2=CC(Cl)=C(Cl)C=C2)C2=CC=CC=C12', 'CNCC[C@H](OC1=CC=CC2=CC=CC=C12)C1=CC=CS1', 'COC1=CC=C(C=C1)C(CN(C)C)C1(O)CCCCC1', 'CN(C)CC(C1=CC=C(O)C=C1)C1(O)CCCCC1', 'CNCC[C@H](OC1=CC=CC2=CC=CC=C12)C1=CC=CS1', 'CCN(CC)C(=O)C1(CC1CN)C1=CC=CC=C1', 'COC1=CC=C(C=C1)C(CN(C)C)C1(O)CCCCC1', 'OC(=O)CCCCCCNC1C2=CC=CC=C2CCC2=CC=CC=C12', 'CC(NC(C)(C)C)C(=O)C1=CC(Cl)=CC=C1', 'COC(=O)C(C1CCCCN1)C1=CC=CC=C1', 'CN1CC(C2=CC=CC=C2)C2=C(C1)C(N)=CC=C2']

with open("data/drug_lists/schizophrenia/schizophrenia_drugs.txt", "r") as s:
    schizophrenia_drugs = s.read().split("\n")

schizophrenia_smiles = ['ClC1=CC=CC(N2CCN(CCCCOC3=CC4=C(CCC(=O)N4)C=C3)CC2)=C1Cl', 'CN1CCN(CC1)C1=NC2=CC(Cl)=CC=C2NC2=CC=CC=C12', 'CN1CCN(CC1)C1=NC2=CC=CC=C2NC2=C1C=C(C)S2', 'CC1=C(CCN2CCC(CC2)C2=NOC3=C2C=CC(F)=C3)C(=O)N2CCCC(O)C2=N1', '[H][C@@]12CCCC[C@]1([H])C(=O)N(CCCCN1CCN(CC1)C1=NSC3=CC=CC=C13)C2=O', 'CC1=C(CCN2CCC(CC2)C2=NOC3=C2C=CC(F)=C3)C(=O)N2CCCCC2=N1', 'CN(C)C(=O)N[C@H]1CC[C@H](CCN2CCN(CC2)C2=C(Cl)C(Cl)=CC=C2)CC1', 'OCCOCCN1CCN(CC1)C1=NC2=CC=CC=C2SC2=CC=CC=C12', 'CN(C)CCOC1=CC2=CC=CC=C2SC2=CC=C(Cl)C=C12']

# m = len(schizophrenia_smiles)
# s_dists = np.ones((m,m))
# for i in range(0,m):
#     for j in range(0,m):
# 
