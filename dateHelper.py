import datetime

class Date:
    def __init__(self):
        pass
    
    def verifyDate(self, date):
        formats = ('%d-%m-%Y', '%d/%m/%Y', '%d.%m.%Y' )
        verified = False
        for i in formats:
            try:
                datetime.datetime.strptime(date,i)
                verified = True
            except ValueError as e:
                pass
        return verified