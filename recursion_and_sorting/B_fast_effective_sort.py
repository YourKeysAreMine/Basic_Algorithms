def quicksort(array: list, left_side: int, right_side: int):
    if left_side >= right_side:
        return -1
    left_changeable = left_side
    right_changeable = right_side
    pivot = array[(left_side + right_side)//2]
    while left_changeable <= right_changeable:
        while array[left_changeable] < pivot:
            left_changeable += 1
        while array[right_changeable] > pivot:
            right_changeable -= 1
        if left_changeable <= right_changeable:
            (array[left_changeable],
             array[right_changeable]) = (array[right_changeable],
                                         array[left_changeable])
            left_changeable += 1
            right_changeable -= 1
    quicksort(array, left_side=left_side, right_side=right_changeable)
    quicksort(array, left_side=left_changeable, right_side=right_side)


if __name__ == '__main__':
    number = int(input())
    input_array = []
    for _ in range(number):
        temporary_array = input().split()
        temporary_array[1] = - int(temporary_array[1])
        temporary_array[2] = int(temporary_array[2])
        input_array.append([temporary_array[1],
                            temporary_array[2],
                            temporary_array[0]])
    quicksort(input_array, left_side=0, right_side=number-1)
    print(*(list(zip(*input_array))[2]), sep="\n")
