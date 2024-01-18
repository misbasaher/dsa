class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 10
        self.capacity = capacity


if __name__ == "__main__":
    a1 = Array(10)
    print(a1.data)


class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 10
        self.capacity = capacity

    # INSERTING AN ELEMENT AT lastmethod
    def insert_at_last(self, element):
        if self.size == self.capacity:
            print("array overflow")
            return
        self.data[self.size] = element
        self.size += 1


if __name__ == "__main__":
    a1 = Array(15)
    print(a1.data)
    a1.insert_at_last(67)
    a1.insert_at_last(13)
    a1.insert_at_last(87)
    print(a1.data)


class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0  # Initialize size to 0
        self.capacity = capacity

# INSERTING AN ELEMENT AT LAST
    def insert_at_last(self, element):
        if self.size == self.capacity:
            print("array overflow")
            return
        self.data[self.size] = element
        self.size += 1

# INSERTING AN ELEMENT IN BETWEEN
    def insert_in_between(self, index, element):
        if self.size == self.capacity:
            print("array overflow")
            return
        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index] = element
        self.size += 1

# INSERTING AN ELEMENT AT FIRST
    def insert_at_first(self, element):
        self.insert_in_between(0, element)


if __name__ == "__main__":
    a1 = Array(15)
    print(a1.data)
    a1.insert_at_last(67)
    a1.insert_at_last(13)
    a1.insert_in_between(0, 31)
    a1.insert_at_first(56)
    print(a1.data)

class Array:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0  # Initialize size to 0
        self.capacity = capacity

# INSERTING AN ELEMENT AT LAST
    def insert_at_last(self, element):
        if self.size == self.capacity:
            print("array overflow")
            return
        self.data[self.size] = element
        self.size += 1

# INSERTING AN ELEMENT IN BETWEEN
    def insert_in_between(self, index, element):
        if self.size == self.capacity:
            print("array overflow")
            return
        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]
        self.data[index] = element
        self.size += 1

# INSERTING AN ELEMENT AT FIRST
    def insert_at_first(self, element):
        self.insert_in_between(0, element)

# DELETING THE ELEMENT AT LAST
    def delete_at_last(self):
        if self.size == 0:
            print("array underflow")
            return
        deletedValue = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return deletedValue

# DELETING THE ELEMENT AT THE GIVEN INDEX
    def delete_at_given_index(self, index):
        if self.size == 0:
            print("array underflow")
            return
        deletedValue = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        return deletedValue

# DELETING THE ELEMENT AT THE FIRST
    def delete_at_first(self):
        return self.delete_at_given_index(0)

if __name__ == "__main__":
    a1 = Array(15)
    print(a1.data)
    a1.insert_at_last(67)
    a1.insert_at_last(97)
    a1.insert_at_last(68)
    a1.insert_in_between(1, 31)
    a1.insert_at_last(98)
    a1.insert_in_between(7, 31)
    a1.insert_at_last(58)
    a1.insert_at_last(8)
    a1.insert_in_between(9, 81)
    a1.insert_in_between(8, 31)
    a1.insert_at_first(56)
    a1.insert_at_last(68)
    a1.insert_in_between(5, 31)
    print(a1.data)
    print("deleted value is:", a1.delete_at_last())
    print("deleted value is:", a1.delete_at_given_index(1))
    print("deleted value is:", a1.delete_at_first())
    print(a1.data)
