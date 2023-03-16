OPERATORS = {
    '/': lambda x, y: x // y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
}

class Stack:
    def __init__(self):
        self.__numbers_list = []
    
    def push(self, value):
        self.__numbers_list.append(value)
    
    def pop(self):
        if len(self.__numbers_list) != 0:
            return self.__numbers_list.pop()
        else:
            raise IndexError('Список пуст')

def calculate_result(sequence):
    stack = Stack()
    for value in sequence:
        try:
            stack.push(int(value))
        except ValueError:
            second_value = stack.pop()
            first_value = stack.pop()
            result = OPERATORS[value](first_value, second_value)
            stack.push(result)
    return stack.pop()
        

if __name__ == '__main__':
    sequence = input().split()
    print(calculate_result(sequence))
