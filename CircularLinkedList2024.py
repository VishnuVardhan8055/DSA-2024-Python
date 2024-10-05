class Node:
    def __init__(self,Data):
        self.data = Data
        self.Next = None
class CircularLinkedList:

    def __init__(self):
        self.head = None

    def Insert(self,data):

        NewNode = Node(data)

        if self.head is None:
            self.head = NewNode
            self.head.next = self.head
        else:
            current = self.head

            while current.next != self.head:

                current = current.next
            current.next = NewNode
            NewNode.next = self.head

    def Display(self):
        if self.head is None:
            print("Circular linked list is empty")

        else:
            current = self.head
            while current.next != self.head:
                print(f"|{current.data}|-->", end="")
                current = current.next
                if current.next == self.head:
                    print(f"|{current.data}|-->",end='')
            #print(f"|{current.data}|-->",end='')
            print(f"|{current.next.data}|")

    def Delete(self):
        if self.head is None:
            print("Circular linked list is empty")
        elif self.head.next == self.head:  # Single node case
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def DeleteLAST(self):
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        prev.next = self.head





CL = CircularLinkedList()
CL.Insert(1)
CL.Insert(2)
CL.Insert(3)
CL.Insert(4)

CL.Display()

CL.Delete()

CL.Display()

CL.DeleteLAST()

CL.Display()



