class DLinkedList:
    class _node:
        def __init__(self, data=None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        self.direction = 'r'

    def __len__(self):
        return self._size

    def print(self):
        printItem = self.head
        while printItem is not None:
            print(printItem.data)
            printItem = printItem.next
        print('Qty of elements: ', self._size)

    def printBack(self):
        printItem = self.tail
        while printItem is not None:
            print(printItem.data)
            printItem = printItem.prev

    def pushFront(self, data):
        self._size += 1
        if self.head == None:
            self.head = self.tail = DLinkedList._node(data)
        else:
            self.head = DLinkedList._node(data, self.head)
            self.head.next.prev = self.head

    def pushBack(self, data):
        self._size += 1
        newNode = DLinkedList._node(data)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insertByIndex(self, index, data):
        if index > self._size or index < 0:
            raise Exception('Entered index is out of range')
        self._size += 1
        if index == 0:
            self.pushFront(data)
        elif index == self._size:
            self.pushFront(data)
        elif index <= self._size // 2:
            insertItem = self.head
            for i in range(index - 1):
                insertItem = insertItem.next
            insertItem.next = DLinkedList._node(data, insertItem.next, insertItem )
            insertItem.next.next.prev = insertItem.next
        elif index > self._size // 2:
            newNode = DLinkedList._node(data)
            insertItem = self.tail
            for i in range(self._size, index + 1, -1):
                insertItem = insertItem.prev
                
          

    def popFront(self):
        if self._size == 0:
            raise Exception('List is empty')
        self._size -= 1
        if self.head.next is None:
            popFrontData = self.head.data
            self.head = None
            self.tail = None
            return popFrontData
        else:
            popFrontData = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return popFrontData
                          
    def popBack(self):
        if self._size == 0:
            raise Exception('List is empty')
        if self.tail.prev is None:
            popBackData = self.tail.data
            self.head = None
            self.tail = None
        else:
            popBackData = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            return popBackData         
        
       

    def __iter__(self):
        if self.direction == 'r':
            self.it = self.head
        else:
            self.it = self.tail
        return self

    def __next__(self):
        if self.it:
            data = self.it.data
            if self.direction == 'r':
                self.it = self.it.next
            else:
                self.it = self.it.prev
            return data
        raise StopIteration


ls = DLinkedList()
ls2 = DLinkedList()
ls.pushFront('Front 1')
#ls.pushFront('Front 2')
#ls.pushFront('Front3')
#ls.pushFront('Front4')
#ls.pushFront('Front5')
#ls.pushBack('Back 132')
#ls.pushBack('Back200')
##ls.pushBack('300')
#ls.pushBack('400')
#ls.pushBack('500')
#ls.pushBack('600')
#ls.pushBack('700')
#ls.pushBack('800')
#ls.pushBack('900')
#ls.insertByIndex(3, '=INSERT=')
#ls.popFront()
#ls.popFront()
#ls.popFront()

ls.popBack()
#ls.popBack()
#ls.popBack()
#ls.popBack()
#ls.popBack()




# r: from left to right, l: from left to right
#ls.pushFront('1111111111')
#ls.printBack()
# print()
# ls.print()


print()

for i in ls:
    print(i)




