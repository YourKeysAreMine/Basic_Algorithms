class StackMaxEffective:
     def __init__(self):
        self.items = []
        self.efficient_items = []

     def push(self, item):
        if len(self.efficient_items) == 0:
            self.items.append(item)
            self.efficient_items.append(item)
        elif item >= self.efficient_items[-1]:
            self.items.append(item)
            self.efficient_items.append(item)
        else:
            self.items.append(item)
            self.efficient_items.append(self.efficient_items[-1])

     def pop(self):
        if len(self.items) == 0:
            return "error"
        else:
            self.efficient_items.pop()
            return self.items.pop()

     def get_max(self):
        if len(self.items) == 0:
             return "None"
        else:
            return self.efficient_items[-1]


if __name__ == '__main__':
    stack = StackMaxEffective()
    n = int(input())
    result = []
    for index in range(n): 
        command = input().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        if command[0] == 'get_max':
            result.append(stack.get_max())
    for index in result:
        print(index)