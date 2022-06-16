from person import Person
import bstNode
import csvHelper
import printHelper
import dvd


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__contact = None
        self.__rented = []
        self.__renting = []
        self.__csv = csvHelper.CSVReaderWriter()
        self.__mainList = self.__csv.reader('customer.csv')
        self.__customerBST = bstNode.BSTWrapper()
        self.__root = None
        self.__dvd = dvd.DVD()
        self.__print = printHelper.PrintHelper()
        self.setBST('id')

    def __insertNode(self, dataType):
        for n, i in enumerate(self.__mainList):
            if dataType == 'id':
                if i['renting'] != '':
                    i[dataType] = int(i[dataType]) if dataType == 'id' else str(i[dataType])
                    if self.__root == None:
                        self.__root = self.__customerBST.setRoot(i[dataType], i)
                    else:
                        self.__root.insert(i[dataType], i)
            # i[dataType] = int(
            #     i[dataType]) if dataType == 'id' else str(i[dataType])
            # if n == 0:
            #     self.__root = self.__customerBST.setRoot(i[dataType], i)
            # else:
            #     self.__root.insert(i[dataType], i)

    def setBST(self, dataType):
        match dataType:
            case 'id':
                self.__insertNode('id')
            case 'firstName':
                self.__insertNode('firstName')

            case 'lastName':
                self.__insertNode('lastName')
                
        self.__customerBST.setPages()

    def setID(self, id=None):
        if id == None:
            lastNnode = self.__customerBST.getLargestNode().node
            self.__id = lastNnode + 1
            return self.__id
        self.__id = id

    def setContact(self, contact):
        self.__contact = contact

    def setRented(self, rented):
        if isinstance(rented, str):
            self.__rented = rented.split(',')
        elif isinstance(rented, list):
            self.__rented = rented

    def setRenting(self, renting):
        if isinstance(renting, str):
            self.__renting = renting.split(',')
        elif isinstance(renting, list):
            self.__renting = renting
        # if newRenting:
        #     self.__renting.append(newRenting)

    def getID(self) -> str:
        return self.__id

    def getContact(self) -> str:
        return self.__contact

    def getRented(self):
        return self.__rented

    def getRenting(self):
        return self.__renting

    def setVals(self, cusID):
        print('cusID: ', type(cusID))
        vals = self.__customerBST.search(cusID)
        print(vals)
        if vals:
            self.setID(vals.data['id'])
            super().setFirstName(vals.data['firstName'])
            super().setLastName(vals.data['lastName'])
            super().setGender(vals.data['gender'])
            self.setContact(vals.data['number'])
            self.setRented(vals.data['rented'])
            self.setRenting(vals.data['renting'])
        else:
            vals = False
        return vals

    def __valsDict(self):
        return {
            'id': self.getID(),
            'firstName': super().getFirstName(),
            'lastName': super().getLastName(),
            'gender': super().getGender(),
            'number': self.getContact(),
            'rented': ','.join(map(str, self.getRented())),
            'renting': ','.join(map(str, self.getRenting()))}

    def printVal(self):
        print(self.__valsDict())

    def printList(self, pageNum, listType=None):
        cliList = []
        nodeList = self.__customerBST.splitList(pageNum)
        for n in nodeList:
            cliList.append(
                f'ID: {n.data["id"]} {n.data["firstName"]} {n.data["lastName"]}')

        self.__print.printColumn(cliList, 120, 'Customers\' IDs and Names')
        self.__print.printFooter(
                f'Showing page {pageNum} of {self.__customerBST.totalPages}')
        # self.__print.printFooter(f'')

    def printDetail(self, cusID):
        print(self.__id)
        if self.__id is None:
            val = self.setVals(cusID)
        else:
            val = True
        if val:
            cusID = f"ID: {self.getID()}"
            firstName = f"First Name: {self.getFirstName()}"
            lastName = f"Last Name: {self.getLastName()}"
            gender = f"Gender: {self.getGender()}"
            number = f"Contact: {self.getContact()}"

            rented = []
            renting = []
            for rd in self.__rented:
                if rd:
                    rdStr = f'ID: {rd} Title: {self.__dvd.getDVDTitle(rd)}'
                    rented.append(rdStr)
                else:
                    rented.append('None')

            for rt in self.__renting:
                if rt:
                    rtStr = f'ID: {rt} Title: {self.__dvd.getDVDTitle(rt)}'
                    renting.append(rtStr)
                else:
                    renting.append('None')

            cliList = [cusID, firstName, lastName,
                       gender, number]
            self.__print.printColumn(cliList, 30, 'Customer Details')
            self.__print.printColumn(rented, 20, 'Previously Rented')
            self.__print.printColumn(renting, 20, 'Currently Renting')
        else:
            self.__print.printFooter('ID Not Found.')

    def update(self, id):
        header = ['id', 'firstName', 'lastName',
                  'gender', 'number', 'rented', 'renting']

        self.__customerBST.update(id, self.__valsDict())
        
    def addCustomer(self):
        header = ['id', 'firstName', 'lastName',
                  'gender', 'number', 'rented', 'renting']

        self.__mainList.append(self.__valsDict())
        self.__csv.writer('customer.csv',self.__valsDict(),header)
        print(self.__mainList[-1])
    # def search(self, dataType, searchText):
    #     if self.__root:
    #         self.setBST(dataType)
    #         self.__customerBST.search(self.__root, searchText)
        # if self.__customerBST.getSearchResults() != []:
        #     print(self.__customerBST.getSearchResults())
        # match dataType:
        #     case 'id':
        #         self.setBST()
        #         self.__customerBST.search(self.__root, searchText)
        #         print(self.__customerBST.getSearchResults())
        #     case 'firstName':
        #         self.__customerBST.search(self.__root, searchText)
        #         print(self.__customerBST.getSearchResults())
        #     case 'lastName':
        #         self.__customerBST.search(self.__root, searchText)
        #         print(self.__customerBST.getSearchResults())

    # def smallest(self):
    #     # self.__customerBST.getAll(self.__root)
    #     return self.__customerBST.getSmallestVal(self.__root)

    # def largest(self):
    #     # self.__customerBST.getAll(self.__root)
    #     return self.__customerBST.getLargestVal(self.__root)

    # def getAll(self):
    #     self.__customerBST.getAll()

    # def reset(self):
    #     self.setBST('id')
    #     self.__customerBST.reset()


# c = Customer()
# c.setBST('id')
# c.setID()
# # print(c.getID())
# c.setFirstName('John')
# c.setLastName('SMith')
# c.setContact('12345678')
# c.printDetail(c.getID())
# c.addCustomer()
# c.printDetail(1002)
# c.printList(50)
# c.setVals(200)
# c.printVal()
# c.setBST('firstName')
# c.setBST('lastName')
# c.setBST('id')
# c.search('id',200)
# c.getAll()
# print(c.smallest(), c.largest())
