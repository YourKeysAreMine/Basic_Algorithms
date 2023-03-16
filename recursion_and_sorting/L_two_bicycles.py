def binary_search(array, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if array[mid] >= x > array[mid - 1] or mid == 0:
        return mid + 1
    elif x <= array[mid]:
        return binary_search(array, x, left, mid)
    else:
        return binary_search(array, x, mid + 1, right)


if __name__ == '__main__':
    array_size = int(input())
    array = [int(x) for x in input().split()]
    bicycle_price  = int(input())
    print(binary_search(
        array,
        bicycle_price,
        left = 0,
        right = len(array)
    ), end=" ")
    print(binary_search(
        array,
        bicycle_price * 2,
        left = 0,
        right = len(array)
    ))
