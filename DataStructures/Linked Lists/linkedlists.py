class Node(object):

    def __init__(self, data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def addFirst(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def getLength(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def findOrdered(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")

    def findUnordered(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def addLast(self, data):
        last = None
        current = self.head
        while current:
            last = current.get_next()
        if last:
            last.set_next(Node(data))
        else:
            self.addFirst(data)

    def addInOrder(self, data):
        if str(data) < self.head:
            self.addFirst(data)
        elif str(data) > self.head:
            self.addLast(data)

    def copyList(self, list):
        new_list = LinkedList(Node(self.head))