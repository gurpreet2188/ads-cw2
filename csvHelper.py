# A simple class to handle the reading and writing
# of the data from csv files.
import csv
import random


class CSVReaderWriter:
    def __init__(self):
        pass  #

    # read from csv file and output the data in
    # Dictionary data type with csv's DictReader
    # Parameters: file -> name of the file to read
    # data from.
    def reader(self, file):
        temp = []
        try:
            with open(file, 'r') as f:
                r = csv.DictReader(f, delimiter=',')
                for i in r:
                    temp.append(i)
        except ValueError as e:
            return print(e)
        return temp

    # Return the date stored in variable from csv file
    # def getReaderData(self):
    #     return self.__readData

    # Append the data to csv files in same Dictionary
    # data type
    # Parameters: file -> name of the file to append
    #             data to.
    #             row -> a single row of data in Dictionary
    #             data type.
    #             header -> header for the csv file.
    def writer(self, file, row, header):
        try:
            with open(file, 'a', newline='') as file:
                w = csv.DictWriter(file, header)
                w.writerow(row)
        except ValueError as e:
            print('File Error!!')

    def writerNew(self, file, rows, header):
        with open(file, 'w', newline='') as file:
            w = csv.DictWriter(file, header)
            w.writeheader()
            w.writerows(rows)


# c = CSVReaderWriter()
# old = c.reader('movies.csv')
# newRows = []
# for i in old:
#     randNumLow = random.randint(2,5)
#     randNumHigh = random.randint(6,10)
#     if float(i['rating']) >= 7:
#         i['copies'] = randNumHigh
#     else:
#         i['copies'] = randNumLow
#     row = {
#         'id': i['id'],
#         'copies': i['copies']
#     }
#     newRows.append(row)


# c.writerNew('store.csv',newRows, ['id','copies'])
# print(newRows[0])


# male
# c = CSVReaderWriter()

# maleList = c.reader('male.csv')

# splitNamesM = []
# rowsM = []
# for n,i in enumerate(maleList):
#     splitNamesM.append(i['names'].split(" "))
#     rowM = {
#         'firstName' : splitNamesM[n][0],
#         'lastName' : splitNamesM[n][1],
#         'gender': 'male'
#     }
#     rowsM.append(rowM)

# print(splitNamesM[0], rowsM[0])

# c = CSVReaderWriter()

# femaleList = c.reader('female.csv')

# splitNamesF = []
# rowsF = []
# for n,i in enumerate(femaleList):
#     splitNamesF.append(i['names'].split(" "))
#     rowF = {
#         'firstName' : splitNamesF[n][0],
#         'lastName' : splitNamesF[n][1],
#         'gender': 'female'
#     }
#     rowsF.append(rowF)

# # print(splitNamesF[0], rowsF[0])

# finalList = rowsM + rowsF

# random.shuffle(finalList)
# id = 1
# for i in finalList:
#     i['id'] = str(id)
#     id += 1

# c.writerNew('customer.csv', finalList, ['id','firstName', 'lastName', 'gender'])
# print(finalList[0:10])

# c = CSVReaderWriter()
# customer = c.reader('customer.csv')


# for i in customer:
#     rented = []
#     renting = []
#     idsStr = ''
#     rentedDvds = random.randint(1, 4)
#     rentingDvds = random.randint(0, 3)
#     if rentedDvds == 0:
#         rented = ''
#     else:
#         for r in range(rentedDvds):
#             ids = random.randint(1, 3601)
#             rented.append(ids)
#     if rentingDvds == 0:
#         renting = ''
#     else:
#         for r in range(rentingDvds):
#             ids = random.randint(1, 3601)
#             renting.append(ids)

#     i['rented'] = '/'.join(str(x)for x in rented)
#     i['renting'] = '/'.join(str(x)for x in renting)

# random.shuffle(customer)

# c.writerNew('customer.csv', customer, ['id','firstName', 'lastName', 'gender', 'rented', 'renting'])


# csvH = CSVReaderWriter()

# cus = csvH.reader('customer.csv')
# num = csvH.reader('num.csv')

# for c, n in list(zip(cus, num)):
#     c['number'] = n['number']
#     # c['contact'] = num['number']


# csvH.writerNew('customern.csv', cus, [
#                'id', 'firstName', 'lastName', 'gender', 'number', 'rented', 'renting'])

# def removeSlash(items):
#             newString = ''
#             for i in items:
#                 if i == '/':
#                     i = ','
#                 newString += i
#             return newString

# csvH = CSVReaderWriter()

# cus = csvH.reader('customer.csv')



# for c in cus:
#     c['rented'] = f'{removeSlash(c["rented"])}'
#     c['renting'] = f'{removeSlash(c["renting"])}'


# csvH.writerNew('customern.csv', cus, [
#                'id', 'firstName', 'lastName', 'gender', 'number', 'rented', 'renting'])


