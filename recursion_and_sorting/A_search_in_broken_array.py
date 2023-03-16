def broken_search(nums: list, target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if nums[middle_index] == target:
            return middle_index
        if nums[left_index] <= nums[middle_index]:
            if nums[left_index] <= target < nums[middle_index]:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        else:
            if nums[middle_index] < target <= nums[right_index]:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
    return - 1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
