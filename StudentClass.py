Import DateTime

class StudentClass:
    def __init__(self, StudentID, Name, DateofBirth, classification):
        self.__StudentID = StudentID
        self.__Name = Name
        self.__DateofBirth = DateofBirth 
        self.__classification = classification
        self.__age = 0
        self.__register = ""

    def __age__(self):
        today = date.today()
        DateofBirth = self.__dob.split("/")
        dob_year = int(dob[2])
        age = today.year - dob_year
        self.__age = age

    def _register_(self):
        if __classification == "Sr":
            self.__register ="4/1 thru 4/3"

        elif __classification == "Jr":
            self.__register = "4/4 thru 4/6"

        elif __classification == "S":
            self.__register = "4/7 thru 4/9"

        elif __classification == "F":
            self.__register = "4/10 thru 4/12"
