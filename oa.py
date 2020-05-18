import fileImport as f
import claimImport as c
import constants as con
from os import system
from colorama import Fore, Back, Style
import globals as g
import oaFileImport as o
import SummaryModule as s

extract = f.fileClass()

system("clear")
print()
print(Fore.RED + "Please Select an Operation you wish to perform:")
print("")
print(Fore.MAGENTA + "[1] Run a new extract")
print(Fore.MAGENTA + "[2] Review Claims for re-run")

allowableKeys = ["1"]

while True:
    menuPress = input()
    if menuPress in allowableKeys:

        if menuPress == "1":
            while True:
                system("clear")
                print()
                print("Please ensure the file you wish to process is in the INPUT directory")
                print("Please paste the file you wish to process below")
                fileToProcess = input()

                try:
                    extract.openInput(fileToProcess)
                    break
                except FileNotFoundError:
                    continue
            print("Break")
        break

# extract.openInput("051520_042420through051220_ins2.csv")
extract.fixAddress("cleaned.csv")
claims = extract.get()

currentAccession = claims.iloc[con.FIRST_ROW, con.ACCESSION_NUMBER]
claim = c.claimClass()
oaFile = o.oaFileClass()
summary = s.summaryClass()
claimList = []

singleRecord = True

for i in range(len(claims)):

    if claims.iloc[i, con.ACCESSION_NUMBER] == currentAccession:
        claim.addRow(claims.loc[i])


    else:
        claimList.append(claim)
        currentAccession = claims.iloc[i, con.ACCESSION_NUMBER]
        claim = c.claimClass()
        claim.addRow(claims.loc[i])
        singleRecord = False

        # last record, put it in list
        if i == len(claims) - 1:
            claimList.append(claim)

if singleRecord == True:
    claimList.append(claim)

summary.writeMast()

system("clear")
print()
print(Fore.YELLOW + "Processing")

numOfClaims = (len(claimList))
claimsProcessed = 1

for claim in claimList:

    # claim.setMedicare()
    claim.checkForLab("LP2")
    claim.checkForLab("LP")
    claim.getDiagCodes()
    claim.loadPrices()
    claim.setDaigCodes(numOfClaims, claimsProcessed)
    oaFile.writeTestBlock(claim.rowList, claim.diagCodeList)
    summary.writeClaim(claim, claim.diagCodeList)

    claimsProcessed += 1

oaFile.closeOAFile()
summary.writePDF()
