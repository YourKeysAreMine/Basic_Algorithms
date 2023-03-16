class MyQueueSized:
    def __init__(self, n) -> None:
        self.items = [None] * n
        self.number_of_elements = 0
        self.head = 0
        self.tail = 0
        self.max_n = n
    
    def size(self):
        return self.number_of_elements
    
    def peek(self):
        return self.items[self.head]
    
    def push(self, x):
        if self.number_of_elements != self.max_n:
            self.items[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.number_of_elements += 1
        else:
            print('error')

    
    def pop(self):
        if self.number_of_elements == 0:
            return None
        x = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.number_of_elements -= 1
        return x


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    my_queue = MyQueueSized(max_size)
    for request in range(n):
        command = input().split()
        if command[0] == 'size':
            print(my_queue.size())
        if command[0] == 'peek':
            print(my_queue.peek())
        if command[0] == 'pop':
            print(my_queue.pop())
        if command[0] == 'push':
            my_queue.push(command[1])