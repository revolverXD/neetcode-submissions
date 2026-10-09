class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        add_arr = [0] * len(self.arr)
        self.arr = self.arr + add_arr
        self.capacity = 2* self.capacity


    def getSize(self) -> int:
        non_empty = [element for element in self.arr if element]
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
