import mysql.connector
from os import system
from colorama import Fore, Back, Style
import time




class database_class:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="rjrobinson.net",
            user="rjrob_admin",
            passwd="hapkido",
            database="rjrob_vernonDB"
        )

        self.mycursor = self.mydb.cursor(buffered=True)

    def deleteAccession(self):



        while True:
            system("clear")
            print()
            print(Fore.YELLOW + "Enter the Accession number to delete from the database")

            accessionNumber = str(input())
            system("clear")
            print(Fore.YELLOW + "Is this the accession number you wish to delete: " + Fore.WHITE + accessionNumber)
            y = str(input())
            if y == "y":
                sql = "DELETE FROM accessionRan WHERE accession=" + "'" + accessionNumber + "'"
                self.mycursor.execute(sql)
                print(Fore.RED + "Accession number deleted!")
                time.sleep(3)
                while True:
                    system("clear")
                    print(Fore.YELLOW + "Do you want to delete another accession code?")
                    x = input()
                    if x == "y":
                        break
                    if x == "n":
                        break
                if x == "y":
                    continue
                if x == "n":
                    break
            if y == "n":
                continue


    def insertAccession(self, _accession):
        sql = "INSERT INTO accessionRan (accession) VALUES (" + str(_accession) + ")"
        val = (_accession)
        self.mycursor.execute(sql)

    def getCPT(self, emgCode):
        self.code = emgCode

        sql = "SELECT CPT FROM codes WHERE code=" + "'" + emgCode + "'"

        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchone()

        return self.myresult

    def didRun(self, accession):


        sql = "SELECT accession FROM accessionRan WHERE accession=" + "'" + accession + "'"

        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchone()
        try:
            x = len(self.myresult)
            return True
        except:
            return False


    def getPrice(self, CPT):
        sql = "SELECT price FROM comp WHERE hcpcs=" + "'" + CPT + "'"

        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchone()

        return self.myresult
