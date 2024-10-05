class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def Enqueue(self,data):
        newNode = Node(data)
        if self.front is None:
            self.front = newNode
        else:
            prev = None
            temp = self.front
            while temp and temp.data >= data:
                prev = temp
                temp = temp.next
            newNode.next = temp
            if prev is None:
                self.front = newNode
            else:
                prev.next = newNode

    def Display(self):
        temp = self.front
        while temp:
            print(f"|{temp.data}|--->",end='')
            temp = temp.next

PQ = PriorityQueue()

PQ.Enqueue(2)
PQ.Enqueue(3)
PQ.Enqueue(1)

PQ.Display()



