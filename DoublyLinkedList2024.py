class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert(self,data):
        NewNode = Node(data)

        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode
            NewNode.prev = self.tail
            self.tail = NewNode

    def display(self):
        current = self.head
        while current:
            if current.prev is None:
                prev_data = "None"
            else:
                prev_data = current.prev.data

            if current.next is None:
                next_data = "None"
            else:
                next_data = current.next.data

            #print(f"|{current.data}| (prev: {prev_data}  next: {next_data})-->", end="")
            print(f"|{prev_data}| ---> ||{current.data}|| ---> |{next_data}| --->", end="")
            current = current.next
        print("None")


    def DeleteFirst(self):
        self.head = self.head.next
        self.head.prev = None

    def DeleteLast(self):
        self.tail = self.tail.prev
        self.tail.next = None



DDL = DoublyLinkedList()

DDL.Insert(10)
DDL.Insert(20)
DDL.Insert(30)
DDL.Insert(40)

DDL.display()


DDL.DeleteFirst()


DDL.display()

DDL.DeleteLast()

DDL.display()
