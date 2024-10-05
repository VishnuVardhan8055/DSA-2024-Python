class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode
            NewNode.prev = self.tail
            self.tail = NewNode

    def Display(self):
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

            # Print the data in a readable format showing previous and next node data
            #print(f"|{prev_data}| <--- ||{current.data}|| ---> |{next_data}|", end="")
            print(f"|{current.data}|-->",end="")
            current = current.next
        print()  # For clean output

    def Sorting(self):

        List = []
        current = self.head
        while current:
            List.append(current.data)
            current = current.next


        List.sort()


        current = self.head
        for data in List:
            current.data = data
            current = current.next

        print("Sorted Doubly Linked List:")
        self.Display()


# Example usage
DDL = DoublyLinkedList()

DDL.Insert(10)
DDL.Insert(9)
DDL.Insert(-1)
DDL.Insert(30)

print("Original Doubly Linked List:")
DDL.Display()

# Perform sorting
DDL.Sorting()
