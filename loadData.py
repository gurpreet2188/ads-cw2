import movies, dvd, customer

class LoadData:
    def __init__(self) :
        self.movies = movies.Movies()
        self.dvd = dvd.DVD()
        self.customer = customer.Customer()
    @property
    def getMovies(self):
        # self.movies.setLinkedList()
        return self.movies
    @property
    def getDVD(self):
        # print('dvdv')
        # self.movies.setLinkedList()
        # self.movies.getLinkList().setPagesAndIndexes()
        return self.dvd
    @property
    def getCustomer(self):
        return self.customer