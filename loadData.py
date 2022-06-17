from importlib import reload
import movies
import dvd
import customer


class LoadData:
    def __init__(self):
        self.movies = movies.Movies()
        self.dvd = dvd.DVD()
        self.customer = customer.Customer()
        # self.customerRenting = customer.Customer('renting')

    @property
    def getMovies(self):
        return self.movies

    @property
    def getDVD(self):
        return self.dvd

    @property
    def getCustomer(self):
        return self.customer


    def getCustomerRenting(self):
        import customer
        self.customerRenting = customer.Customer('renting')
        return self.customerRenting
