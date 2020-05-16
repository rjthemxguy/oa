import csv
import pandas as pd
import constants as con


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

                    if self.__numIn(row[con.NUM_FIX_1]) == True:
                        row[con.NUM_FIX_1 - 1] = row[con.NUM_FIX_1 - 1] + row[con.NUM_FIX_1]
                        del row[con.NUM_FIX_1]

                    if self.__numIn(row[con.NUM_FIX_2]) == True:
                        row[con.NUM_FIX_2 - 1] = row[con.NUM_FIX_2 - 1] + row[con.NUM_FIX_2]
                        del row[con.NUM_FIX_2]


                    if self.__numIn(row[con.NUM_FIX_3]) == True:
                        row[con.NUM_FIX_3 - 1] = row[con.NUM_FIX_3 - 1] + row[con.NUM_FIX_3]
                        del row[con.NUM_FIX_3]

                    if "SUITE" in row[con.SUITE_FIX_1]:
                        row[con.SUITE_FIX_1 - 1] = row[con.SUITE_FIX_1 - 1] + row[con.SUITE_FIX_1]
                        del row[con.SUITE_FIX_1]


                    writer.writerow(row)


                result.close()

    def get(self):

        self.dataset = pd.read_csv("scratch/addressFixed.csv", header=None)

        return(self.dataset)