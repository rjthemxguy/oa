import constants as con


class claimClass:
    def __init__(self):
        self.rowList = []
        self.rowDict = {}
        self.diagCodeList = []


    def addRow(self, claimRow):

        self.rowDict = {
            "INSURANCE_PLAN_NAME": claimRow[con.INSURANCE_PLAN_NAME],
            "INSURANCE_PAYER_ID": claimRow[con.INSURANCE_PAYER_ID],
            "INSURANCE_STREET_ADDR": claimRow[con.INSURANCE_STREET_ADDR],
            "INSURANCE_CITY": claimRow[con.INSURANCE_CITY],
            "INSURANCE_STATE": claimRow[con.INSURANCE_STATE],
            "INSURANCE_ZIP": claimRow[con.INSURANCE_ZIP],
            "PLAN_GROUP_HEALTH_PLAN": claimRow[con.PLAN_GROUP_HEALTH_PLAN],
            "PATIENT_ID": claimRow[con.PATIENT_ID],
            "PATIENT_LAST": claimRow[con.PATIENT_LAST],
            "PATIENT_FIRST": claimRow[con.PATIENT_FIRST],
            "PATIENT_MID_INIT": claimRow[con.PATIENT_MID_INIT],
            "PATIENT_DOB": claimRow[con.PATIENT_DOB],
            "PATIENT_GENDER": claimRow[con.PATIENT_GENDER],
            "PATIENT_STREET_ADDR": claimRow[con.PATIENT_STREET_ADDR],
            "PATIENT_CITY": claimRow[con.PATIENT_CITY],
            "PATIENT_STATE": claimRow[con.PATIENT_STATE],
            "PATIENT_ZIP": claimRow[con.PATIENT_ZIP],
            "PATIENT_PHONE": claimRow[con.PATIENT_PHONE],
            "PATIENT_SIG_DATE": claimRow[con.PATIENT_SIG_DATE],
            "REFER_PHY_FIRST": claimRow[con.REFER_PHY_FIRST],
            "REFER_PHY_LAST": claimRow[con.REFER_PHY_LAST],
            "REFER_PHY_QUAL": claimRow[con.REFER_PHY_QUAL],
            "REFER_PHY_NPI": claimRow[con.REFER_PHY_NPI],
            "DIAG_1": claimRow[con.DIAG_1],
            "DIAG_2": claimRow[con.DIAG_2],
            "DIAG_3": claimRow[con.DIAG_3],
            "DIAG_4": claimRow[con.DIAG_4],
            "DIAG_5": claimRow[con.DIAG_5],
            "DIAG_6": claimRow[con.DIAG_6],
            "DIAG_7": claimRow[con.DIAG_7],
            "DIAG_8": claimRow[con.DIAG_8],
            "DIAG_9": claimRow[con.DIAG_9],
            "DIAG_10": claimRow[con.DIAG_10],
            "DIAG_11": claimRow[con.DIAG_11],
            "DIAG_12": claimRow[con.DIAG_12],
            "FROM_DATE_SERVICE": claimRow[con.FROM_DATE_SERVICE],
            "TO_DATE_SERVICE": claimRow[con.TO_DATE_SERVICE],
            "CPT": claimRow[con.CPT],
            "EMG": claimRow[con.EMG],
            "PRICE": "",
            "REFER_PHY_ID": claimRow[con.REFER_PHY_ID]
        }

        self.rowList.append(self.rowDict)

    def getPrices(self):
        pass

    def rowCount(self):
        return len(self.rowList)

    def getDiagCodes(self):

        self.diagCodeList.append(self.rowList[0]["DIAG_1"])
        self.diagCodeList.append(self.rowList[0]["DIAG_2"])
        self.diagCodeList.append(self.rowList[0]["DIAG_3"])
        self.diagCodeList.append(self.rowList[0]["DIAG_4"])
        self.diagCodeList.append(self.rowList[0]["DIAG_5"])
        self.diagCodeList.append(self.rowList[0]["DIAG_6"])
        self.diagCodeList.append(self.rowList[0]["DIAG_7"])
        self.diagCodeList.append(self.rowList[0]["DIAG_8"])
        self.diagCodeList.append(self.rowList[0]["DIAG_9"])
        self.diagCodeList.append(self.rowList[0]["DIAG_10"])
        self.diagCodeList.append(self.rowList[0]["DIAG_11"])
        self.diagCodeList.append(self.rowList[0]["DIAG_12"])




    def checkForLab(self, labCode):

        if labCode == "LP2":

            emgCount = 0

            for lp2_claim in self.rowList:

                if "LP" in lp2_claim.values():
                    emgCount += 1
                    LP= lp2_claim

                if "LDLD" in lp2_claim.values():
                    emgCount += 1
                    LDLD = lp2_claim

                if emgCount == 2:
                    lp2_claim.remove(LP)
                    LDLD["EMG"] = "LP2"
                    break

        if labCode == "LP":

            emgCount = 0
            listCount = 0


            for claim in self.rowList:

                # check for 3 tests that make up panel
                if "HDL" in claim.values():
                    emgCount += 1
                    HDL = claim


                if "CHOL" in claim.values():
                    emgCount += 1
                    CHOL = claim


                if "TRIG2" in claim.values():
                    emgCount += 1
                    TRIGclaim = claim

                if emgCount == 3:
                    TRIGclaim["EMG"] = "LP"
                    TRIGclaim["CPT"] = "80061"
                    self.rowList.remove(HDL)
                    self.rowList.remove(CHOL)
                    break



                listCount += 1

