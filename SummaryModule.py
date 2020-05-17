class summaryClass:



    def __init__(self):

        from fpdf import FPDF
        self.pdf = FPDF()
        self.currentRow = 0
        self.claimCount = 1

    def writeClaim(self, claim):
        self.pdf.set_font('Arial', '', 8)
        self.pdf.set_xy(0, self.currentRow)
        self.pdf.cell(5, 4, "[" + str(self.claimCount) + "]")



        for row in claim.rowList:
            pass



        self.currentRow += 10
        self.claimCount += 1





    def writeMast(self):

        self.pdf.add_page()
        self.pdf.set_font('Arial', '', 10)
        self.pdf.set_xy(0,0)
        self.pdf.cell(5, 10, 'Claim Summary - ')
        self.pdf.set_xy(8, self.currentRow + 10)
        self.pdf.set_font('Arial', '', 8)
        self.pdf.cell(5, 4, "Accession #")
        self.pdf.set_xy(30, self.currentRow + 10)
        self.pdf.cell(5, 4, "Sub ID")
        self.pdf.set_xy(50, self.currentRow + 10)
        self.pdf.cell(5, 4, "Patient Last")
        self.pdf.set_xy(75, self.currentRow + 10)
        self.pdf.cell(5, 4, "Patient First")
        self.pdf.set_xy(95, self.currentRow + 10)
        self.pdf.cell(5, 4, "DOB")
        self.pdf.set_xy(110, self.currentRow + 10)
        self.pdf.cell(5, 4, "Gender")
        self.pdf.set_xy(125, self.currentRow + 10)
        self.pdf.cell(5, 4, "Ref Phy")
        self.pdf.set_xy(145, self.currentRow + 10)
        self.pdf.cell(5, 4, "Ref Phy NPI")
        self.pdf.set_xy(165, self.currentRow + 10)
        self.pdf.cell(5, 4, "Insurance")
        self.currentRow = 20


    def writePDF(self):
        self.pdf.output('claimSummary.pdf', 'F')