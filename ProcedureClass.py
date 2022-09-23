class Procedure: 
    def __init__(self, Procedure, Date, Practitioner, Charges, PatientID):
        self.__Procedure = Procedure
        self.__Date = Date
        self.__Practitioner = Practitioner 
        self.__Charges = Charges
        self.__PatientID = PatientID

    def get_Procedure (self):
        return self.__Procedure

    def get_Date (self):
        return self.__Date

    def get_Practitioner (self):
        return self.__Practitioner

    def get_Charges (self):
        return self.__Charges

    def get_PatientID (self):
        return self.__PatientID

