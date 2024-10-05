class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SortingCircularLinkedList:
    def __init__(self):
        self.head = None

    def Insert(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            self.head.next = NewNode
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = NewNode
            NewNode.next = self.head

    def Display(self):
        current = self.head
        while current.next != self.head:
            print(f"|{current.data}|-->",end="")
            current = current.next
        if current.next == self.head:
            print(f"|{current.data}|-->",end="")
            print(f"|{current.next.data}|")



    def Sorting(self):
        List = []
        current = self.head
        while current.next != self.head:
            List.append(current.data)
            current = current.next
        if current.next == self.head:
            List.append(current.data)

        List.sort()

        current = self.head
        for Data in List:
            current.data = Data
            current = current.next

        SCLL.Display()

SCLL = SortingCircularLinkedList()

SCLL.Insert(10)
SCLL.Insert(5)
SCLL.Insert(26)

SCLL.Display()

SCLL.Sorting()


