import pandas as pd


class oaFileClass:
    def __init__(self):
        self.rowIndex = 1
        self.testIndex = 0

        self.oaTemplate = pd.read_csv("template/OATemplate.csv", header=0)

    def _writeHeader(self, _claim, _diagCodeList):
        self.oaTemplate.at[self.rowIndex, "InsurancePlanName"] = _claim[0]["INSURANCE_PLAN_NAME"]
        self.oaTemplate.at[self.rowIndex, "InsurancePayerID"] = _claim[0]["INSURANCE_PAYER_ID"]
        self.oaTemplate.at[self.rowIndex, "InsuranceStreetAddr"] = _claim[0]["INSURANCE_STREET_ADDR"]
        self.oaTemplate.at[self.rowIndex, "InsuranceCity"] = _claim[0]["INSURANCE_CITY"]
        self.oaTemplate.at[self.rowIndex, "InsuranceState"] = _claim[0]["INSURANCE_STATE"]
        self.oaTemplate.at[self.rowIndex, "InsuranceZip"] = _claim[0]["INSURANCE_ZIP"]
        self.oaTemplate.at[self.rowIndex, "PlanGroupHealthPlan"] = _claim[0]["PLAN_GROUP_HEALTH_PLAN"]
        self.oaTemplate.at[self.rowIndex, "PatientID"] = _claim[0]["PATIENT_ID"]
        self.oaTemplate.at[self.rowIndex, "PatientLast"] = _claim[0]["PATIENT_LAST"]
        self.oaTemplate.at[self.rowIndex, "PatientFirst"] = _claim[0]["PATIENT_FIRST"]
        self.oaTemplate.at[self.rowIndex, "PatientMidInit"] = _claim[0]["PATIENT_MID_INIT"]
        self.oaTemplate.at[self.rowIndex, "PatientDOB"] = _claim[0]["PATIENT_DOB"]
        self.oaTemplate.at[self.rowIndex, "PatientStreetAddress"] = _claim[0]["PATIENT_STREET_ADDR"]
        self.oaTemplate.at[self.rowIndex, "PatientCity"] = _claim[0]["PATIENT_CITY"]
        self.oaTemplate.at[self.rowIndex, "PatientState"] = _claim[0]["PATIENT_STATE"]
        self.oaTemplate.at[self.rowIndex, "PatientZip"] = _claim[0]["PATIENT_ZIP"]
        self.oaTemplate.at[self.rowIndex, "PatientPhone"] = _claim[0]["PATIENT_ZIP"]
        self.oaTemplate.at[self.rowIndex, "PatientRelationSELF"] = 1
        self.oaTemplate.at[self.rowIndex, "PatientSignature"] = "Signature on file"
        self.oaTemplate.at[self.rowIndex, "PatientSignatureDate"] = _claim[0]["PATIENT_SIG_DATE"]
        self.oaTemplate.at[self.rowIndex, "InsuredSignature"] = "Signature on File "
        self.oaTemplate.at[self.rowIndex, "ReferringPhysician"] = _claim[0]["REFER_PHY_FIRST"] + " " + _claim[0]["REFER_PHY_LAST"]
        self.oaTemplate.at[self.rowIndex, "ReferPhysQualifier"] = _claim[0]["REFER_PHY_QUAL"]
        self.oaTemplate.at[self.rowIndex, "Refer_Phys_NPI"] = _claim[0]["REFER_PHY_NPI"]
        self.oaTemplate.at[self.rowIndex, "PhysicianSignature"] = "Signature on File"
        self.oaTemplate.at[self.rowIndex, "PhysicianSignatureDate"] = _claim[0]["TO_DATE_SERVICE"]
        self.oaTemplate.at[self.rowIndex, "PhysicianLast"] = "Prime Clinical"
        self.oaTemplate.at[self.rowIndex, "PhysicianFirst"] = "Lab"
        self.oaTemplate.at[self.rowIndex, "FacilityName"] = "Prime Clinical Lab"
        self.oaTemplate.at[self.rowIndex, "FacilityStreetAddr"] = "27825 Fremont Ct"
        self.oaTemplate.at[self.rowIndex, "FacilityCity"] = "Velencia"
        self.oaTemplate.at[self.rowIndex, "FacilityState"] = "CA"
        self.oaTemplate.at[self.rowIndex, "FacilityZip"] = "91355"
        self.oaTemplate.at[self.rowIndex, "FacilityCityStateZip"] = "Valencia CA 91355"
        self.oaTemplate.at[self.rowIndex, "FacilityNPI"] = "1871038778"

        print((_diagCodeList))

    def writeTestBlock(self, _claim, _diagCodeList):
        self._writeHeader(_claim, _diagCodeList)

        for i in range(len(_claim)):
            print(_claim[i])



    def closeOAFile(self):
        self.oaTemplate.to_csv("scratch/oaClaims.csv", header=False, index=False)



