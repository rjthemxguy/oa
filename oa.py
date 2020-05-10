import fileImport as f


extract = f.fileClass()


extract.openInput("claims1.csv")
extract.fixAddress("cleaned.csv")
claims = extract.get()
