def bubble_sort(array_length, array):
    changed = True
    for i in range(array_length - 1):
        for index, number in enumerate(array):
            if index < array_length - 1:
                second_number = array[index + 1]
                if number > second_number:
                    changed = True
                    array[index] = second_number
                    array[index + 1] = number
        if changed:
            print(*array)
            changed = False


if __name__ == '__main__':
    array_length = int(input())
    array = [int(x) for x in input().split()]
    bubble_sort(array_length, array)
