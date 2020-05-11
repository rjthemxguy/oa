import fileImport as f
import claimImport as c
import constants as con


extract = f.fileClass()


extract.openInput("claims1.csv")
extract.fixAddress("cleaned.csv")
claims = extract.get()

currentAccession = claims.iloc[0, con.ACCESSION_NUMBER]
claim = c.claimClass()

for i in range(len(claims)):

    if claims.iloc[i, con.ACCESSION_NUMBER] == currentAccession:
        claim.addRow(claims.loc[i])

    else:
        currentAccession = claims.iloc[i, con.ACCESSION_NUMBER]

