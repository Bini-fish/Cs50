class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Invalid capacity")
        else:
            self._capacity = capacity
            self._size = 0
    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Exceeded capacity")
        else:
            self.size += n
        

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("There is no enough cookies")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity 
    @capacity.setter
    def capacity(self, capacity):
        if capacity:
            self._capacity = capacity
        else:
            raise ValueError("Invalid value")
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size=0):
        if size < 0:
            raise ValueError("It's empty")
        else:
            self._size = size


    

def main():
    
    jar = Jar(25)
    jar.deposit(16)
    jar.withdraw(5)
    jar.withdraw(2)
    print(jar)
    

if __name__ == "__main__":
    main()