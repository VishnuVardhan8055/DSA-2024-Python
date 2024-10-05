class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.Front = None
        self.Rear = None

    def EnQueue(self,data):
        NewNode = Node(data)
        if self.Front is None:
            self.Front = NewNode
            self.Rear = NewNode
            NewNode.next = NewNode

        else:
            self.Rear.next = NewNode
            self.Rear = NewNode
            NewNode.next = self.Front

    def DeQueue(self):
        self.Front = self.Front.next
        self.Rear.next = self.Front


    def Peek(self):
        if self.Front is None:
            print("Queue Is Empty")
        print(self.Front.data)

    def Size(self):
        count = 0
        temp = self.Front
        while temp:
            count += 1
            temp = temp.next
            if temp.next == self.Front:
                break
        print(count)

    def Display(self):
        temp = self.Front
        while temp:
            print(f"|{temp.data}|<--->",end='')
            temp = temp.next
            if temp.next == self.Front:
                print(f"|{temp.data}|<--->",end="")
                break
        print(f"|{temp.next.data}|")
        print()

    def Empty(self):
        if self.Front and self.Rear is None:
            pass

CQ = CircularQueue()

CQ.EnQueue("A")
CQ.EnQueue("B")
CQ.EnQueue("C")
CQ.EnQueue("D")

CQ.Display()

CQ.DeQueue()


CQ.Display()
CQ.Size()
CQ.Peek()




