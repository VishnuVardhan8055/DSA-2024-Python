class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SortingLinkedList:
    def __init__(self):
        self.head = None

    def Insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def Display(self):
        current = self.head
        while current:
            print(f"|{current.data}|-->",end="")
            current = current.next
        print()

    def Sorting(self):
        List = []
        current = self.head
        while current:
            List.append(current.data)
            current = current.next

        print(List)

        List.sort(reverse=True)

        current = self.head
        for DATA in List:
            current.data = DATA
            current = current.next

        print(List)

        SLL.Display()

SLL = SortingLinkedList()

SLL.Insert(2)
SLL.Insert(-3)
SLL.Insert(-1)

SLL.Display()

SLL.Sorting()

