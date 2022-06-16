import csvHelper
import linkedList
import printHelper
import movies


class Store:
    def __init__(self):
        self.__id = None
        self.__copies = []
        self.__csv = csvHelper.CSVReaderWriter()
        self.__mainList = self.__csv.reader('store.csv')

        self.__linkedList = linkedList.LinkedList()
        for i in self.__mainList:
            self.__linkedList.insert(i)

        self.__head = self.__linkedList.getHead()
        self.__dvd = movies.Movies()
       
        self.__print = printHelper.PrintHelper()

    def setID(self, id):
        self.__id = id

    def setCopies(self, copies=None):
        if copies == None and self.getID():
            current = self.__head
            while current:
                if int(current.data['id']) == int(self.getID()):
                    self.__copies = int(current.data['copies'])
                current = current.next
        else:
            self.__copies = copies

    def printDvds(self, pageNum):
        dvdHead = self.__dvd.getHead()
        self.compare(self.__head, dvdHead)
        self.__dvd.printList(pageNum)

    def compare(self, copies, dvds):
        while copies and dvds:
            if int(copies.data['copies']) == 0:
                print('yes')
                self.__dvd.getLinkList().delete(dvds.data)
            copies = copies.next
            dvds = dvds.next

    def checkCopies(self, DVDids=None):
        if self.__head == None:
            return False
        current = self.__head
        while current:
            if int(current.data['copies']) > 0:
                self.__copies.append(current.data)
                current = current.next

        if self.__copies == []:
            return False

    def getID(self):
        return self.__id

    def getCopies(self):
        return self.__copies

    # def searchIDs(self, ids):
    #     current = self.__head
    #     if current == None:
    #         return
    #     return self.searchID(ids)

    # def searchIDs(self, ids):
    #     if self.__head == None:
    #         return
    #     copies = []
    #     for id in ids:
    #         copies.append(self.searchID(id))
    #     return copies

    # def searchID(self, id):
    #     current = self.__head
    #     while current:
    #         if int(current.data['id']) == int(id):
    #             return current.data
    #         current = current.next
    #     return False

    def printCopies(self):
        self.__print.printHeader(f'Copies available: {self.getCopies()} ')

    def updateCopies(self):
        header = ['id', 'copies']

        current = self.__head
        newList = []
        while current:
            if int(current.data['id']) == int(self.getID()):
                current.data['copies'] = str(self.getCopies())
            newList.append(current.data)
            current = current.next

        self.__csv.writerNew('storeTemp.csv', newList, header)

    def saveToFile(self):
        header = ['id', 'copies']
        row = {
            'id': self.getID(),
            'copies': self.getCopies()
        }
        self.__csv.writer('store.csv', row, header)


# s = Store()
# s.printDvds(1)
