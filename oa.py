import fileImport as f
import claimImport as c
import constants as con
from os import system

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
    
    claim.checkForLab("LP2")
    claim.checkForLab("LP")
    claim.getDiagCodes()
    print(claim.accession_number)
    claim.setDaigCodes()


