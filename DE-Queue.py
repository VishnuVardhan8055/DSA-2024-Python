class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DE_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def FrontEnQueue(self,data):
        NewNode = Node(data)
        if self.front is None:
            self.front = NewNode
            self.rear = NewNode
        else:
            NewNode.next = self.front
            self.front = NewNode

    def RearEnQueue(self,data):
        NewNode = Node(data)
        if self.front is None:
            self.front = NewNode
            self.rear = NewNode
        else:
            self.rear.next = NewNode
            self.rear = NewNode

    def FrontDeQueue(self):
        self.front = self.front.next

    def rearDeQueue(self):
        prev = self.front
        while prev.next != self.rear:
            prev = prev.next
        prev.next = None
        self.rear = prev

    def Display(self):

        temp = self.front
        while temp:
            print(f"|{temp.data}|-->",end='')
            temp = temp.next
        print()


DE = DE_Queue()

DE.FrontEnQueue(2)
DE.FrontEnQueue(4)
DE.RearEnQueue(3)
DE.FrontEnQueue(4)

DE.Display()



DE.rearDeQueue()

DE.Display()

DE.FrontDeQueue()

DE.Display()
