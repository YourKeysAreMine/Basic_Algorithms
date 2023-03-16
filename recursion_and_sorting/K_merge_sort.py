def merge(arr, lf, mid, rg):
    result = []
    left_array = arr[lf: mid]
    right_array = arr[mid: rg]
    left_iterator = 0
    right_iterator = 0
    while (left_iterator < len(left_array)
           and right_iterator < len(right_array)):
        if left_array[left_iterator] <= right_array[right_iterator]:
            result.append(left_array[left_iterator])
            left_iterator += 1
        else:
            result.append(right_array[right_iterator])
            right_iterator += 1
    if left_iterator < len(left_array):
        result += left_array[left_iterator:]
    if right_iterator < len(right_array):
        result += right_array[right_iterator:]
    return result


def merge_sort(arr, lf, rg):
    if rg - lf >= 2:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected