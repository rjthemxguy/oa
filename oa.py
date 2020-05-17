import fileImport as f
import claimImport as c
import constants as con
from os import system
from colorama import Fore, Back, Style
import globals as g
import SummaryModule as s






extract = f.fileClass()


extract.openInput("051520_042420through051220_ins2.csv")
extract.fixAddress("verysmallBatch.csv")
claims = extract.get()


print(claims)

currentAccession = claims.iloc[con.FIRST_ROW, con.ACCESSION_NUMBER]
claim = c.claimClass()
summary = s.summaryClass()
claimList = []

for i in range(len(claims)):

    if claims.iloc[i, con.ACCESSION_NUMBER] == currentAccession:
        claim.addRow(claims.loc[i])
        print(claim.rowList)





    else:
        claimList.append(claim)
        currentAccession = claims.iloc[i, con.ACCESSION_NUMBER]
        claim = c.claimClass()
        claim.addRow(claims.loc[i])
        print(claim.rowList)

        # last record, put it in list
        if i == len(claims) - 1:
            claimList.append(claim)








for claim in claimList:
    pass

    #claim.setMedicare()
    #claim.checkForLab("LP2")
    #claim.checkForLab("LP")
    #claim.getDiagCodes()
    #claim.loadPrices()
    #claim.setDaigCodes()
    #summary.writeClaim(claim)






