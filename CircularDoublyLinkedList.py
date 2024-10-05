class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert(self,data):
        NewNode = Node(data)

        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
            self.next = self.head
            self.prev = self.head

        else:

            NewNode.prev = self.tail
            NewNode.next = self.head
            self.tail.next = NewNode
            self.head.prev = NewNode
            self.tail = NewNode


    def Display(self):
        current = self.head
        while current.next != self.head:
            print(f"|{current.data}|--->",end='')
            current = current.next
            if current.next == self.head:
                print(f"|{current.data}|--->",end='')
        print(f"|{current.next.data}|")

    def DeleteFirst(self):
        self.head = self.head.next
        self.tail.next = self.head
        self.head.prev = self.tail


    def DeleteLast(self):
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail


CDLL = CircularLinkedList()

CDLL.Insert(10)
CDLL.Insert(20)
CDLL.Insert(30)
CDLL.Insert(40)

CDLL.Display()

CDLL.DeleteLast()

CDLL.Display()

CDLL.DeleteFirst()

CDLL.Display()
