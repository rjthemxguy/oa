import fileImport as f
import claimImport as c

extract = f.fileClass()
claim = c.claimClass()

extract.openInput("claims1.csv")
extract.fixAddress("cleaned.csv")
claims = extract.get()

currentAcession = claims.iloc[0, 362]
x = 0

for i in range(len(claims)):

    if claims.iloc[i, 362] == currentAcession:
        x += 1
        claim.addRow(claims.loc[i])
        print(x)
    else:
        currentAcession = claims.iloc[i, 362]
        x = 1
        print(x)
