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
        last = None:
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


def main():

    print ("\n\n***************************************************************")
    print ("Test of addFirst:  should see 'node34...node0'")
    print ("***************************************************************")
    myList1 = LinkedList()
    for i in range(35):
        myList1.addFirst("node"+str(i))

    print (myList1)

    print ("\n\n***************************************************************")
    print ("Test of addLast:  should see 'node0...node34'")
    print ("***************************************************************")
    myList2 = LinkedList()
    for i in range(35):
        myList2.addLast("node"+str(i))

    print (myList2)


    print ("\n\n***************************************************************")
    print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
    print ("***************************************************************")
    greekList = LinkedList()
    greekList.addInOrder("gamma")
    greekList.addInOrder("delta")
    greekList.addInOrder("alpha")
    greekList.addInOrder("epsilon")
    greekList.addInOrder("omega")
    print (greekList)



    print ("\n\n***************************************************************")
    print ("Test of getLength:  should see 35, 5, 0")
    print ("***************************************************************")
    emptyList = LinkedList()
    print ("   Length of myList1:  ", myList1.getLength())
    print ("   Length of greekList:  ", greekList.getLength())
    print ("   Length of emptyList:  ", emptyList.getLength())


    print ("\n\n***************************************************************")
    print ("Test of findUnordered:  should see True, False")
    print ("***************************************************************")
    print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
    print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

    print ("\n\n***************************************************************")
    print ("Test of findOrdered:  should see True, False")
    print ("***************************************************************")
    print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
    print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))


    print ("\n\n***************************************************************")
    print ("Test of delete:  should see 'node25 found', 'node34 found',")
    print ("   'node0 found', 'node40 not found'")
    print ("***************************************************************")
    print ("   Deleting 'node25' (random node) from myList1: ")
    if myList1.delete("node25"):
        print ("      node25 found")
    else:
        print ("      node25 not found")
    print ("   myList1:  ")
    print (myList1)


    print ("   Deleting 'node34' (first node) from myList1: ")
    if myList1.delete("node34"):
        print ("      node34 found")
    else:
        print ("      node34 not found")
    print ("   myList1:  ")
    print (myList1)


    print ("   Deleting 'node0'  (last node) from myList1: ")
    if myList1.delete("node0"):
        print ("      node0 found")
    else:
        print ("      node0 not found")
    print ("   myList1:  ")
    print (myList1)


    print ("   Deleting 'node40' (node not in list) from myList1: ")
    if myList1.delete("node40"):
        print ("      node40 found")
    else:
        print ("   node40 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("\n\n***************************************************************")
    print ("Test of copyList:")
    print ("***************************************************************")
    greekList2 = greekList.copyList()
    print ("   These should look the same:")
    print ("      greekList before delete:")
    print (greekList)
    print ("      greekList2 before delete:")
    print (greekList2)


    greekList2.delete("alpha")
    print ("   This should only change greekList2:")
    print ("      greekList after deleting 'alpha' from second list:")
    print (greekList)

    print ("      greekList2 after deleting 'alpha' from second list:")
    print (greekList2)
    greekList.delete("omega")
    print ("   This should only change greekList1:")
    print ("      greekList after deleting 'omega' from first list:")
    print (greekList)
    print ("      greekList2 after deleting 'omega' from first list:")
    print (greekList2)


    print ("\n\n***************************************************************")
    print ("Test of reverseList:  the second one should be the reverse")
    print ("***************************************************************")
    print ("   Original list:")
    print (myList1)
    print ("   Reversed list:")
    myList1Rev = myList1.reverseList()
    print (myList1Rev)


    print ("\n\n***************************************************************")
    print ("Test of sortList:  the second list should be the first one sorted")
    print ("***************************************************************")
    planets = LinkedList()
    planets.addFirst("Mercury")
    planets.addFirst("Venus")
    planets.addFirst("Earth")
    planets.addFirst("Mars")
    planets.addFirst("Jupiter")
    planets.addFirst("Saturn")
    planets.addFirst("Uranus")
    planets.addFirst("Neptune")
    planets.addFirst("Pluto!")

    print ("   Original list:")
    print (planets)
    print ("   Sorted list:")
    sortedPlanets = planets.sortList()
    print (sortedPlanets)


    print ("\n\n***************************************************************")
    print ("Test of isSorted:  should see False, True")
    print ("***************************************************************")
    print ("   Original list:")
    print (planets)
    print ("   Sorted: ", planets.isSorted())
    sortedPlanets = planets.sortList()
    print ("   After sort:")
    print (sortedPlanets)
    print ("   Sorted: ", sortedPlanets.isSorted())


    print ("\n\n***************************************************************")
    print ("Test of isEmpty:  should see True, False")
    print ("***************************************************************")
    newList = LinkedList()
    print ("New list (currently empty):", newList.isEmpty())
    newList.addFirst("hello")
    print ("(After adding one element:",newList.isEmpty())


    print ("\n\n***************************************************************")
    print ("Test of mergeList")
    print ("***************************************************************")
    list1 = LinkedList()
    list1.addLast("aardvark")
    list1.addLast("cat")
    list1.addLast("elephant")
    list1.addLast("fox")
    list1.addLast("lynx")
    print ("   first list:")
    print (list1)
    list2 = LinkedList()
    list2.addLast("bacon")
    list2.addLast("dog")
    list2.addLast("giraffe")
    list2.addLast("hippo")
    list2.addLast("wolf")
    print ("   second list:")
    print (list2)
    print ("   merged list:")
    list3 = list1.mergeList(list2)
    print (list3)


    print ("\n\n***************************************************************")
    print ("Test of isEqual:  should see True, False, True")
    print ("***************************************************************")
    print ("   First list:")
    print (planets)
    planets2 = planets.copyList()
    print ("   Second list:")
    print (planets2)
    print ("      Equal:  ",planets.isEqual(planets2))
    print (planets)
    planets2.delete("Mercury")
    print ("   Second list:")
    print (planets2)
    print ("      Equal:  ",planets.isEqual(planets2))
    print ("   Compare two empty lists:")
    emptyList1 = LinkedList()
    emptyList2 = LinkedList()
    print ("      Equal:  ",emptyList1.isEqual(emptyList2))


    print ("\n\n***************************************************************")
    print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
    print ("***************************************************************")
    dupList = LinkedList()
    print ("   removeDuplicates from an empty list shouldn't fail")
    newList = dupList.removeDuplicates()
    print ("   printing what should still be an empty list:")
    print (newList)
    dupList.addLast("giraffe")
    dupList.addLast("wolf")
    dupList.addLast("cat")
    dupList.addLast("elephant")
    dupList.addLast("bacon")
    dupList.addLast("fox")
    dupList.addLast("elephant")
    dupList.addLast("wolf")
    dupList.addLast("lynx")
    dupList.addLast("elephant")
    dupList.addLast("dog")
    dupList.addLast("hippo")
    dupList.addLast("aardvark")
    dupList.addLast("bacon")
    print ("   original list:")
    print (dupList)
    print ("   without duplicates:")
    newList = dupList.removeDuplicates()
    print (newList)

main()