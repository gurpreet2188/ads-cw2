import dateHelper, printHelper


class InputHelper:

    def __init__(self):
        self.__date = dateHelper.Date()
        self.__errMsg = 'Error!! invalid or no value enterd.'
        self.__print = printHelper.PrintHelper()

    def stringInput(self, msg, type):
        check = False
        val = ''
        while check is not True:
            val = str(input(msg))
            if val.strip() == '' or val == None:  # check if value is blank or none
                print(self.__errMsg)
            elif type == 'name':
                # only letters and spaces for customer or employee names
                if all(x.isspace() or x.isalpha() for x in val):
                    check = True
                else:
                    print(self.__errMsg)
            elif type == 'number':
                if not val.isnumeric():  # must only contains numbers
                    print(self.__errMsg)
                else:
                    check = True
            else:
                check = True
        return val

    def dateInput(self, msg):
        check = False
        val = ''
        while check is not True:
            val = str(input(msg))
            if val.strip() == '' or val == None:
                print(self.__errMsg)
            elif val.isalpha():
                print(self.__errMsg)
            else:
                check = self.__date.verifyDate(val)
                if check is not True:
                    print(self.__errMsg)
        return val

    def menuInput(self, msg, options, menuName):
        check = False
        val = 0
        while check is not True:
            self.__print.printMenu(options, menuName)
            try:
                val = int(input(msg))
            except ValueError as e:
                print(self.__errMsg)
            if val not in range(1, len(options)+1):
                print(self.__errMsg)
            else:
                check = True
        return val

    def detailsMenuInput(self, msg):
        check = False
        val = 0
        while check is not True:
            val = str(input(msg))
            if val != 'exit':
                try:
                    val = int(val)
                    check = True
                except ValueError as e:
                    print(self.__errMsg)
            else:
                check = True
        return val
