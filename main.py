# implementation of array first program
class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0
        self.capacity = capacity
    def insertAtLast(self,element):
        if self.size == self.capacity:
            print("array overflow")
            return
        self.data[self.size] = element
        self.size +=1
    def inbetween(self,index,element):
        if self.size==self.capacity:
            print("o")
            return
        for i in range(self.size,index,-1):
            self.data[i]=self.data[i-1]
        self.data[index]=element
        self.size=+1
    def atfirst(self,element):
        self.inbetween(0,element)

if __name__ == "__main__":
    array1=Array(4)
    print(array1.data)
    array1.insertAtLast(15)
    array1.insertAtLast(90)
    array1.insertAtLast(78)
    array1.inbetween(2,'m')
    array1.atfirst('s')
    print(array1.data)

