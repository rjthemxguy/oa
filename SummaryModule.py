class summaryClass:



    def __init__(self):

        from fpdf import FPDF
        self.pdf = FPDF()
        self.currentRow = 0

    def writeMast(self):

        self.pdf.add_page()
        self.pdf.set_font('Arial', '', 12)
        self.pdf.set_x(0)
        self.pdf.set_y(self.currentRow)
        self.pdf.cell(5, 40, 'Claim Summary')

    def writePDF(self):
        self.pdf.output('claimSummary.pdf', 'F')