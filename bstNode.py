import time

from tomlkit import item
class BSTNode:
    def __init__(self, node, data, nodeType=None):
        self.node = node
        self.data = data
        self.nodeType = nodeType
        # self.index = None
        self.right = None
        self.left = None
        self.total = 1

    def insert(self, node, data, nodeType=None):
        if nodeType == 'id':
            if node == self.node:
                return

        if node < self.node:
            if self.left:
                self.left.insert(node, data, nodeType)
            else:
                self.left = BSTNode(node, data)
        else:
            if self.right:
                self.right.insert(node, data, )
            else:
                self.right = BSTNode(node, data)
        self.total += 1

    def delete(self, nodeVal):
        if self.node is None:
            return self

        if self.node == nodeVal:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            elif self.left is not None and self.right is not None:
                smallest = self.right.getSmallestVal()
                self.node = smallest.node
                self.data = smallest.data
                self.right = self.right.delete(self.node)
        elif nodeVal < self.node:
            if self.left:
                self.left = self.left.delete(nodeVal)
        else:
            if self.right:
                self.right = self.right.delete(nodeVal)
        return self
    
    # def addIndex(self):
    
    def update(self, node, data):
        current = self.searchNode(node)
        if current:
            print(current.data)
            current.data = data
            print(current.data)

    def searchNode(self, node):
        if self.node == node:
            return self
        elif node < self.node:
            if self.left:
                return self.left.searchNode(node)
        else:
            if self.right:
                return self.right.searchNode(node)
        return False

    def getSmallestVal(self):
        if self.left is None:
            return self
        return self.left.getSmallestVal()
    
    def getLargestVal(self):
        if self.right is None:
            return self
        return self.right.getLargestVal()

    def getTotal(self):
        return self.total

    def inorder(self):
        items = []
        items += self.left.inorder() if self.left else []
        items.append(self)
        items += self.right.inorder()if self.right else []
        return items

    def print(self):
        print(self.right.node)
        

    def splitList(self, pageNum, start, end, totalPages, total):
        items = []
        # print(index)
        items += self.left.splitList(pageNum, start,
                                     end, totalPages, total) if self.left else []
        # if self.index:
        #     self.index = None
        # if self.index is None:
        #     self.index = 0
        # print(start[pageNum], end[pageNum])
        if pageNum == 1:
            if start[pageNum - 1] <= self.node <= end[pageNum - 1]:
                items.append(self)
        elif 1 < pageNum < totalPages:
            if start[pageNum - 1] < self.node <= end[pageNum - 1]:
                items.append(self)
        elif pageNum == totalPages:
            if start[pageNum - 1] < self.node <= total:
                items.append(self)
        items += self.right.splitList(pageNum, start,
                                      end, totalPages, total)if self.right else []
        # self.index += 1
        return items


class BSTWrapper:
    def __init__(self):
        self.root = None
        self.totalPages = 0
        self.start = []
        self.end = []
        self.total = 1

    def setRoot(self, node, data):
        self.root = BSTNode(node, data)
        return self.root

    def insert(self, node, data):
        if self.root is not None:
            self.root.insert(node, data)

    def delete(self, node):
        return self.root.delete(node)
    
    def update(self, node, data):
        return self.root.update(node, data)

    def inorder(self):
        return self.root.inorder()

    def getItems(self):
        if self.root:
            return self.root.getItems()
        
    def getLargestNode(self):
        if self.root:
            return self.root.getLargestVal()
    
    def getSmallestNode(self):
        if self.root:
            return self.root.getSmallestVal()

    def search(self, node):
        if self.root:
            return self.root.searchNode(node)

    def setPages(self):
        items = self.root.inorder()
        self.total = items[-1].node
        print(items[19].node, items[39].node, items[59].node, items[79].node, items[99].node)
        for i in range(0, len(items), 20):
            if i == 0:
                self.start.append(items[0].node)
            else:
                self.start.append(items[i - 1].node)
                self.end.append(items[i - 1].node)
            self.totalPages += 1
            # time.sleep(3)
        print(self.start, self.end)
        
        
    def splitList(self, pageNum):
        return self.root.splitList(pageNum, self.start, self.end, self.totalPages, self.total)


