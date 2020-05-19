import os
from os import system
from colorama import Fore, Back, Style

class inputClass:
    def __init__(self):
        self.inputList = []

    def getInput(self):
        inputDirList = os.listdir('input')

        system("clear")
        print(Fore.YELLOW + "Please select the file wish to process")
        print()

        allowableKeys = []
        inputCount = 0
        for i in range(len(inputDirList)):
            if "csv" in inputDirList[i]:
                inputCount += 1
                allowableKeys.append(str(inputCount))
                self.inputList.append(inputDirList[i])
                print(Fore.WHITE + "[" + str(i+1) + "] " + "- " + inputDirList[i])

        while True:
            x = int(input())
            if str(x) in allowableKeys:
                return self.inputList[x-1]
