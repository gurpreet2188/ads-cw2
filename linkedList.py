class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__total = 1
        self.__totalPages = 0
        self.__start = []
        self.__end = []

    def insert(self, val):
        if self.__head == None:
            self.__head = Node(val)
            return

        current = self.__head  # store the current head in vairable

        while (current.next):  # if current.next exist, loop through
            current = current.next  # reassign current to current.next

        # link next node with current node if next is None
        current.next = Node(val)
        self.__total += 1

    def delete(self, node):
        currentTemp = self.__head

        if currentTemp != None:
            if currentTemp.data == node:
                self.__head = currentTemp.next
                currentTemp = None
                self.__total -= 1
                return

        while currentTemp:
            if currentTemp.data == node:
                break
            previous = currentTemp
            currentTemp = currentTemp.next

        if currentTemp == None:
            return

        previous.next = currentTemp.next
        self.__total -= 1
        currentTemp = None

    def setTotal(self, total):
        self.__total = total

    def getTotal(self):
        return self.__total

    def getPageInfo(self):
        return [self.__start, self.__end, self.__totalPages]

    def getHead(self):
        return self.__head

    def printList(self):
        if self.__head == None:
            return
        current = self.__head
        while current:
            print(current.data)
            current = current.next

    def setPagesAndIndexes(self):
        self.__totalPages = 0
        self.__start = []
        self.__end = []
        for i in range(1, self.__total, 20):
            if i == 1:
                self.__start.append(0)
            else:
                self.__start.append(i - 1)
                self.__end.append(i - 2)
            self.__totalPages += 1
            # print(i)

    def splitList(self, pageNum):
        if self.__head == None:
            return
        # self.setPagesAndIndexes()

        head = self.__head
        cliList = []
        count = 0
        if pageNum == 1:
            while head:
                cliList.append(head.data)
                head = head.next
                count += 1
                if count >= 20:
                    break
            return cliList

        elif 1 < pageNum < self.getPageInfo()[2]:
            while head:
                if self.getPageInfo()[1][pageNum - 1] >= count >= self.getPageInfo()[0][pageNum - 1]:
                    cliList.append(head.data)
                head = head.next
                count += 1
            return cliList

        elif pageNum == self.getPageInfo()[2]:
            while head:
                if self.getTotal() >= count >= self.getPageInfo()[0][pageNum - 1]:
                    cliList.append(head.data)
                head = head.next
                count += 1
            return cliList
        else:
            return False

    def __iter__(self):
        node = self.__head
        while node is not None:
            yield node
            node = node.next

    def updateData(self, id, data):
        if self.__head == None:
            return False
        current = self.__head

        while current:
            if id == current.data['id']:
                current.data = data
                break
            current = current.next

        return False

    def findExact(self, searchText, searchType):
        if self.__head == None:
            return False
        current = self.__head

        while current:
            if searchText == current.data[searchType]:
                return current.data
            current = current.next

        return False

    def findSimilar(self, searchText, searchType):
        if self.__head == None:
            return False
        current = self.__head
        results = False
        while current:
            if searchText.lower() not in current.data[searchType].lower():
                self.delete(current.data)
                results = True
                # results.append(current.data)
            current = current.next

        return results
    
    def reset(self):
        self.__head = None
        self.__total = 1
        self.__totalPages = 0
        self.__start = []
        self.__end = []
