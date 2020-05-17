import pandas as pd


class oaFileClass:
    def __init__(self):
        self.rowIndex = 1
        self.testIndex = 0

        self.oaTemplate = pd.read_csv("template/OATemplate.csv", header=0)

    def _writeHeader(self, _claim):
        self.oaTemplate.at[self.rowIndex, "InsurancePlanName"] = _claim[0]["INSURANCE_PLAN_NAME"]
        self.oaTemplate.at[self.rowIndex, "InsurancePayerID"] = _claim[0]["INSURANCE_PAYER_ID"]
        self.oaTemplate.at[self.rowIndex, "InsuranceStreetAddr"] = _claim[0]["INSURANCE_STREET_ADDR"]

    def writeTestBlock(self, _claim):
        self._writeHeader(_claim)

        for i in range(len(_claim)):
            print(_claim[i])



    def closeOAFile(self):
        self.oaTemplate.to_csv("scratch/oaClaims.csv", header=False, index=False)



