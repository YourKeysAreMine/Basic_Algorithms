class MaxDequeSizeError(Exception):
	
    def __init__(self, message = 'Превышен размер дека'):
        self.message = message
    
    def __str__(self):
        return self.message


class DequeEmptyError(Exception):
	
    def __init__(self, message = 'Дек - пуст'):
        self.message = message
    
    def __str__(self):
        return self.message


class Deque:
    
    def __init__(self, n) -> None:
        self.__queue = [None] * n
        self.__max_deck_size = n
        self.__front_index = 1
        self.__back_index = 0
        self.__size = 0
    
    def push_back(self, x):
        if self.__size != self.__max_deck_size:
            self.__queue[self.__back_index] = x
            self.__back_index = self.__get_new_index(self.__back_index, -1)
            self.__size = (self.__size + 1)
        else:
            raise MaxDequeSizeError()
    
    def push_front(self, x):
        if self.__size != self.__max_deck_size:
            self.__queue[self.__front_index] = x
            self.__front_index = self.__get_new_index(self.__front_index, +1)
            self.__size = (self.__size + 1)
        else:
            raise MaxDequeSizeError()
    
    def pop_back(self):
        if self.__size == 0:
            raise DequeEmptyError()
        else:
            self.__back_index = self.__get_new_index(self.__back_index, +1)
            result = self.__queue[self.__back_index]
            self.__queue[self.__back_index] = None
            self.__size = (self.__size - 1)
            print(result)

    def pop_front(self):
        if self.__size == 0:
            raise DequeEmptyError()
        else:
            self.__front_index = self.__get_new_index(self.__front_index, -1)
            result = self.__queue[self.__front_index]
            self.__queue[self.__front_index] = None
            self.__size = (self.__size - 1)
            print(result)
    
    def __get_new_index(self, index, new):
        return (index + new) % self.__max_deck_size


if __name__ == '__main__':
    n = int(input())
    deque_size = int(input())
    my_deque = Deque(deque_size)
    for request in range(n):
        try:
            command, *params = input().split()
            result = getattr(my_deque, command)(*params)
        except MaxDequeSizeError:
            print('error')
        except DequeEmptyError:
            print('error')
        except Exception:
            print('Нужный метод не найден!')
