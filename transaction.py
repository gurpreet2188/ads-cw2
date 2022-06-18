import printHelper
# import loadData
# import time

class Transaction:

    def __init__(self, dvd, customer):
        # self.__data = loadData.LoadData()
        self.__dvd =  dvd
        self.__customer = customer
        # self.__customerRenting = self.__data.getCustomerRenting()
        self.__print = printHelper.PrintHelper()

    def rentDvd(self, dvdID, cusID):
        # print(dvdID, cusID)
        # self.__dvd.setID(dvdID)
        # self.__dvd.setCopies()
        copies = self.__dvd.getCopies()
        if int(copies) > 0:
            self.__customer.setVals(cusID)
            customerDVDID = self.__customer.getRenting()
            if customerDVDID != []:
                for cd in customerDVDID:
                    if str(cd) == str(dvdID):
                        self.__print.printFooter('Customer is already renting this DVD')
                        return False
            newCopies = copies - 1
            self.__dvd.setCopies(newCopies)
            self.__dvd.updateCopies()
            self.__dvd.reset()
            customerDVDID.append(dvdID)
            
            self.__customer.setRenting(customerDVDID)
            self.__print.printFooter('Updated currently rented DVD details.')
            self.__customer.printDetail(cusID)
            self.__customer.update()
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
            self.__customer.update()

            # add copy back to stock
            self.__dvd.setID(dvdID)
            self.__dvd.setCopies()
            copies = self.__dvd.getCopies()
            self.__dvd.setCopies(copies+1)
            self.__customer.printDetail(cusID)
        else:
            return self.__print.printFooter('ID not found')
        
