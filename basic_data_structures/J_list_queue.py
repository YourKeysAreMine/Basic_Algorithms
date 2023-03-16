class ListQueue:
    def __init__(self) -> None:
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def get(self):
        if len(self.items) == 0:
            return 'error'
        x = self.items[-1]
        self.items.pop()
        return x
    
    def put(self, x):
        self.items.insert(0, x)


if __name__ == '__main__':
    n = int(input())
    my_queue = ListQueue()
    for request in range(n):
        command = input().split()
        if command[0] == 'size':
            print(my_queue.size())
        if command[0] == 'get':
            print(my_queue.get())
        if command[0] == 'put':
            my_queue.put(command[1])
