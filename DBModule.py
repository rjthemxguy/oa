import mysql.connector


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
            print()
            print("Enter the Accession number to delete from the database")

            x = input()

            if x == "y":
                break
            if x == "n":
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
