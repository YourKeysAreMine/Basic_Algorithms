def comparator(first_number, second_number):
    return first_number < second_number


def big_number(array_length, array, less):
    for i in range(1, array_length):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and less(int(array[j] + item_to_insert), int(item_to_insert + array[j])):
            first_number = array[j]
            second_number = array[j + 1]
            array[j] = second_number
            array[j + 1] = first_number
            j -= 1
    return (''.join(array))

if __name__ == '__main__':
    array_length = int(input())
    array = input().split()
    print(big_number(array_length, array, comparator))
