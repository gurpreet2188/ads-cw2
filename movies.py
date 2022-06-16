import linkedList
import csvHelper


class Movies:
    def __init__(self):
        # movie properties
        self.__id = None
        self.__title = None
        self.__releaseDate = None
        self.__cast = []
        self.__director = None
        self.__producer = None
        self.__company = None
        self.__rating = None
        self.__genre = None
        self.__summary = None
        self.__copies = 0
        self.__searchResults = []
        # linkedlist
        self.__linkedList = linkedList.LinkedList()
        self.__csv = csvHelper.CSVReaderWriter()
        self.__head = None  # head node for movies
        # self.setLinkedList()

    def setLinkedList(self):

        # load the data from csv and
        # get the normal list from csv file
        movies = self.__csv.reader('movies.csv')
        for i in movies:
            # insert every item from list into linkedlist
            self.__linkedList.insert(i)
        # self.__linkedList.setPagesAndIndexes()
        self.__head = self.__linkedList.getHead()  # get the linked list from class

    def setID(self, id):
        self.__id = id

    def setTitle(self, title):
        self.__title = title

    def setReleaseDate(self, releaseDate):
        self.__releaseDate = releaseDate

    def setCast(self, cast):
        self.__cast = cast

    def setDirector(self, director):
        self.__director = director

    def setProducer(self, producer):
        self.__producer = producer

    def setCompany(self, company):
        self.__company = company

    def setRating(self, rating):
        self.__rating = rating

    def setGenre(self, genre):
        self.__genre = genre

    def setSummary(self, summary):
        self.__summary = summary

    def setCopies(self, num):
        self.__copies = num

    def getID(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getRleaseDate(self):
        return self.__releaseDate

    def getCast(self):
        return self.__cast

    def getDirector(self):
        return self.__director

    def getProducer(self):
        return self.__producer

    def getCompany(self):
        return self.__company

    def getRating(self):
        return self.__rating

    def getGenre(self):
        return self.__genre

    def getSummary(self):
        return self.__summary

    def getCopies(self):
        return self.__copies

    def getHead(self):
        return self.__head
    
    def getTotal(self):
        return self.__linkedList.getTotal()

    def updateDetails(self):
        header = ['id', 'genre', 'title', 'cast', 'director',
                  'producer', 'company', 'rating', 'rDate', 'summary']
        updatedList = []
        current = self.__head
        while current:
            if int(current.data['id']) == int(self.getID()):
                current.data['title'] = str(self.getTitle())
                current.data['genre'] = str(self.getGenre())
                current.data['cast'] = str(self.getCast())
                current.data['director'] = str(self.getDirector())
                current.data['producer'] = str(self.getProducer())
                current.data['rating'] = str(self.getRating())
                current.data['company'] = str(self.getCompany())
                current.data['summary'] = str(self.getSummary())
                current.data['rDate'] = str(self.getRleaseDate())
            updatedList.append(current.data)
            current = current.next

        self.__csv.writerNew('temp.csv', updatedList, header)

    def searchTitle(self, searchText):
        results = self.__linkedList.findSimilar(
            searchText, 'title')
        if results:
            return True
        else:
            False

    def setDetail(self, id):
        if self.__head == None:
            return
        current = self.__head
        found = False
        while current:
            if int(current.data['id']) == int(id):
                self.setID(id)
                self.setGenre(current.data['genre'])
                self.setTitle(current.data['title'])
                self.setCast(current.data['cast'])
                self.setDirector(current.data['director'])
                self.setProducer(current.data['producer'])
                self.setCompany(current.data['company'])
                self.setRating(current.data['rating'])
                self.setReleaseDate(current.data['rDate'])
                self.setSummary(current.data['summary'])
                found = True
                break
            current = current.next
        return found

    def getLinkList(self):
        return self.__linkedList
    
    def reset(self):
        self.__linkedList.reset()
        self.setLinkedList()
        self.__linkedList.setTotal(0)

    
