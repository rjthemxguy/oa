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

                    if self.__numIn(row[25]) == True:
                        row[24] = row[24] + row[25]
                        del row[25]


                    if self.__numIn(row[31]) == True:
                        row[30] = row[30] + row[31]
                        del row[31]

                    if "SUITE" in row[343]:
                        row[342] = row[342] + row[343]
                        row[343] = ""

                        del row[345]



                    writer.writerow(row)


                result.close()

    def get(self):

        self.dataset = pd.read_csv("scratch/addressFixed.csv", header=None)

        return(self.dataset)