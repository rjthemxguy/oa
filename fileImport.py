import csv
import pandas as pd

class fileClass:
    def __init__(self):

        self.filePath = "input/"
        self.inputFileName = ""

    def __numIn(self, s):
        return any(i.isdigit() for i in s)

    def setPath(self, path):
        self.filePath = path

    def openInput(self,inputFileName):
        with open(self.filePath + inputFileName, 'r') as file:
            fileData = file.read()

            fileData = fileData.replace('"', '')

            with open('scratch/cleaned.csv', 'w') as file:
                file.write(fileData)

                file.close()

    def fixAddress(self, fileName):

        with open('scratch/' + fileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/addressFixed.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:

                    if self.__numIn(row[4]) == True:
                        row[3] = row[3] + row[4]
                        del row[4]

                    if self.__numIn(row[27]) == True:
                        row[26] = row[26] + row[27]
                        del row[27]

                    if self.__numIn(row[33]) == True:
                        row[32] = row[32] + row[33]
                        del row[33]

                    if "SUITE" in row[345]:
                        row[344] = row[344] + row[345]
                        row[345] = ""

                        del row[345]



                    writer.writerow(row)


                result.close()

    def get(self):

        self.dataset = pd.read_csv("scratch/addressFixed.csv", header=None)

        return(self.dataset)