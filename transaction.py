import printHelper
import loadData


class Transaction:

    def __init__(self):
        self.__data = loadData.LoadData()
        self.__dvd =  self.__data.dvd
        self.__customer = self.__data.customer
        self.__print = printHelper.PrintHelper()

    def rentDvd(self, dvdID, cusID):
        self.__dvd.setID(dvdID)
        self.__dvd.setCopies()
        copies = self.__dvd.getCopies()
        if int(copies) > 0:
            self.__customer.setVals(cusID)
            customerDVDID = self.__customer.getRenting()
            if customerDVDID != []:
                for cd in customerDVDID:
                    if cd == dvdID:
                        return self.__print.printFooter('Customer is already renting this DVD')
            newCopies = copies - 1
            self.__dvd.setCopies(newCopies)
            customerDVDID.append(dvdID)
            self.__customer.setRenting(customerDVDID)
            self.__print.printFooter('Updated currently rented DVD details.')
            self.__customer.printDetail(cusID)
            self.__customer.update(cusID)
        else:
            self.__print.printFooter('Sorry, no copies available for this DVD')

    def returnDvd(self, dvdID, cusID):
        self.__customer.setVals(cusID)
        self.__customer.printDetail(cusID)
        rendtingDVDID = self.__customer.getRenting()
        dvdID = str(dvdID) # convert int ID to str for storing
        if dvdID in rendtingDVDID:
            
            # remove DVD ID from customer's renting and add it in rented
           
            renting = self.__customer.getRenting()
            rented = self.__customer.getRented()
            renting.remove(dvdID)
            self.__customer.setRenting(renting)
            rented.append(dvdID)
            self.__customer.setRented(rented)

            # add copy back to stock
            self.__dvd.setID(dvdID)
            self.__dvd.setCopies()
            copies = self.__dvd.getCopies()
            self.__dvd.setCopies(copies+1)
        else:
            return self.__print.printFooter('ID not found')
      
        
                
# t = Transaction()

# t.rentDvd(18,20)
