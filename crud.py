# from importlib import reload
import loadData
import transaction
import movies
import dvd
import inputHelper
# import customer


class CRUD:
    def __init__(self):
        self.__data = loadData.LoadData()
        self.__customer = self.__data.customer
        self.__dvd = self.__data.dvd
        # self.__customerRenting = self.__data.customerRenting
        self.__transaction = transaction.Transaction(
            self.__dvd, self.__customer)
        self.__inputHelper = inputHelper.InputHelper()

    def addCustomer(self):
        msg1 = 'Enter First Name: '
        msg2 = 'Enter Last Name: '
        msg3 = 'Enter Contact Number: '

        newCustomer = self.__customer

        userInput = self.__inputHelper

        newCustomer.setID()
        # First name
        fName = userInput.stringInput(msg1, type='name')
        newCustomer.setFirstName(fName)

        # Last name
        lName = userInput.stringInput(msg2, type='name')
        newCustomer.setLastName(lName)

        # gender
        gender = userInput.stringInput('Enter gender: ', type='name')
        newCustomer.setGender(gender)
        # Contact
        contact = userInput.stringInput(msg3, type='number')
        newCustomer.setContact(contact)

        newCustomer.printDetail(int(newCustomer.getID()))

    def updateCustomer(self, cusID, dataType):
        userInput = self.__inputHelper
        msg1 = 'Change First Name: '
        msg2 = 'Chnage Last Name: '
        msg3 = 'Change Contact Number: '
        self.__customer.setVals(cusID)
        if dataType == 'firstName':
            fName = userInput.stringInput(msg1, type='name')
            self.__customer.setFirstName(fName)
        elif dataType == 'lastName':
            lName = userInput.stringInput(msg2, type='name')
            self.__customer.setFirstName(lName)
        elif dataType == 'gender':
            gender = userInput.stringInput('Change gender: ', type='name')
            self.__customer.setFirstName(gender)
        elif dataType == 'contact':
            contact = userInput.stringInput(msg3, type='number')
            self.__customer.setFirstName(contact)

    def deleteCustomer(self, cusID):
        self.__customer.setVals(cusID)
        self.__customer.printDetail(cusID)

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

        # Summary
        summary = userInput.stringInput(msgGenre, type='any')
        newMovie.setSummary(summary)

    def searchdvd(self, searchText, pageNum):
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

        # Summary
        elif dataType == 'summary':
            summary = userInput.stringInput(msgSummary, type='any')
            m.setSummary(summary)

        # Copies
        elif dataType == 'copies':
            copies = userInput.stringInput(msgCopies, type='number')
            dvds.setID(m.getID())
            dvds.setCopies(copies)

        m.printDetail()
        # self.__store.printCopies()

    def customerList(self, pageNum):

        # cus = customer.Customer('id')
        self.__customer.printList(pageNum)
        # cus.reset()

    def customerDetail(self, cusID):

        # cus = customer.Customer('id')
        self.__customer.printDetail(cusID)
        # cus.reset()

    def customerListRenting(self, pageNum):

        self.__data.getCustomerRenting().printList(pageNum)
        # cus.reset()

    def rentDvd(self, dvdID, cusID):

        self.__transaction.rentDvd(dvdID, cusID)

    def returnDVD(self, dvdID, cusID):

        self.__transaction.returnDvd(dvdID, cusID)

    def saveToFile(self, saveType, dataType=None):
        if dataType == 'customer':
            if saveType == 'new':
                self.__customer.addNewCustomerToBST()
                self.__customer.reloadPages()
                self.__customer.saveToFile()
                return
            elif saveType == 'update':
                self.__customer.update()
                return
            elif saveType == 'delete':
                self.__customer.update(updateType='delete')
                self.__customer.reloadPages()
                return
        else:
            m = movies.Movies()
            if saveType == 'update':
                m.updateDetails()
