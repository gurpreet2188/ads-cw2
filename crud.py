import staff
import transaction
import movies
import dvd
import customer
# import loadData



class CRUD:
    def __init__(self):
        # self.__data = loadData.LoadData()
        self.__customer = customer.Customer()
        self.__staff = staff.Staff()
        # self.__movies = self.__data.movies
        # self.__dvd = self.__data.dvd
        self.__transaction = transaction.Transaction()
        

    def addCustomer(self):
        msg1 = 'Enter First Name: '
        msg2 = 'Enter Last Name: '
        msg3 = 'Enter Contact Number: '
        msg4 = 'Enter Address: '

        newCustomer = self.__customer

        userInput = self.__inputHelper

        # First name
        fName = userInput.stringInput(msg1, type='name')
        newCustomer.setFirstName(fName)

        # Last name
        lName = userInput.stringInput(msg2, type='name')
        newCustomer.setLastName(lName)

        # Contact
        contact = userInput.stringInput(msg3, type='number')
        newCustomer.setContact(contact)

        # Address
        address = userInput.stringInput(msg4, type='any')
        newCustomer.setAddress(address)
        

    def addStaff(self):
        msg1 = 'Enter First Name: '
        msg2 = 'Enter Last Name: '
        msg3 = 'Enter Employee Type: '

        newStaff = self.__staff

        userInput = self.__inputHelper

        # First name
        fName = userInput.stringInput(msg1, type='name')
        newStaff.setFirstName(fName)

        # Last name
        lName = userInput.stringInput(msg2, type='name')
        newStaff.setLastName(lName)

        # Position
        position = userInput.stringInput(msg3, type='name')
        newStaff.setType(position)

    def addMovie(self):
        newMovie = movies.Movies()
        userInput = self.__inputHelper
        msgTitle = 'Enter Movie Title: '
        msgName = 'Enter name: '
        msgRating = 'Enter Rating: '
        msgGenre = 'Enter Genre: '

        # Title
        title = userInput.stringInput(msgTitle, type='any')
        newMovie.setTitle(title)

        # ReleaseDate
        releaseDate = userInput.dateInput(msgTitle)
        newMovie.setReleaseDate(releaseDate)

        # Cast
        cast = userInput.stringInput(msgName, type='name')
        newMovie.setCast(cast)

        # Director
        director = userInput.stringInput(msgName, type='name')
        newMovie.setDirector(director)

        # Producer
        producer = userInput.stringInput(msgName, type='name')
        newMovie.setProducer(producer)

        # Company
        company = userInput.stringInput(msgName, type='any')
        newMovie.setCompany(company)

        # Rating
        rating = userInput.stringInput(msgRating, type='number')
        newMovie.setRating(rating)

        # Genre
        genre = userInput.stringInput(msgGenre, type='name')
        newMovie.setGenre(genre)
        
        #Summary
        summary = userInput.stringInput(msgGenre, type='any')
        newMovie.setSummary(summary)
        
    def searchdvd(self,searchText, pageNum):
        m = movies.Movies()
        dvds = dvd.DVD()
        return dvds.searchDVD(searchText, pageNum)
        
    def dvdList(self, pageNum):
        m = movies.Movies()
        dvds = dvd.DVD()
        dvds.printDVDList(pageNum)
    
    def dvdDetail(self, dvdID):
        m = movies.Movies()
        dvds = dvd.DVD()
        dvds.printDetail(dvdID)
            
    def updateDvdDetail(self, dataType):
        m = movies.Movies()
        dvds = dvd.DVD()
        userInput = self.__inputHelper
        msgTitle = 'Enter Movie Title: '
        msgSummary = 'Enter New Summary'
        msgCopies = 'Enter Number of Copies available in store.'
        
        # Title
        if dataType == 'title':
            title = userInput.stringInput(msgTitle, type='any')
            m.setTitle(title)
            
        #Summary
        elif dataType == 'summary':
            summary = userInput.stringInput(msgSummary, type='any')
            m.setSummary(summary)
        
        #Copies
        elif dataType == 'copies':
            copies = userInput.stringInput(msgCopies, type='number')
            dvds.setID(m.getID())
            dvds.setCopies(copies)
            
        m.printDetail()
        # self.__store.printCopies()
        
        
    def customerList(self,pageNum):
        self.__customer.printList(pageNum)
        
    def customerDetail(self, cusID):
        self.__customer.printDetail(cusID)
        
    def rentDvd(self, dvdID, cusID):
        self.__transaction.rentDvd(dvdID, cusID)
        
    def returnDVD(self, dvdID, cusID):
        self.__transaction.returnDvd(dvdID, cusID)
        
    def saveToFile(self,saveType):
        m = movies.Movies()
        if saveType == 'update':
            m.updateDetails()
            
            