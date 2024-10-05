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

    def Sorting(self):
        if self.head is None:
            return  # Handle empty list

        List = []
        current = self.head
        while True:
            List.append(current.data)
            current = current.next
            if current == self.head:
                break


        List.sort()

        current = self.head
        for data in List:
            current.data = data
            current = current.next

        print("Sorted Circular Doubly Linked List:")
        self.Display()



CDLL = CircularLinkedList()

CDLL.Insert(1)
CDLL.Insert(0)
CDLL.Insert(-99)
CDLL.Insert(500)

CDLL.Display()

CDLL.Sorting()