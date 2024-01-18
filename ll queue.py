#IMPLEMENTATION USING LINKED LIST ENQUEUE

class LinkedListQueue:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, element):
        newNode = self.Node(element)
        if newNode is None:
            print("New node is not created")
            return
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def traverseQueue(self):
        currNode = self.head
        while currNode:
            print(currNode.data)
            currNode = currNode.next

if __name__ == "__main__":
    q = LinkedListQueue()
    q.enqueue(31)
    q.enqueue(13)
    q.traverseQueue()

#IMPLEMENTATION USING LL DEQUEUE
class LinkedListQueue:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

        def enqueue(self, element):
            newNode = self.Node(element)
            if newNode is None:
                print("New node is not created")
                return
            if self.size == 0:
                self.head = newNode
                self.tail = newNode
                self.size += 1
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.size += 1

        def dequeue(self):
            if self.size == 0:
                print("Queue underflow occurred")
                return
            deletedValue = self.head.data
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.size -= 1
            return deletedValue

        def traverseQueue(self):
            currNode = self.head
            while currNode:
                print(currNode.data)
                currNode = currNode.next


    if __name__ == "__main__":
        q = LinkedListQueue()
        q.enqueue(31)
        q.enqueue(13)
        print("Deleted value:", q.dequeue())
        print("Deleted value:", q.dequeue())
        q.traverseQueue()
        q.enqueue(7)
        q.enqueue(56)
        q.traverseQueue()