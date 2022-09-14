class LinkedList:
    class _node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.firstItem = None
        self._size = 0

    def __len__(self):
        return self._size

    def addAtBegin(self, data):
        self._size += 1
        newNode = LinkedList._node(data)
        newNode.next = self.firstItem
        self.firstItem = newNode

    def addAtEnd(self, data):
        self._size += 1
        newNode = LinkedList._node(data)
        if self.firstItem is None:
            self.firstItem = newNode
            return
        last = self.firstItem
        while (last.next):
            last = last.next
        last.next = newNode

    def insertAtIndex(self, index, data): #DRY
        newNode = LinkedList._node(data)
        self._size += 1
        if index == 0:
            newNode.next = self.firstItem
            self.firstItem = newNode
        elif index > 0:
            insertItem = self.firstItem
            for i in range(index - 1):
                insertItem = insertItem.next
            newNode.next = insertItem.next
            insertItem.next = newNode

    def remove(self, index):
        if index < 0 or index > self._size - 1:
            # k = 0
            raise Exception('def remove: Entered index is out of range')
        self._size -= 1
        if index == 0:
            self.firstItem = self.firstItem.next
        else:
            item = self.firstItem
            for i in range(index - 1):
                item = item.next
            item.next = item.next.next

    def __iter__(self):
        self.it = self.firstItem
        return self

    def __next__(self):
        if self.it:
            data = self.it.data
            self.it = self.it.next
            return data
        raise StopIteration


if __name__ == "__main__":
    ls = LinkedList()
    ls.addAtBegin('123')
    ls.addAtBegin('456')
    ls.addAtBegin('start')

    # ls.addAtBegin('789')
    ls.addAtEnd('end1')
    ls.addAtEnd('end2')
    ls.insertAtIndex(2, '=INSERT=')
    ls.remove(4)
    # ls.remove(0)
    # ls.addAtEnd('end1')
    # ls.insertAfterItem('AAA', 'YYY')
    # ls.delAtStart()
    # ls.delAtEnd()

    for i in ls:
        print('>>>',i)

    a = list(map(str.upper, ls))
    print(a)

if t == 0:
    
