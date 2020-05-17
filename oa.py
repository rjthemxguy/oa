import fileImport as f
import claimImport as c
import constants as con
from os import system
from colorama import Fore, Back, Style
import globals as g
import SummaryModule as s

extract = f.fileClass()

extract.openInput("051520_042420through051220_ins2.csv")
extract.fixAddress("smallBatch.csv")
claims = extract.get()

currentAccession = claims.iloc[con.FIRST_ROW, con.ACCESSION_NUMBER]
claim = c.claimClass()
summary = s.summaryClass()
claimList = []

for i in range(len(claims)):

    if claims.iloc[i, con.ACCESSION_NUMBER] == currentAccession:
        claim.addRow(claims.loc[i])






    else:
        claimList.append(claim)
        currentAccession = claims.iloc[i, con.ACCESSION_NUMBER]
        claim = c.claimClass()
        claim.addRow(claims.loc[i])

        # last record, put it in list
        if i == len(claims) - 1:
            claimList.append(claim)

summary.writeMast()

for claim in claimList:
    print(claim.rowList)
    # claim.setMedicare()
    claim.checkForLab("LP2")
    claim.checkForLab("LP")
    claim.getDiagCodes()
    #claim.loadPrices()
    #claim.setDaigCodes()
    summary.writeClaim(claim)

summary.writePDF()