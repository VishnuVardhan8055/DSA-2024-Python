class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def Insert(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = NewNode

    def Display(self):
        current = self.head
        while current:
            print(f"|{current.data}|-->",end="")
            current = current.next
        print("|None|")


    def Delete(self):
        if self.head:
            self.head = self.head.next


    def ReverseLinkedList(self, prev=None):
        prev = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev


LL = LinkedList()
LL.Insert(1)
LL.Insert(2)
LL.Insert(3)
LL.Insert(4)


LL.Display()

LL.Delete()

LL.ReverseLinkedList()

LL.Display()







