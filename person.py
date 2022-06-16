class Person:
    def __init__(self):
        self.__firstName = None
        self.__lastName = None
        self.__gender = None

    def setFirstName(self, fName):
        self.__firstName = fName

    def setLastName(self, lName):
        self.__lastName = lName
        
    def setGender(self, gender):
        self.__gender = gender

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName
    
    def getGender(self) -> str:
        return self.__gender
