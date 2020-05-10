import fileImport as f
import claimImport as c

extract = f.fileClass()


extract.openInput("claims1.csv")
extract.fixAddress("cleaned.csv")
claims = extract.get()

currentAcession = claims.iloc[0, 362]
claim = c.claimClass()

for i in range(len(claims)):

    if claims.iloc[i, 362] == currentAcession:
        claim.addRow(claims.loc[i])

    else:
        currentAcession = claims.iloc[i, 362]

