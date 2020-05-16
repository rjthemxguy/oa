import fileImport as f
import claimImport as c
import constants as con
from os import system
from colorama import Fore, Back, Style
import globals as g



extract = f.fileClass()


extract.openInput("claims5.csv")
extract.fixAddress("cleaned.csv")
claims = extract.get()

currentAccession = claims.iloc[0, con.ACCESSION_NUMBER]
claim = c.claimClass()
claimList = []

for i in range(len(claims)):

    if claims.iloc[i, con.ACCESSION_NUMBER] == currentAccession:
        claim.addRow(claims.loc[i])



    else:
        claimList.append(claim)
        currentAccession = claims.iloc[i, con.ACCESSION_NUMBER]
        claim = c.claimClass()
        claim.addRow(claims.loc[i])



for claim in claimList:
    claim.setMedicare()
    claim.checkForLab("LP2")
    claim.checkForLab("LP")
    claim.getDiagCodes()
    #claim.setDaigCodes()


print(g.mode)