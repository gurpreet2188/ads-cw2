import crud


class Navigation:
    def __init__(self):
        self.__crud = crud.CRUD()

    def showDvdLists(self, pageNum):
        self.__crud.dvdList(pageNum)

    def showDvdDetails(self, id):
        self.__crud.dvdDetail(id)

    def upateDvdDetails(self, dataType):
        self.__crud.updateDvdDetail(dataType)

    def saveDetails(self, saveType, dataType=None):
        self.__crud.saveToFile(saveType, dataType)

    def searchTitle(self, searchText, pageNum):
        return self.__crud.searchdvd(searchText, pageNum)

    def showCustomerList(self, pageNum):
        self.__crud.customerList(pageNum)

    def showCustomerListRenting(self, pageNum):
        self.__crud.customerListRenting(pageNum)

    def showCustomerDetail(self, id):
        self.__crud.customerDetail(id)

    def showTransaction(self, dvdID, cusID):
        self.__crud.rentDvd(dvdID, cusID)

    def showTransactionReturn(self, dvdID, cusID):
        self.__crud.returnDVD(dvdID, cusID)

    def showAddCustomer(self):
        self.__crud.addCustomer()

    def showUpdateCustomer(self, cusID, dataType):
        self.__crud.updateCustomer(cusID, dataType)
