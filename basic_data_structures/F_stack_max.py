class StackMax:
     def __init__(self):
        self.items = []

     def push(self, item):
        self.items.append(item)

     def pop(self):
        if len(self.items) == 0:
            return "error"
        else:
            return self.items.pop()

     def get_max(self):
        if len(self.items) == 0:
             return "None"
        else:
            return max(self.items)


if __name__ == '__main__':
    stack = StackMax()
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