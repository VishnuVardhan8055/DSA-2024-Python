class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinearQueue:
    def __init__(self):
        self.Front = None
        self.Rear = None

    def EnQueue(self,data):

        NewNode = Node(data)
        if self.Rear is None:
            self.Front = NewNode
            self.Rear = NewNode
        else:
            self.Rear.next = NewNode
            self.Rear = NewNode

    def DeQueue(self):
        if self.Front and self.Rear is None:
            return "Queue Is Empty"
        else:
            temp = self.Front
            self.Front = temp.next

    def Peek(self):
        print(self.Front.data)
        #return self.Front.data

    def Size(self):
        count = 0
        temp = self.Front
        while temp:
            count = count+1
            temp = temp.next
        #return count
        print(count)

    def Display(self):
        temp = self.Front
        while temp:
            print(f"|{temp.data}|<--->",end="")
            temp = temp.next
        print()

LQ = LinearQueue()

LQ.EnQueue("B")
LQ.EnQueue("A")
LQ.EnQueue("C")
LQ.EnQueue("E")

LQ.Display()

LQ.DeQueue()

LQ.Display()

LQ.Peek()

LQ.Size()

