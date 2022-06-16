import movies
import printHelper
import csvHelper
import linkedList


class DVD:
    def __init__(self):
        self.__id = None
        self.__copies = 0
        self.__csv = csvHelper.CSVReaderWriter()
        self.__mainList = self.__csv.reader('dvd.csv')
        self.__linkedList = linkedList.LinkedList()
        self.__movies = movies.Movies()
        self.__print = printHelper.PrintHelper()
        self.__head = None
        self.__movies.setLinkedList()
        self.setLinkedList()

    def setLinkedList(self):
       
        for i in self.__mainList:
            self.__linkedList.insert(i)

        self.__head = self.__linkedList.getHead()
        self.__movies.getLinkList().setPagesAndIndexes()
        self.setFilteredList()

    def setFilteredList(self):
        if self.__head == None:
            return
        copiesHead = self.__head
        moviesHead = self.__movies.getHead()
        while copiesHead and moviesHead:
            if int(copiesHead.data['copies']) == 0:
                print('yes')
                self.__movies.getLinkList().delete(moviesHead.data)
            copiesHead = copiesHead.next
            moviesHead = moviesHead.next

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

    def getID(self):
        return self.__id

    def getCopies(self):
        return self.__copies
    
    def getTotal(self):
        return self.__movies.getTotal()

    def printDetail(self, dvdID):
        movies = self.__movies
        check = movies.setDetail(dvdID)
        if check:
            if self.__id is None:
                self.setID(dvdID)
                self.setCopies()

            id = ''
            genre = ''
            cast = ''
            director = ''
            producer = ''
            company = ''
            rating = ''
            releaseDate = ''
            summary = ''

            def removeSlash(items):
                newString = ''
                for i in items:
                    if i == '/':
                        i = ','
                    newString += i
                return newString

            id = f'ID: {self.getID()}'
            
            detailHeader = f' Title: {movies.getTitle()}| Copies Available: {self.getCopies()} '

            genre = f'Genre: {removeSlash(movies.getGenre())}'

            cast = f'Cast: {removeSlash(movies.getCast())}'

            director = f'Director: {movies.getDirector()}'

            producer = f'Producer: {movies.getProducer()}'

            company = f'Company: {movies.getCompany()}'

            rating = f'Rating: {movies.getRating()}'

            releaseDate = f'Release Date: {movies.getRleaseDate()}'

            summary = f'Summary: {movies.getSummary()}'

            printList = [id, genre, cast, director,
                        producer, company, rating, releaseDate, summary]

            self.__print.printColumn(printList, 120, detailHeader)
        else:
            self.__print.printFooter('ID Not Found.')

    def printDVDList(self, pageNum):
        movies = self.__movies
        printHelper = self.__print
        cliList = []
        # movies.getLinkList().setPagesAndIndexes()
        splitList = movies.getLinkList().splitList(pageNum)
        if splitList:
            for i in splitList:
                cliList.append(f'ID: {i["id"]} -> {i["title"]}')

            printHelper.printColumn(cliList, 120, 'Available DVDs')
            printHelper.printFooter(
                f'Showing page {pageNum} of {self.__movies.getLinkList().getPageInfo()[2]}')
        else:
            printHelper.printFooter('404 page not found.')

    def getDVDTitle(self, dvdID):
        print(dvdID)
        self.__movies.setDetail(dvdID)
        return self.__movies.getTitle()

    def searchDVD(self, searchText, pageNum):
        movies = self.__movies
        results = movies.searchTitle(searchText)
        # results = movies.getLinkList().findSimilar(searchText, 'title')
        if results:
            self.__movies.getLinkList().setPagesAndIndexes()
            self.printDVDList(pageNum)
            self.reset()
        else:
            self.__print.printFooter(f"No match found for: ',{searchText}")
        return results
        
    def reset(self):
        self.__linkedList.reset()
        self.__movies.reset()
        self.setLinkedList()
        

    def saveToFile(self):
        header = ['id', 'copies']
        row = {
            'id': self.getID(),
            'copies': self.getCopies()
        }
        self.__csv.writer('dvd.csv', row, header)
        

# d = DVD()
# d.setLinkedList()
# d.printDVDList(1)
# d.printDetail(200)
# print(d.getTotal())
# d.searchDVD('harry')
# print(d.getTotal())
# d.printList(1)
# d.reset()
# print(d.getTotal())
# d.printDetail(21)
