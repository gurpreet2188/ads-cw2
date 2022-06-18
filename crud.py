import dvd
import inputHelper
import printHelper
import customer


class CRUD:
    def __init__(self):
        
        self.__dvd = dvd.DVD()
        self.__movies = self.__dvd.getMovies()
        self.__customer = customer.Customer(self.__dvd)
        self.__inputHelper = inputHelper.InputHelper()
        self.__print = printHelper.PrintHelper()

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
        newMovie = self.__movies
        userInput = self.__inputHelper
        msgTitle = 'Enter Movie Title: '
        msgName = 'Enter name: '
        msgRating = 'Enter Rating: '
        msgGenre = 'Enter Genre: '

        # ID
        newMovie.setID()
        # Title
        title = userInput.stringInput(msgTitle, type='any')
        newMovie.setTitle(title)

        # ReleaseDate
        releaseDate = userInput.dateInput('Enter Release Date: ',)
        newMovie.setReleaseDate(releaseDate)

        # Cast
        cast = userInput.stringInput('Eneter movie stars (\'/\' seprated): ', type='name')
        newMovie.setCast(cast)

        # Director
        director = userInput.stringInput('Eneter director name: ', type='name')
        newMovie.setDirector(director)

        # Producer
        producer = userInput.stringInput('Enter Producer name: ', type='name')
        newMovie.setProducer(producer)

        # Company
        company = userInput.stringInput('Enter company name: ', type='any')
        newMovie.setCompany(company)

        # Rating
        rating = userInput.stringInput('Enter movie rating: ', type='number')
        newMovie.setRating(rating)

        # Genre
        genre = userInput.stringInput('Enter movie genre (\'/\' seprated): ', type='name')
        newMovie.setGenre(genre)

        # Summary
        summary = userInput.stringInput('Enter movie summary: ', type='any')
        newMovie.setSummary(summary)

        copies = userInput.stringInput(
            'Enter Copies Available: ', type='number')
        self.__dvd.setID(newMovie.getID())
        self.__dvd.setCopies(int(copies))

    def searchdvd(self, searchText, pageNum):
        return self.__dvd .searchDVD(searchText, pageNum)

    def dvdList(self, pageNum):
        self.__dvd .printDVDList(pageNum)

    def dvdDetail(self, dvdID):

        self.__dvd .printDetail(dvdID)

    def updateDvdDetail(self, dataType):
        m = self.__movies
        dvds = self.__dvd
        userInput = self.__inputHelper
        msgTitle = 'Enter Movie Title: '
        msgSummary = 'Enter New Summary'
        msgCopies = 'Enter Number of Copies available in store.'

        # Title
        if dataType == 'title':
            title = userInput.stringInput(msgTitle, type='any')
            m.setTitle(title)
            print('New title set as: ', m.getTitle())

        # Summary
        elif dataType == 'summary':
            summary = userInput.stringInput(msgSummary, type='any')
            m.setSummary(summary)
            print('New summary set as: ', m.getSummary())

        # Copies
        elif dataType == 'copies':
            copies = userInput.stringInput(msgCopies, type='number')
            dvds.setID(m.getID())
            dvds.setCopies(copies)
            print('Current Copies for this DVD is: ', self.__dvd.getCopies())

        # self.__dvd.printDetail(m.getID())
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
        self.__customer.setBST('retning')
        self.__customer.printList(1)
        # self.__data
        # self.__data.getCustomerRenting().printList(pageNum)
        # cus.reset()

    def rentDvd(self, dvdID, cusID):
        self.__dvd.setVals(dvdID)
        copies = self.__dvd.getCopies()
        if int(copies) > 0:
            self.__customer.setVals(cusID)
            customerDVDID = self.__customer.getRenting()
            if customerDVDID != []:
                for cd in customerDVDID:
                    if str(cd) == str(dvdID):
                        self.__print.printFooter('Customer is already renting this DVD')
                        return False
            newCopies = int(copies) - 1
            self.__dvd.setCopies(newCopies)
            self.__dvd.updateCopies()
            self.__dvd.reset()
            self.__customer.setVals(cusID)
            r = self.__customer.getRenting()
            r.append(str(dvdID))
            self.__customer.setRented(r)
            self.__print.printFooter('Updated currently rented DVD details.')
            self.__customer.update()
            self.__customer.printDetail(cusID)
        else:
            self.__print.printFooter('Sorry, no copies available for this DVD')

    def returnDVD(self, dvdID, cusID):
        self.__customer.setVals(cusID)
        self.__customer.printDetail(cusID)
        # self.__dvd.setID(dvdID)
        self.__dvd.setVals(dvdID)
        rendtingDVDID = self.__customer.getRenting()
        dvdID = str(dvdID)  # convert int ID to str for storing
        if dvdID in rendtingDVDID and self.__dvd.getID():

            # remove DVD ID from customer's renting and add it in rented
            self.__customer.setVals(cusID)
            renting = self.__customer.getRenting()
            rented = self.__customer.getRented()
            renting.remove(dvdID)
            self.__customer.setRenting(renting)
            rented.append(dvdID)
            self.__customer.setRented(rented)
            self.__customer.update()
            self.__customer.printDetail(cusID)
            self.__customer.reset()

            # add copy back to stock
            
            copies = int(self.__dvd.getCopies())
            self.__dvd.setCopies(copies+1)
            self.__dvd.updateCopies('update')
            self.__dvd.reset()
            # self.__customer.printDetail(cusID)
        else:
            return self.__print.printFooter('ID not found')

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
            if saveType == 'new':
                self.__movies.addToFile()
                self.__dvd.addNewDVD()
            elif saveType == 'update':
                self.__movies.updateDetails()
                self.__dvd.updateCopies()
            elif saveType == 'delete':
                self.__movies.updateDetails('delete')
                self.__dvd.updateCopies('delete')



# c = CRUD()
# c.rentDvd(200, 32)
# # c.rentDvd(2, 30)
