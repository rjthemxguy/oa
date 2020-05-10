import fileImport as f

extract = f.fileClass()

extract.openInput("claims1.csv")
extract.fixAddress("cleaned.csv")
claims = extract.get()

currentAcession = claims.iloc[0, 362]
x = 0

for i in range(len(claims)):

    if claims.iloc[i, 362] == currentAcession:
        x += 1
        print(x)
    else:
        currentAcession = claims.iloc[i, 362]
        x = 1
        print(x)


