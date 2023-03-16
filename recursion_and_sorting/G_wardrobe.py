def cloths_sort(array_length, array):
    result_pink = []
    result_yellow = []
    result_red = []
    for value in array:
        if value == '0':
            result_pink += value
        if value == '1':
            result_yellow += value
        if value == '2':
            result_red += value
    result_final = result_pink + result_yellow + result_red
    return result_final


if __name__ == '__main__':
    array_length = int(input())
    array = [x for x in input().split()]
    print(*cloths_sort(array_length, array))
